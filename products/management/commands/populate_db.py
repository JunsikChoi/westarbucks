from django.core.management.base import BaseCommand, CommandError
from products.utils import initialize_db


class Command(BaseCommand):
    help = "Check if crawled data exist in ./data folder. if not, start crawler and save crawled data to data folder"

    def add_arguments(self, parser):
        parser.add_argument(
            "-f", "--filename", type=str, default="starbucks_drinks.csv"
        )

    def handle(self, *args, **options):
        path = "./data/{}".format(options["filename"])

        self.stdout.write(self.style.NOTICE("Populating DB..."))

        try:
            initialize_db.populate_db(path)
        except Exception as e:
            print(e)
            self.stdout.write(
                self.style.ERROR(
                    "Something went wrong.. See the error msg above! :( \nError Occurred."
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("Successfully Populated DB "))
