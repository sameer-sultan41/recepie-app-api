from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2OperationalError


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    def test_wait_for_db_ready(self, patch_check):
        """Test waiting for db when db is available"""
        patch_check.return_value = True
        call_command('wait_for_db')
        patch_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patch_check):
        """Test waiting for db"""
        patch_check.side_effect = [Psycopg2OperationalError] * 3 + \
            [OperationalError] * 2 + [True]
        call_command('wait_for_db')
        self.assertEqual(patch_check.call_count, 6)
        patch_check.assert_called_with(databases=['default'])
