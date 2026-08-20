from math import inf

def add_contents(list):
    try:  
        total = 0
        for i in list:
            total += i
        return total
    except (TypeError, ValueError, IndexError):
        return 'List contained a non number character'
        

def largest_number(list):
    largest_number = -inf
    try:
        if len(list):
            for i in list:
                if i > largest_number:
                    largest_number = i
        else:
            largest_number = None

        return largest_number
    except TypeError:
        return 'List contained a non number character'
