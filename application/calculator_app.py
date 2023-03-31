from appium.webdriver.common.appiumby import AppiumBy

from application.base_actions import BaseActions


class CalculatorPage(BaseActions):
    digit_zero = (AppiumBy.ACCESSIBILITY_ID, '0')
    button_dot = (AppiumBy.ACCESSIBILITY_ID, 'point')
    button_delete = (AppiumBy.ACCESSIBILITY_ID, 'delete')
    digit_one = (AppiumBy.ACCESSIBILITY_ID, '1')
    digit_two = (AppiumBy.ACCESSIBILITY_ID, '2')
    digit_three = (AppiumBy.ACCESSIBILITY_ID, '3')
    button_plus = (AppiumBy.ACCESSIBILITY_ID, 'plus')
    equals = (AppiumBy.ACCESSIBILITY_ID, 'equals')
    digit_four = (AppiumBy.ACCESSIBILITY_ID, '4')
    digit_five = (AppiumBy.ACCESSIBILITY_ID, '5')
    digit_six = (AppiumBy.ACCESSIBILITY_ID, '6')
    digit_seven = (AppiumBy.ACCESSIBILITY_ID, '7')
    digit_eight = (AppiumBy.ACCESSIBILITY_ID, '8')
    digit_nine = (AppiumBy.ACCESSIBILITY_ID, '9')
    button_minus = (AppiumBy.ACCESSIBILITY_ID, 'minus')
    button_multiply = (AppiumBy.ACCESSIBILITY_ID, 'multiply')
    button_divide = (AppiumBy.ACCESSIBILITY_ID, 'divide')
    button_percent = (AppiumBy.ACCESSIBILITY_ID, 'percent')
    button_parenthesis = (AppiumBy.ACCESSIBILITY_ID, 'left or right parenthesis')
    button_clear = (AppiumBy.ACCESSIBILITY_ID, 'clear')
    button_square_root = (AppiumBy.ACCESSIBILITY_ID, 'square root')
    button_pi = (AppiumBy.ACCESSIBILITY_ID, 'pi')
    button_power = (AppiumBy.ACCESSIBILITY_ID, 'power')
    button_factorial = (AppiumBy.ACCESSIBILITY_ID, 'factorial')
    button_expand = (AppiumBy.ACCESSIBILITY_ID, 'Expand')
    no_result_field = (AppiumBy.ACCESSIBILITY_ID, 'No result')
    result_preview = (AppiumBy.ID, 'com.google.android.calculator:id/result_preview')
    formula_field = (AppiumBy.ID, 'com.google.android.calculator:id/formula')
    result = (AppiumBy.ID, 'com.google.android.calculator:id/result_final')

    def __init__(self, driver):
        super().__init__(driver)

    def click_zero(self):
        self.click(self.digit_zero)

    def click_one(self):
        self.click(self.digit_one)

    def click_two(self):
        self.click(self.digit_two)

    def click_three(self):
        self.click(self.digit_three)

    def click_four(self):
        self.click(self.digit_four)

    def click_five(self):
        self.click(self.digit_five)

    def click_six(self):
        self.click(self.digit_six)

    def click_seven(self):
        self.click(self.digit_seven)

    def click_eight(self):
        self.click(self.digit_eight)

    def click_nine(self):
        self.click(self.digit_nine)

    def click_dot(self):
        self.click(self.button_dot)

    def click_minus(self):
        self.click(self.button_minus)

    def click_multiply(self):
        self.click(self.button_multiply)

    def click_divide(self):
        self.click(self.button_divide)

    def click_percent(self):
        self.click(self.button_percent)

    def click_parenthesis(self):
        self.click(self.button_parenthesis)

    def click_clear(self):
        self.click(self.button_clear)

    def click_square_root(self):
        self.click(self.button_square_root)

    def click_pi(self):
        self.click(self.button_pi)

    def click_power(self):
        self.click(self.button_power)

    def click_factorial(self):
        self.click(self.button_factorial)

    def click_plus(self):
        self.click(self.button_plus)

    def click_equals(self):
        self.click(self.equals)

    def get_result(self):
        return self.get_text(self.result)

    def click_expand(self):
        self.click(self.button_expand)

    def get_result_preview(self):
        return self.get_text(self.result_preview)

    def get_formula(self):
        return self.get_text(self.formula_field)
