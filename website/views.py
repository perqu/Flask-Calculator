from flask import Blueprint, render_template, request
from .Calculator import Calculator

calc = Calculator()

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "%" in request.form:
            calc.button_operation("%")
        elif "7" in request.form:
            calc.button_click(7)
        elif "8" in request.form:
            calc.button_click(8)
        elif "9" in request.form:
            calc.button_click(9)
        elif "/" in request.form:
            calc.button_operation("/")

        elif "+-" in request.form:
            calc.button_change()
        elif "4" in request.form:
            calc.button_click(4)
        elif "5" in request.form:
            calc.button_click(5)
        elif "6" in request.form:
            calc.button_click(6)
        elif "x" in request.form:
            calc.button_operation("x")

        elif "c" in request.form:
            calc.button_clear()
        elif "1" in request.form:
            calc.button_click(1)
        elif "2" in request.form:
            calc.button_click(2)
        elif "3" in request.form:
            calc.button_click(3)
        elif "+" in request.form:
            calc.button_operation("+")

        elif "√" in request.form:
            calc.button_operation("√")
        elif "0" in request.form:
            calc.button_click(0)
        elif "." in request.form:
            calc.button_dot()
        elif "=" in request.form:
            calc.count()
        elif "-" in request.form:
            calc.button_operation("-")

        elif "2√" in request.form:
            calc.button_operation("2√")
        elif "**" in request.form:
            calc.button_operation("**")
        elif "x**2" in request.form:
            calc.button_operation("x**2")
        elif "mod" in request.form:
            calc.button_operation("mod")
        elif "<--" in request.form:
            calc.button_backspace()

    # print([calc.number1, calc.number2, calc.operation, calc.current_number])
    return render_template("calc.html", screen=calc.display_operator())
