# set up dictionary
phone_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

# get user input
phone_input = input('phone number ')

# set up variable to store result
result = ''

# loop through user input
for i in phone_input:
    
    # find matching key and log value to result
    result += phone_dict.get(i , '!') + " "
print(result + ' ')
