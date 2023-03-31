from application.calculator_app import CalculatorPage
from tests.base_test import BaseTest


class TestAddition(BaseTest):

    def test_addition(self):
        calc = CalculatorPage(self.driver)
        calc.click_one()
        calc.click_plus()
        calc.click_two()
        calc.click_equals()
        assert calc.get_result() == '3'

    def test_addition_negative(self):
        calc = CalculatorPage(self.driver)
        calc.click_two()
        calc.click_plus()
        calc.click_three()
        calc.click_equals()
        assert calc.get_result() != '4'
