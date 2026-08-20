import json

def main():
    add_expenses = add_expenses()
    save_expenses = save_expenses(add_expenses)

def add_expenses():
    while True:
        name_of_full_expense = input('What would you like to name the full expense? ').title().strip()
        if name_of_full_expense == '':
            continue
        else:
            name_of_full_expense = Tracker()
            break
    while True:
        name = input("What is the expense's name? ").strip().title()
        if name == '':
             continue
        else:
            break
    while True:
        try:
            cost = f'{float(input("What is the expense's cost? ")):.2f}'
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
    
    return name_of_full_expense.add_expense(name, cost, description)

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
        return self.full_expsense

            
