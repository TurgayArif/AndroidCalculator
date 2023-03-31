from application.calculator_app import CalculatorPage
from tests.base_test import BaseTest


class TestSubtraction(BaseTest):

    def test_subtraction(self):
        calc = CalculatorPage(self.driver)
        calc.click_four()
        calc.click_minus()
        calc.click_two()
        calc.click_equals()
        assert calc.get_result() == '2'

    def test_subtraction_negative(self):
        calc = CalculatorPage(self.driver)
        calc.click_two()
        calc.click_minus()
        calc.click_one()
        calc.click_equals()
        assert calc.get_result() != '2'
        