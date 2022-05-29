import pytest
from website.Calculator import Calculator


class TestCalculator:
    def test_calc(self):
        calc = Calculator()
        assert isinstance(calc, Calculator)

    ### BUTTON CLICK ###
    def test_button_click(self):
        calc = Calculator()
        calc.button_click(1)
        assert calc.get_current_number() == "1"

    ### BUTTON CHANGE ###
    def test_button_change_empty(self):
        calc = Calculator()
        calc.button_change()
        assert calc.get_current_number() == "-"

    def test_button_change_number_positive(self):
        calc = Calculator()
        calc.button_click(5)
        calc.button_change()
        assert calc.get_current_number() == "-5"

    def test_button_change_number_negative(self):
        calc = Calculator()
        calc.button_click(-5)
        calc.button_change()
        assert calc.get_current_number() == "5"

    def test_button_change_minus(self):
        calc = Calculator()
        calc.button_change()
        calc.button_change()
        assert calc.get_current_number() == ""

    def test_button_change_minus_after_count(self):
        calc = Calculator()
        calc.button_click(5)
        calc.button_operation("-")
        calc.button_click(10)
        calc.count()
        calc.button_change()
        assert calc.get_number1() == 5

    def test_button_change_with_operation(self):
        calc = Calculator()
        calc.button_click(1)
        calc.button_change()
        calc.button_operation("-")
        assert calc.display_operator() == "-1 -"

    ### BUTTON BACKSPACE ###
    def test_button_backspace_one_digit(self):
        calc = Calculator()
        calc.button_click(5)
        calc.button_backspace()
        assert calc.get_current_number() == ""

    def test_button_backspace_two_digits(self):
        calc = Calculator()
        calc.button_click(50)
        calc.button_backspace()
        assert calc.get_current_number() == "5"

    def test_button_backspace_after_operation(self):
        calc = Calculator()
        calc.button_click(5)
        calc.button_operation("x**2")
        calc.button_backspace()
        assert calc.display_operator() == "25"

    ### TEST BUTTON CLEAR ###
    def test_button_clear(self):
        calc = Calculator()
        calc.button_click(2)
        calc.button_operation("+")
        calc.button_click(6)
        calc.count()
        calc.button_clear()
        assert calc.get_number1() == None
        assert calc.get_number2() == None
        assert calc.get_operation() == None
        assert calc.get_current_number() == ""
        assert calc.is_error() == False

    ### BUTTON OPERATION ###
    def test_button_operation(self):
        calc = Calculator()
        calc.button_operation("+")
        assert calc.get_operation() == "+"

    def test_button_operation_count(self):
        calc = Calculator()
        calc.button_click(2)
        calc.button_operation("x**2")
        assert calc.get_number1() == 4

    def test_button_operation_change(self):
        calc = Calculator()
        calc.button_click(2)
        calc.button_operation("-")
        calc.button_operation("+")
        assert calc.display_operator() == "2 +"

    ### BUTTON DOT ###
    def test_button_dot_already_dot(self):
        calc = Calculator()
        calc.button_dot()
        first_dot = calc.get_current_number()
        calc.button_dot()
        second_dot = calc.get_current_number()
        assert first_dot == second_dot

    def test_button_dot_empty(self):
        calc = Calculator()
        calc.button_dot()
        assert calc.get_current_number() == "0."

    def test_button_dot_digit(self):
        calc = Calculator()
        calc.button_click(1)
        calc.button_dot()
        assert calc.get_current_number() == "1."

    ### DISPLAY OPERATOR ###
    def test_display_operator(self):
        calc = Calculator()
        calc.button_click(2)
        assert calc.display_operator() == "2"
        calc.button_operation("+")
        assert calc.display_operator() == "2 +"
        calc.button_click(6)
        assert calc.display_operator() == "2 + 6"
        calc.count()
        assert calc.display_operator() == "8"
        calc.button_click(1)
        assert calc.display_operator() == "1"

    ### ROUND TEST ###
    def test_round(self):
        calc = Calculator()
        calc.button_click(1)
        calc.button_operation("/")
        calc.button_click(3)
        calc.count()
        assert calc.get_number1() == 0.33333333

    ### ADDITIONION ###
    def test_add_two_int(self):
        calc = Calculator()
        calc.button_click(2)
        calc.button_operation("+")
        calc.button_click(6)
        calc.count()
        assert calc.get_number1() == 8

    def test_add_two_float(self):
        calc = Calculator()
        calc.button_click(2.5)
        calc.button_operation("+")
        calc.button_click(6.9)
        calc.count()
        assert calc.get_number1() == 9.4

    ### SUBSTRACTION ###
    def test_sub_two_int(self):
        calc = Calculator()
        calc.button_click(500)
        calc.button_operation("-")
        calc.button_click(6)
        calc.count()
        assert calc.get_number1() == 494

    def test_sub_two_float(self):
        calc = Calculator()
        calc.button_click(50.6)
        calc.button_operation("-")
        calc.button_click(6.2)
        calc.count()
        assert calc.get_number1() == 44.4

    ### MULTIPLICATION ###
    def test_mul_two_int(self):
        calc = Calculator()
        calc.button_click(2)
        calc.button_operation("x")
        calc.button_click(6)
        calc.count()
        assert calc.get_number1() == 12

    def test_mul_two_float(self):
        calc = Calculator()
        calc.button_click(2.5)
        calc.button_operation("x")
        calc.button_click(6.2)
        calc.count()
        assert calc.get_number1() == 15.5

    ### DIVISION ###
    def test_div_two_int(self):
        calc = Calculator()
        calc.button_click(6)
        calc.button_operation("/")
        calc.button_click(2)
        calc.count()
        assert calc.get_number1() == 3

    def test_div_two_float(self):
        calc = Calculator()
        calc.button_click(4.8)
        calc.button_operation("/")
        calc.button_click(2.4)
        calc.count()
        assert calc.get_number1() == 2

    def test_div_zero(self):
        calc = Calculator()
        calc.button_click(6)
        calc.button_operation("/")
        calc.button_click(0)
        calc.count()
        assert calc.display_operator() == "ERROR"

    ### MOD ###
    def test_mod_two_int(self):
        calc = Calculator()
        calc.button_click(7)
        calc.button_operation("mod")
        calc.button_click(2)
        calc.count()
        assert calc.get_number1() == 1

    def test_mod_two_int(self):
        calc = Calculator()
        calc.button_click(6)
        calc.button_operation("mod")
        calc.button_click(2.4)
        calc.count()
        assert calc.get_number1() == 1.2

    def test_mod_zero(self):
        calc = Calculator()
        calc.button_click(6)
        calc.button_operation("mod")
        calc.button_click(0)
        calc.count()
        assert calc.display_operator() == "ERROR"

    ### ROOT 2√ ###
    def test_root(self):
        calc = Calculator()
        calc.button_click(9)
        calc.button_operation("2√")
        assert calc.get_number1() == 3

    ### ROOT x√y ###
    def test_root_3(self):
        calc = Calculator()
        calc.button_click(3)
        calc.button_operation("√")
        calc.button_click(27)
        calc.count()
        assert calc.get_number1() == 3

    def test_root_0(self):
        calc = Calculator()
        calc.button_click(0)
        calc.button_operation("√")
        calc.button_click(27)
        calc.count()
        assert calc.is_error() == True

    def test_root_0_after_0(self):
        calc = Calculator()
        calc.button_operation("√")
        calc.button_click(27)
        calc.count()
        assert calc.is_error() == True

    ### POWER 2 ###
    def test_power_2(self):
        calc = Calculator()
        calc.button_click(3)
        calc.button_operation("x**2")
        assert calc.get_number1() == 9

    ### POWER x**y ###
    def test_power_2(self):
        calc = Calculator()
        calc.button_click(3)
        calc.button_operation("**")
        calc.button_click(3)
        calc.count()
        assert calc.get_number1() == 27

    ### PERCENT ###
    def test_percent_int(self):
        calc = Calculator()
        calc.button_click(100)
        calc.button_operation("%")
        assert calc.get_number1() == 1

    def test_percent_float(self):
        calc = Calculator()
        calc.button_click(99)
        calc.button_operation("%")
        assert calc.get_number1() == 0.99
