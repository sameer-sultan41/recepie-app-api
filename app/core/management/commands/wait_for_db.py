from django.core.management.base import BaseCommand  # noqa
import time
from django.db.utils import OperationalError  # noqa
from psycopg2 import OperationalError as Psycopg2OperationalError # noqa


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('wait for database connection...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write('Waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
