def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


class Calculator:
    def __init__(self):
        self.__number1 = None
        self.__number2 = None
        self.__operation = None
        self.__current_number = ""
        self.__error = False

    def get_number1(self):
        return self.__number1

    def get_number2(self):
        return self.__number2

    def get_operation(self):
        return self.__operation

    def get_current_number(self):
        return self.__current_number

    def is_error(self):
        return self.__error

    def button_click(self, button):
        if self.__operation == None and self.__number1 != None:
            self.__number1 = None
        if len(self.__current_number) < 9:
            if self.__current_number == "0" or self.__current_number == "-0":
                self.__current_number = str(button)
            else:
                self.__current_number += str(button)

    def button_dot(self):
        if "." not in self.__current_number:
            if len(self.__current_number) > 0:
                self.__current_number += "."
            else:
                self.__current_number += "0."

    def __prepare_numbers(self):
        if self.__current_number != "":
            curr_num = round(float(self.__current_number), 8)
            self.__current_number = ""
            if curr_num % 1 == 0:
                curr_num = int(curr_num)

            if self.__number1 == None and curr_num != "":
                self.__number1 = curr_num
            elif self.__number2 == None and curr_num != "":
                self.__number2 = curr_num
            else:
                self.count()

        elif self.__current_number == "" and (
            self.__operation == None or self.__number1 == None
        ):
            # and self.__operation == None
            self.__number1 = 0

    def button_operation(self, __operation):

        self.__operation = __operation

        if (
            self.__operation == "%"
            or self.__operation == "x**2"
            or self.__operation == "2√"
        ):
            self.count()
        else:
            self.__prepare_numbers()

    def count(self):
        if self.__operation != None:
            self.__prepare_numbers()
            if self.__number1 == None:
                self.__number1 = 0
            if self.__number2 == None:
                self.__number2 = 0

            try:
                if self.__operation == "x**2":
                    self.__current_number = self.__number1**2
                elif self.__operation == "%":
                    self.__current_number = self.__number1 / 100
                elif self.__operation == "2√":
                    self.__current_number = self.__number1 ** (1 / 2)
                elif self.__operation == "+":
                    self.__current_number = self.__number1 + self.__number2
                elif self.__operation == "-":
                    self.__current_number = self.__number1 - self.__number2
                elif self.__operation == "x":
                    self.__current_number = self.__number1 * self.__number2
                elif self.__operation == "/":
                    self.__current_number = self.__number1 / self.__number2
                elif self.__operation == "mod":
                    self.__current_number = self.__number1 % self.__number2
                elif self.__operation == "**":
                    self.__current_number = self.__number1**self.__number2
                elif self.__operation == "√":
                    self.__current_number = self.__number2 ** (1 / self.__number1)
            except ZeroDivisionError:
                self.__error = True
            except Exception as e:
                print(e)

            self.__number1 = None
            self.__number2 = None
            self.__operation = None

            self.__prepare_numbers()

    def button_backspace(self):
        if len(self.__current_number) > 1:
            self.__current_number = self.__current_number[:-1]
        else:
            self.__current_number = ""

    def button_clear(self):
        self.__number1 = None
        self.__number2 = None
        self.__operation = None
        self.__current_number = ""
        self.__error = False

    def button_change(self):
        if (
            self.__operation == None
            and self.__current_number == ""
            and self.__number1 != None
        ):
            if self.__number1 == 0:
                self.__number1 = None
                self.__current_number = "-"
            else:
                self.__number1 = -self.__number1
        elif (
            len(self.__current_number) == 0
            or self.__current_number == 0
            or self.__current_number == "0"
        ):
            self.__current_number = "-"
        elif self.__current_number[0] == "-":
            self.__current_number = self.__current_number.replace("-", "")
        else:
            self.__current_number = "-" + self.__current_number

    def display_operator(self):
        display_string = ""
        if not self.__error:
            if self.__number1 != None:
                display_string += str(self.__number1) + " "

            if self.__operation != None:
                display_string += str(self.__operation) + " "

            if self.__number2 != None:
                display_string += str(self.__number2) + " "

            display_string += self.__current_number
            if len(display_string) <= 0 or (
                display_string.find(str(self.__operation)) == 0
                and len(list(find_all(display_string, str(self.__operation)))) <= 1
            ):
                display_string = "0 " + display_string
        else:
            display_string = "ERROR"

        return display_string.strip()
