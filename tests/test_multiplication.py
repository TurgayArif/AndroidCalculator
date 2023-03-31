from application.calculator_app import CalculatorPage
from tests.base_test import BaseTest


class TestMultiplication(BaseTest):
    def test_multiply(self):
        calc = CalculatorPage(self.driver)
        calc.click_eight()
        calc.click_multiply()
        calc.click_two()
        calc.click_equals()
        assert calc.get_result() == '16'

    def test_multiply_negative(self):
        calc = CalculatorPage(self.driver)
        calc.click_seven()
        calc.click_multiply()
        calc.click_three()
        calc.click_equals()
        assert calc.get_result() != 20