# ************** Chapter 10 solution *************************


class Calc:

    def __init__(self, num=0):
        self.num = num
        self.res = 0

    def add(self, num1):
        self.res = self.num + num1

    def mul(self, num2):
        self.res = self.num * num2

    def print_res(self):
        print(self.res)


class Calac2(Calc):
    pass
