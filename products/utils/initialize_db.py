import sys, os
import ast

# sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from products.utils.crawler import load_to_csv
import products.models as pm
from django.db import Error


def create_menu():
    try:
        menu = pm.Menu.objects.create(name="drinks")
    except Error as e:
        print(e.__cause__)
        menu = pm.Menu.objects.get(name="drinks")
    finally:
        return menu


def populate_db(path_to_db=None):

    if path_to_db:
        db = load_to_csv(path_to_db)
    else:
        db = load_to_csv()

    # Create Menu data
    # db has only one Menu = drinks
    # try:
    #     menu = pm.Menu.objects.create(name="drinks")
    # except Error as e:
    #     print(e.__cause__)
    menu = create_menu()

    # Create Category data
    category_set = {data["category"] for data in db.values()}

    for category in category_set:
        pm.Category.objects.create(name=category, menu=menu)

    # Create Allegy Factor data
    allegy_set = set()
    for data in db.values():
        allegy_factor_list = ast.literal_eval(data["allegy_factors"])
        allegy_set.update(allegy_factor_list)
    for allegy in allegy_set:
        pm.Allegy.objects.create(name=allegy)

    # Create Product data
    for data in db.values():
        nutrition = pm.Nutrition.objects.create(
            one_serving_kcal=data["kcal"],
            sodium_mg=data["sodium"],
            saturated_fat_g=data["sat_FAT"],
            sugars_g=data["sugars"],
            protein_g=data["protein"],
            caffeine_mg=data["caffeine"],
            size_ml=data["size_ml"],
            size_ounce=data["size_oz"],
        )
        product = pm.Product.objects.create(
            category=pm.Category.objects.get(name=data["category"]),
            nutrition=nutrition,
            korean_name=data["name_kor"],
            english_name=data["name_eng"],
            description=data["description"],
        )
        allegy_factors = ast.literal_eval(data["allegy_factors"])
        if allegy_factors:
            for allegy in allegy_factors:
                product.allegies.add(pm.Allegy.objects.get(name=allegy))
        pm.Image.objects.create(image_url=data["img_src"], drink=product)

    return


if __name__ == "__main__":
    populate_db()