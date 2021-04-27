import re
import csv
from pprint import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def crawl_starbucks_drinks():
    url = "https://www.starbucks.co.kr/menu/drink_list.do"

    # Use Selenium without live chrome window.
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Install
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(5)  # wait maximum 5sec for page loading

    browser.get(url)

    category_list = browser.find_elements_by_xpath(
        '//*[@id="container"]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd'
    )

    drink_db = {}

    for category in category_list:

        category_name = " ".join(
            category.find_element_by_tag_name("ul")
            .get_attribute("class")
            .split("_")[1:]
        )
        drink_list = category.find_elements_by_class_name("goDrinkView")

        print(
            f"[LOG] Processing {len(drink_list)} drinks in category {category_name}..."
        )

        # drink_list = drink_list[:1]

        for drink in drink_list:
            drink_id = drink.get_attribute("prod")
            drink_img_elem = drink.find_element_by_tag_name("img")
            drink_img_src = drink_img_elem.get_attribute("src")
            drink_name_kor = drink_img_elem.get_attribute("alt")
            drink_db[drink_id] = {
                "img_src": drink_img_src,
                "name_kor": drink_name_kor,
                "category": category_name,
            }

    print("[LOG] Starting Detail Search...")

    for drink_id in drink_db.keys():
        drink_detail_url = (
            "https://www.starbucks.co.kr/menu/drink_view.do?product_cd=" + drink_id
        )

        browser.get(drink_detail_url)
        drink_detail_info = browser.find_element_by_class_name("product_view_detail")

        drink_name_info = drink_detail_info.find_element_by_xpath(".//div[1]/h4").text

        name_kor = drink_name_info.split("\n")[0]
        name_eng = drink_detail_info.find_element_by_xpath(".//div[1]/h4/span[1]").text

        description = drink_detail_info.find_element_by_xpath(".//div[1]/p").text

        drink_size_info = drink_detail_info.find_element_by_id("product_info01").text

        size_ml = float(re.findall(r"(\d+|\d+ )ml", drink_size_info)[0])

        if re.findall(r"(\d.\d+|\d+) fl oz", drink_size_info):
            size_oz = float(re.findall(r"(\d.\d+|\d+) fl oz", drink_size_info)[0])

        nutrition_info_list = drink_detail_info.find_elements_by_xpath(
            ".//form/fieldset/div/div[2]/ul/li"
        )

        # Exclude not visible nutrition factors
        nutrition_info_list = list(
            filter(
                lambda n: n.get_attribute("style") != "display: none;",
                nutrition_info_list,
            )
        )

        nutrition_info_db = {}

        for nutrition_info in nutrition_info_list:
            name = nutrition_info.get_attribute("class").split(" ")[
                0
            ]  # Exclude "last" classname
            content = float(nutrition_info.find_element_by_xpath(".//dl/dd").text)
            nutrition_info_db[name] = content

        allegy_factor_info = drink_detail_info.find_element_by_xpath(
            ".//form/fieldset/div/div[3]/p"
        ).text

        if allegy_factor_info:
            allegy_factors_list = list(
                map(lambda s: s.strip(), allegy_factor_info.split(":")[1].split("/"))
            )

        drink_db[drink_id]["name_eng"] = name_eng
        drink_db[drink_id]["description"] = description
        drink_db[drink_id]["size_ml"] = size_ml

        if size_oz:
            drink_db[drink_id]["size_oz"] = size_oz
        if allegy_factor_info:
            drink_db[drink_id]["allegy_factors"] = allegy_factors_list
        else:
            drink_db[drink_id]["allegy_factors"] = []

        drink_db[drink_id] = {**drink_db[drink_id], **nutrition_info_db}

        pprint(drink_db[drink_id])

    browser.quit()

    return drink_db


def save_to_csv(db, file_path):
    print(f"[LOG] SAVING DATA IN CSV TO {file_path}...")

    column_names = list(list(db.values())[0].keys())
    data = list(db.values())

    with open(file_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        writer.writeheader()
        for d in data:
            writer.writerow(d)

    return


if __name__ == "__main__":
    drink_db = crawl_starbucks_drinks()
    save_to_csv(drink_db, "./data/starbucks_drinks.csv")
