class Tracker():
    def __init__(self):
        self.full_expsense = {}
    
    def add_expense(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

        #---------------------Get the expense's name---------------------#
        while True:
            try:
                name = input("What is the expense's name? ").strip().title()
                if name == '':
                    continue
                else:
                    self.full_expsense['Name'] = name
                    break
            except KeyError:
                continue

        #---------------------Get the expense's cost---------------------#
        while True:
            try:
                cost = f'{float(input("What is the expense's cost? ")):2f}'
                if cost == '':
                    continue
                else:
                    self.full_expsense['Cost'] = cost
                    break
            except (ValueError, KeyError):
                continue        

        #---------------------Get the expense's description---------------------#
        while True:
            description = input("What is the expense's description? ").strip()
            if len(description) > 60:
                print('Description must be smaller in size.(Less than 60 characters)')
                continue
            else:
                self.full_expsense['Description'] = description
                break

        return self.full_expsense

    def remove_expense(self):
            del self.full_expsense

    def __str__(self):
        return self.full_expsense

    

            
