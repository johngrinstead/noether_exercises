def is_two(x):
    '''
    This function takes in an argument and determines if the argument is the string or integer for the number 2
    '''
    return x == 2 or x == '2' or x == 'two'


##--------------------------------------------------------------------------------------------##

def is_vowel(x):
    '''
    This function takes an argument and evaluates it to determine if it is a vowel letter
    '''
    return x.lower() in ('a', 'e', 'i', 'o', 'u')


##--------------------------------------------------------------------------------------------##

def is_consonant(x):
    '''
    This function takes and argument and evaluates it to determine if it is not a vowel
    '''
    return is_vowel(x) == False


##--------------------------------------------------------------------------------------------##

def capitalize_consonant(x):
    '''
    This function takes an argument and determines if the first character is not a vowel, if it is not it will capitalize the first letter
    '''
    if is_consonant(x[0]) == True:
        return x.capitalize()
    else:
        return x
    
##--------------------------------------------------------------------------------------------##

def calculate_tip(tip_percent, bill_total):
    '''
    This function takes in 2 arguments:
        - The tip percent as a decimal fraction
        - The total of the bill
    Then it will return the value of what the tip should be 
    '''
    tip = bill_total * tip_percent
    return tip


##--------------------------------------------------------------------------------------------##

def apply_discount(original_price, discount_percent):
    '''
    This function takes in 2 arguments:
        - The original price of an item
        - The discounted percent as a whole number 
    Then it will output the new price of the item after calculating the discount 
    '''
    discount = original_price * (discount_percent / 100)
    new_price = original_price - discount
    return new_price
    
##--------------------------------------------------------------------------------------------##

def handle_commas(x):
    '''
    This function will take in an argument and if any of the characters are commas it will remove them, then return the value as an integer data type 
    '''
    return int(x.replace(',', ''))


##--------------------------------------------------------------------------------------------##

def get_letter_grade(grade):
    '''
    This function will take in an argument that is a number grade, then will return the corresponding letter grade
    '''
    if grade > 90:
        return('A')
    elif grade > 80:
        return('B')
    elif grade > 70:
        return('C')
    elif grade > 60:
        return('D')
    else:
        return('F')
    
    
##--------------------------------------------------------------------------------------------##

def remove_vowels(x):
    '''
    This functions will take an argument in the form of a word, then return the same work with no vowels
    '''
    word = ''
    for letter in x:
        if is_consonant(letter) == True:
            word += letter
    return word


##--------------------------------------------------------------------------------------------##

def normalize_name(name):
    '''
    This function will take an argument in the form of a word, it will then normalize the string by:
        - Remove white space from beginning and end of the string
        - Replace any blank spaces between characters with an underscore 
        - Remove any character that is not a letter
        - Return the string with all lowercase letters 
    '''
    name = name.strip()
    name = name.replace(' ', '_')
    normal_name = ''
    for character in name:
        if character.isalpha() == True or character =='_':
            normal_name+=character
    return normal_name.lower()

##--------------------------------------------------------------------------------------------##

def cumulative_sum(numbers):
    '''
    This function takes an argument in the form of a list of integers, then will return a new list after performing a cumulative sum calculation on each subsequent number
    '''
    # Establish a new list
    newlist = []
    # Establish a variable to count through the index
    i = 1
    # Loop through the list
    for num in numbers:
        # Calculate the next number in the list 
        cumulative = sum(numbers[:i])
        # Add the next number to the new list 
        newlist.append(cumulative)
        # Move on to the next item on the list 
        i += 1
    return newlist