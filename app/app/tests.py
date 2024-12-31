from django.test import SimpleTestCase
from app import my


# Create your tests here.
class CalTest(SimpleTestCase):
    def test_add(self):
        res = my.add_two_numbers(3, 4)
        self.assertEqual(res, 7)

    def test_subtract(self):
        res = my.subtract(10, 5)
        self.assertEqual(res, 5)
