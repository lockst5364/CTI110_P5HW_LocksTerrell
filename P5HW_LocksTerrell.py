#P5HW - Math Quiz
#December 7, 2023
#CTI-110 P5HW - Math Quiz
#Terrell Locks
#

import random

def display():
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()

def create_rando():
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    return random1, random2

def subtract():
    i = 1
    random1, random2 = create_rando()
    answer = random1 - random2
    while user_ent != answer:
        if random1 < random2:
            user_ent = int(input(f"{random1}\n'+'\n{random2}\nEnter answer: "))
            answer_ent = int(input('Sorry, guess is too low.\nTry again: '))
        else:
            print('Sorry, guess is too high')
            answer = int(input('Try again'))
            i +=1
            print('Congratulations!!!!! Your answer is correct.')
            print(f"Number of guesses: {i}")

def add():
    i = 1
    random1, random2 = create_rando()
    answer = random1 + random2
    user_ans = int(input(f"{random1}\n'+'\n{random2}\nEnter answer: "))
    while user_ans != answer:
        if user_ans < answer:
            user_ans = random1 - random2
            answer = int(input('Sorry, guess is too high.\nTry again: '))
        else:
            answer = int(input('Sorry, guess is too low.\nTry again: '))
            print('Congratulations!!!!! You answer is correct.')
            i +=1
            print(f"Number of guesses: {i}")

def function():
    print("Welcome to Math Quiz!")
    while True:
        display()
        option = input("\nPlease choose one of the menu options: ")
        if option == '1':
            add()
        elif option == '2':
                subtract()
        elif option == '3':
                print('Thank you for playing...')
                print()
                print('Bye')
                break
        else:
                    print()
                    print('Error: Invalid choice. Please choose again.')
    



if __name__ == "__main__":
    function()
