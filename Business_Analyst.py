# -*- coding: utf-8 -*-
"""

Business Analyst Python test in 30 minutes time limit

"""

# Question 1
def HighestKey(dictionary):
    ''' 
    takes a dictionnary as an input and return a list of the
    three keys with the highest values.

    Input : dictionnary with length greather than 3 (keys ; ‘str’, values : ‘float’) 
    Output : list
    '''
    # required library
    from collections import Counter 
    # counter
    k = Counter(dictionary) 
    # Finding 3 highest values 
    high = k.most_common(3) 
    return high

# test cases
    
dictionary = {'A': 67, 'A': 67, 'C': 45,  
           'D': 56, 'E': 12, 'F': 69} 

HighestKey(dictionary)

# Question 2
def sum_digits(n):
    """
    Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    # convert to a list of digits
    digits = [int(element) for element in str(n)]
    # return the sum of digits
    return sum(digits)

print(sum_digits(10))
print(sum_digits(4224))
print(sum_digits(1234567890))

# Question 3
def date_conversion_robust(date_string):
    """
    Converts date string from slash format to dash format.
    Checks if input date is valid; if not, prints an error and returns None.
    Valid dates are as follows:
        - European date ordering (day-month-year).
        - Two-digit years are in the past century (1918-2017 is "past century", 2018- is not...).
        - The year of the date is in either range 00 - 99 or 1000 - 9999
    
    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/17
        (DO NOT assume every input is a valid date)
    
    
    Returns:
    if input was valid: string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1917
    if input was not valid: print out "Not a valid date.", return None
    Example use:
    >>> print(date_conversion_robust('19/8/16'))
    19-08-2016
    >>> print(date_conversion_robust('1/12/1898'))
    01-12-1898
    >>> print(date_conversion_robust('16/3/18'))
    16-03-1918
    >>> print(date_conversion_robust('29/2/2017'))
    Not a valid date.
    None
    >>> print(date_conversion_robust('131/2/1928'))
    Not a valid date.
    None
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    
    """
    # empty list container
    date = []
    
    try: 
        # split the date_string
        day, month, year = date_string.split('/')
        
        # day conversion
        if len(day) <= 1 and int(day) <= 9:
            day = '0' + day
        # excpetion threshold for day
        elif len(day) < 0 or len(day) >= 3 or int(day) > 31:
            raise Exception("Not a valid date.")
            
    # month converstion
        if len(month) == 1 and int(month) <= 9:
            month = '0' + month
        # excpetion threshold for month
        elif len(month) < 0 or len(month) >= 3 or int(month) > 12:
            raise Exception("Not a valid date.")
    # year conversion
        if len(year) == 2 and int(year) <= 17:
            year = '20' + year
        elif len(year) == 2 and int(year) > 17:
            year = '19' + year
        
        # excpetion threshold for year
        elif len(year) <= 1 or len(year) > 4 or (99 < int(year) < 1000):
            raise Exception("Not a valid date.")
            
        # feb exception
        elif int(month) == 2 and int(day) > 28:
            raise Exception("Not a valid date.")
        
        # append all the elements in the list container
        date.append(day)
        date.append(month)
        date.append(year)
        
        # join the result together
        result = '-'.join(date)
        # return result
        return result
    
    except:
        print('Not a valid date.')
    
# my test cases
print(date_conversion_robust('19/8/16'))
print(date_conversion_robust('1/12/1898'))   
print(date_conversion_robust('16/3/18'))

print(date_conversion_robust('29/2/2017'))
print(date_conversion_robust('131/2/1928'))
print(date_conversion_robust(2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    













