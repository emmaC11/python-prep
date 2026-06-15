class Package:
    menu =  {
        'flight':{'economy':149,'business':500},
        'accommodation':{'5-star':250,'4-star':210, '3-star':175}, 
        'events':{'diving':100,'walking':15, 'climbing':40}
     } # class var
    
    def __init__(self, name):
        self.name = name # instance var
        self._items = {'flight':"economy", 'accommodation':"5-star", 'nights':14, 'events':['diving', 'walking']} # protected instance variable

    def getCost(self):
        total = 0

        if self._items['flight']:
            total += Package.menu['flight'][self._items['flight']]

        if self._items['accommodation']:
            total += Package.menu['accommodation'][self._items['accommodation']] * self._items['nights']

        if self._items['events']:
            for x in self._items['events']:
                total += Package.menu['events'][x]

        print(total)
        return total

    def addEvent(self, event):
        self._items['events'].append(event)

class weekPackage(Package):
    def __init__(self, name, discount):
        super().__init__(name)
        self.discount = discount

    def getCost(self):
        base = super().getCost()
        full_weeks = self._items['nights'] // 7
        print(base - (full_weeks * self.discount))



# p = Package('emma')
# p.getCost()

wp = weekPackage('emma', 50)
wp.getCost()
        