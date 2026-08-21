import json
from sum_List_largest_number import add_contents, largest_number
import sys

def main():
#In the end of each variable V is short for Variable and L is short for List.
    not_saved_expensesL = []
    name_of_full_expenseL = []
    try:
        past_expenses = load_expenses()
        while True:
                if past_expenses and past_expenses != 'No past expense':
                    if input('Do you want to see your expenses?(Y:Yes/N:No) ').strip().lower() == 'y':
                        print(load_expenses())
                        break
                    break
                break
        while True:
            ask = input('Do you want to add or remove an expense? ').strip().lower()
            if ask == 'add':
                while True:
                    name_of_full_expense, not_saved_expenses = add_expenses()
                    name_of_full_expenseL.append(name_of_full_expense)
                    not_saved_expensesL.append(not_saved_expenses)                   
                    more_addition = input('Do you want to add more?(Y:Yes/N:No) ').strip().lower()
                    if more_addition == 'y':
                        continue
                    elif more_addition == 'n':
                        save_expenses(not_saved_expensesL, name_of_full_expenseL)                        
                        break
                    break   
                past_expenses = load_expenses()                 
            elif ask == 'remove':
                while True:
                    removeE = input('What expense do you want to remove? ').strip().title()
                    remove_expenses(removeE)
                    more_removal = input('Do you want to remove more?(Y:Yes/N:No) ').strip().lower()
                    if more_removal == 'y':
                        continue
                    elif more_removal == 'n':
                        break
                    break
                past_expenses = load_expenses()
            else:
                continue

            try:
                if past_expenses and past_expenses != 'No past expense':
                    while True:
                        total_expenses = input('Do you want to see your total expenses?(Y:Yes/N:No) ').strip().lower()
                        if total_expenses == 'y':
                            print(total_spending(past_expenses)[0])
                            break
                        elif total_expenses == 'n':
                            break
                    while True:
                        biggest_spend = input('Do you want to see your largest expense?(Y:Yes/N:No) ').strip().lower()
                        if biggest_spend == 'y':
                            total_spendingL = total_spending(past_expenses)[1]
                            for key, value in past_expenses.items():
                                if value['Cost'] == largest_expense(total_spendingL):
                                    print(f'{key}: ${largest_expense(total_spendingL)}')
                                    break
                            break
                        elif biggest_spend == 'n':      
                            break
                elif past_expenses == 'No past expense' or past_expenses == {}:
                    print('You have no past expenses to see!')

            except (KeyError, ValueError, IndexError, TypeError, OSError):
                print('Something went wrong while loading your past expenses')
    except (KeyboardInterrupt, EOFError):
        sys.exit()

def add_expenses():
    while True:
        name_of_full_expense = input('What would you like to name the full expense? ').strip().title()
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
            if cost <= 0:
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
    
    return [name_of_full_expense, tracker.add_expense(name, cost, description)]

def remove_expenses(expenses):
    try:
        with open('Expenses.json', 'r') as file:
            data = json.load(file)
            del data[expenses]
        with open('Expenses.json', 'w') as file:
            json.dump(data, file)
    except (json.JSONDecodeError, OSError, FileNotFoundError, KeyError):
        return 'You have no expenses to remove!'
    return data

def save_expenses(not_saved_expensesL, name_of_full_expenseL):
    try:
        with open('Expenses.json', 'r') as file:
            data = json.load(file)
            for expense, expense_name in zip(not_saved_expensesL, name_of_full_expenseL):
                data[expense_name] = expense

        with open('Expenses.json', 'w') as file:
            json.dump(data, file)
            not_saved_expensesL.clear()
            name_of_full_expenseL.clear()
    except (KeyError, FileNotFoundError, json.JSONDecodeError):
        data = {}
        with open('Expenses.json', 'w') as file:
            for expense, expense_name in zip(not_saved_expensesL, name_of_full_expenseL):
                data[expense_name] = expense
            json.dump(data, file)
            not_saved_expensesL.clear()
            name_of_full_expenseL.clear()
    except OSError:
        print('Sorry, programm could not save your expenses!')

def total_spending(past_expenses):
    total_spendingL = []
    try:
        for expense_cost in past_expenses:
            total_spendingL.append(past_expenses[expense_cost]['Cost'])
    except (KeyError, ValueError, OSError, json.JSONDecodeError):
        print('You do not have expenses')
    return [add_contents(total_spendingL), total_spendingL]

def largest_expense(total_spendingL):
    return largest_number(total_spendingL)

def load_expenses():
    try:
        with open('Expenses.json', 'r') as file:
            return json.load(file)
    
    except (OSError, FileNotFoundError, json.JSONDecodeError):
        return 'No past expense'


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
    
if __name__ == '__main__':
    main()