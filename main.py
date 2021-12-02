from art import arter
from data import morse_code_data



print(f"{arter}\n")

# the of the morse code
MORSE_CODE = morse_code_data


def get_key(val):
    '''
    Takes the value from the dictionary and returns key
    '''
    for key, value in MORSE_CODE.items():
        if val == value:
            return key

    return "key doesn't exist"
is_on="y"
while is_on=="y":
    # method we perfrom
    method= input("Encode or Decode (e/d)? ")
    user_input=input("Enter your Message: ").upper()

    end=""
    if method =="e":
        for letter in user_input:
            if letter == " ":
                end+=" "
            else:
                end += f"{MORSE_CODE[letter]}"
                end += " "
        print(end)
    elif method=="d":
        user_input = user_input.split(" ")
        for letter in user_input:
            if letter == "":
                end+=" "
            else:
                end+=f"{get_key(letter)}"
        print(end.capitalize())

    elif method =="x":
        is_on=="x"





