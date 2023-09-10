class Father:
    def __init__(self, attr1):
        self.attr1 = attr1

    def method1(self):
        return f"Метод Parent1: {self.attr1}"


class Mother:
    def __init__(self, attr2):
        self.attr2 = attr2

    def method2(self):
        return f"Метод Parent2: {self.attr2}"


class ComplexChild(Father, Mother):
    def __init__(self, attr1, attr2, attr3):
        Father.__init__(self, attr1)
        Mother.__init__(self, attr2)
        self.attr3 = attr3

    def method3(self):
        return f"Метод ComplexChild: {self.attr3}"


child = ComplexChild("Сила", "Любов", "Комбінезон")

# Виклик методів для об'єкта
print(child.method1())
print(child.method2())
print(child.method3())
# Від Нікіти
