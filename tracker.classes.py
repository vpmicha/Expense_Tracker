import json

def main():
    add_expensesV = add_expenses()
    save_expensesV = save_expenses(add_expensesV)

def add_expenses():
    while True:
        name_of_full_expense = input('What would you like to name the full expense? ').title().strip()
        if name_of_full_expense == '':
            continue
        else:
            tracker = Tracker()
            break
    while True:
        name = input("What is the expense's name? ").strip().title()
        if name == '':
             continue
        else:
            break
    while True:
        try:
            cost = round(float(input("What is the expense's cost? ")), 2)
            if cost == '':
                continue
            else:
                break
        except (ValueError, KeyError):
            continue        
    while True:
        description = input("What is the expense's description? ").strip()
        if len(description) > 60:
            print('Description must be smaller in size.(Less than 60 characters)')
            continue
        else:
            break
    
    return {name_of_full_expense: tracker.add_expense(name, cost, description)}

def save_expenses(expenses):
    try:
        with open('Expenses.json', 'a') as file:
            json.dump(expenses, file)
    except (OSError, KeyError):
        print('Sorry! Programm could not save your expenses.')

    


class Tracker():
    def __init__(self):
        self.full_expsense = {}
    
    def add_expense(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description
        self.full_expsense['Name'] = name
        self.full_expsense['Cost'] = cost
        self.full_expsense['Description'] = description

        return self.full_expsense

    def remove_expense(self):
            del self.full_expsense

    def __str__(self):
        return str(self.full_expsense)

            
