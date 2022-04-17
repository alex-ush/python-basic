class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._incom.values())


driver = Position('Mike', 'Smith', 'Driver', 3500, 750)
print(driver.get_full_name())
print(driver.position)
print(driver.get_total_income())
