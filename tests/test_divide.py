from application.calculator_app import CalculatorPage
from tests.base_test import BaseTest


class TestDivide(BaseTest):
    def test_divide(self):
        calc = CalculatorPage(self.driver)
        calc.click_eight()
        calc.click_divide()
        calc.click_two()
        calc.click_equals()
        assert calc.get_result() == '4'

    def test_divide_negative(self):
        calc = CalculatorPage(self.driver)
        calc.click_nine()
        calc.click_divide()
        calc.click_three()
        calc.click_equals()
        assert calc.get_result() != '7'

    def test_divide_by_zero(self):
        calc = CalculatorPage(self.driver)
        calc.click_one()
        calc.click_divide()
        calc.click_zero()
        calc.click_equals()
        assert calc.get_result_preview() == 'Can\'t divide by 0'

