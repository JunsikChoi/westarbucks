from django.core.management.base import BaseCommand, CommandError
from products.utils import crawler


class Command(BaseCommand):
    help = "Check if crawled data exist in ./data folder. if not, start crawler and save crawled data to data folder"

    def add_arguments(self, parser):
        parser.add_argument(
            "-f", "--filename", type=str, default="starbucks_drinks.csv"
        )

    def handle(self, *args, **options):

        path = "./data/%s".format(options["filename"])
        self.stdout.write(self.style.NOTICE("Start Crawler..."))
        try:
            drink_db = crawler.crawl_starbucks_drinks()
            crawler.save_to_csv(drink_db, path)
        except:
            self.stdout.write(
                self.style.ERROR("Something went wrong.. :( \n Error Occurred.")
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully Crawled Data and Stored in %s".format(path)
            )
        )
