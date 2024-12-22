import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Ingredient


class Command(BaseCommand):

    PATH_DATA, FILE_NAME = 'data', 'ingredients.csv'

    PATH = settings.BASE_DIR.parent.joinpath(PATH_DATA)

    FIELD_NAMES = ('name', 'measurement_unit')

    help = f'''Populates Database with the Data from csv-File Located within
{PATH_DATA}'''

    def handle(self, *args, **options) -> None:

        with open(self.PATH.joinpath(self.FILE_NAME), encoding='utf8') as file:
            reader = csv.DictReader(file, fieldnames=self.FIELD_NAMES)
            Ingredient.objects.bulk_create(Ingredient(**_) for _ in reader)

        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully Populated Database with the Data from
csv-File Located within {self.PATH_DATA}'''
            )
        )
