class Apprentice:
    aCount = 0 # class var
    def __init__(self, name, site):
        self.name = name  # instance vars
        self.site = site
        self._tasks = ['task 1', 'task 2'] # protected
        Apprentice.aCount += 1

    def displayApprentice(self):
        print(f'{self.name}, working on site {self.site} has {len(self._tasks)} tasks to complete')

    def addTask(self, task):
        self._tasks.append(task)

class SeniorApprentice(Apprentice):
    def __init__(self, name, site, supervisees):
        super().__init__(name, site)
        self._supervisees = [supervisees]

    def displayApprentice(self):
        super().displayApprentice()
        supervisees_str = ', '.join(self._supervisees)
        print(supervisees_str)

a = Apprentice('emma', 'dublin site')
a.displayApprentice()

b = SeniorApprentice('emma', 'dublin site', 'supervisor 1')
b.displayApprentice()
