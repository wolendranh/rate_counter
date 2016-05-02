from django.test import TestCase
import utils
from .models import TableRow
# Create your tests here.


class UtilsModuleTestCase(TestCase):
    def test_no_table_rows(self):
        """
        without table rows, there is shouldn't be any result
        """
        table_rows = TableRow.objects.all()
        self.assertEqual(utils.get_result(table_rows), False)

    def test_no_coefficient_in_table_row(self):
        """
        without coefficient in table row, result should be zero:
        """
        test_row = TableRow(point=75, coefficient=0)
        table_rows = [test_row]
        self.assertEqual(utils.get_result(table_rows), False)

    def test_no_score_in_table_row(self):
        """
        without score in table row, result should be zero:
        """
        test_row = TableRow(point=0, coefficient=6)
        table_rows = [test_row]
        self.assertEqual(utils.get_result(table_rows), False)

    def test_coefficient_less_than_zero(self):
        test_row = TableRow(point=0, coefficient=-6)
        table_rows = [test_row]
        self.assertEqual(utils.get_result(table_rows), False)

    def test_proper_working_of_function_at_regular_case(self):
        test_row1 = TableRow(point=85, coefficient=6)
        test_row2 = TableRow(point=50, coefficient=4)
        table_rows = [test_row1, test_row2]
        self.assertEqual(utils.get_result(table_rows), (85*6 + 50*4)/(6+4))

    def test_color_if_less_than_71(self):
        result = 52.67
        self.assertEqual(utils.get_color(result), 'danger')

    def test_color_if_more_than_71_and_less_than_88(self):
        result = 87.9999
        self.assertEqual(utils.get_color(result), 'warning')

    def test_color_if_more_than_88(self):
        result = 96
        self.assertEqual(utils.get_color(result), 'success')

    # it is impossible to get the result, which will be bigger than 100, or less than 0.
    # restrictions of input fields will prevent such situations
