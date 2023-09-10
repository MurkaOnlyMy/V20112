import random


class Cipher:
    def __init__(self, value):
        self.value = value
        self._encrypted_value = self._encrypt()

    def _encrypt(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            return self.value + random.randint(1, 10)
        elif operation == "-":
            return self.value - random.randint(1, 10)
        elif operation == "*":
            return self.value * random.randint(1, 10)
        elif operation == "/":
            divisor = random.randint(1, 10)
            return self.value / divisor

    def __str__(self):
        return f"Введене число: {self.value}, Зашифроване число: {self._encrypted_value}"


# Введене число, яке ми хочемо зашифрувати
input_number = 12

# Створення об'єкта класу Cipher
cipher = Cipher(input_number)

# Виведення результату
print(cipher)
# Від Нікіти
