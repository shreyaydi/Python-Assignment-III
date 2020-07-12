import os
import json
import platform
from academy import *

import os
import json
import platform
from academy import *


class Student:
    def __init__(self, name="", payment_left=20000):
        self.name = name
        self.payment_left = payment_left
        self.roll = academy.get_roll()
        self.course_complete = False

    def payment(self, deposit):
        self.payment_left -= deposit

    def get_info(self):
        return {"name": self.name, "payment_left": self.payment_left, "roll": self.roll,
                "course_complete": self.course_complete}

    def update_name(self, new_name):
        self.name = new_name

    def clear_payment(self):
        self.payment_left = 0

    def set_student(self, student_info):
        self.name = student_info["name"]
        self.roll = student_info["roll"]
        self.payment_left = student_info["payment_left"]
        self.course_complete = student_info["course_complete"]


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


academy = Academy()

clear_screen()
print('Select what you want to do. \n1) Signup \n2) Login')
startChoice = int(input('Enter your Choice: '))
if startChoice == 1:
    clear_screen()
    print("Signup\n\n")
    name = input("Enter your name: ")
    student = Student(name)

elif startChoice == 2:
    clear_screen()
    print("Login\n\n")
    roll = int(input("Enter your roll: "))
    student = Student()
    student.set_student(academy.get_student_from_roll(roll))

while True:
    clear_screen()
    print("Hello ", student.name)
    print("Select what you want to do: \n1) Inquire Courses \n2) Register \n3) Display payment information \n4) "
          "Update information \n5) Leave program \n6) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_screen()
        academy.inquiry_course()
        input()
    elif choice == 2:
        clear_screen()
        print("Choose payment option: \n1) Rs20000 \n2) Rs10000")
        payment_choice = int(input("Enter your Choice: "))
        if payment_choice == 1:
            student.payment(20000)
        elif payment_choice == 2:
            student.payment(10000)
        academy.register_student(student)
        input()
    elif choice == 3:
        clear_screen()
        print(student.get_info())
        input()
    elif choice == 4:
        clear_screen()
        print("Choose update option: \n1) Update Name \n2) Pay left Fees")
        update_choice = int(input("Enter your Choice: "))
        if update_choice == 1:
            new_name = input("Enter your new name: ")
            student.update_name(new_name)
        elif update_choice == 2:
            if student.get_info()["payment_left"] == 0:
                print('You do not have any payment left')
            else:
                print('10000 dollar paid')
                student.clear_payment()
        print('Your account has been updated.')
        input()
        academy.update_student(student.get_info())
    elif choice == 5:
        academy.remove_student(student.get_info())
        if student.course_complete:
            print('Your deposit amount (Rs. 20000) will be returned.')
        else:
            print(
                'Your have not completed the course so deposit amount (Rs. 20000) will not be returned.')
        input()
    elif choice == 6:
        break


class Student:
    def __init__(self, name="", payment_left=20000):
        self.name = name
        self.payment_left = payment_left
        self.roll = academy.get_roll()
        self.course_complete = False

    def payment(self, deposit):
        self.payment_left -= deposit

    def get_info(self):
        return {"name": self.name, "payment_left": self.payment_left, "roll": self.roll,
                "course_complete": self.course_complete}

    def update_name(self, new_name):
        self.name = new_name

    def clear_payment(self):
        self.payment_left = 0

    def set_student(self, student_info):
        self.name = student_info["name"]
        self.roll = student_info["roll"]
        self.payment_left = student_info["payment_left"]
        self.course_complete = student_info["course_complete"]


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


academy = Academy()

clear_screen()
print('Select what you want to do \n1) LogIn \n2) SignUp')
startChoice = int(input('Enter your Choice: '))
if startChoice == 1:
    clear_screen()
    print("LOGIN\n\n")
    name = input("Enter your name: ")
    student = Student(name)

elif startChoice == 2:
    clear_screen()
    print("SignUp\n\n")
    roll = int(input("Enter your roll: "))
    student = Student()
    student.set_student(academy.get_student_from_roll(roll))

while (True):
    clear_screen()
    print("Hello ", student.name)
    print("Select what you want to do: \n1) Inquire Coueses \n2) Registeer \n3) Display payment information \n4) "
          "Update information \n5) Leave program \n6) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_screen()
        academy.inquiry_course()
        input()
    elif choice == 2:
        clear_screen()
        print("Choose payment option: \n1) Rs20000 \n2) Rs10000")
        payment_choice = int(input("Enter your Choice: "))
        if payment_choice == 1:
            student.payment(20000)
        elif payment_choice == 2:
            student.payment(10000)
        academy.register_student(student)
        input()
    elif choice == 3:
        clear_screen()
        print(student.get_info())
        input()
    elif choice == 4:
        clear_screen()
        print("Choose update option: \n1) Update Name \n2) Pay left Fees")
        update_choice = int(input("Enter your Choice: "))
        if update_choice == 1:
            new_name = input("Enter your new name: ")
            student.update_name(new_name)
        elif update_choice == 2:
            if student.get_info()["payment_left"] == 0:
                print('You do not have any payment left')
            else:
                print('10000 dollar paid')
                student.clear_payment()
        print('Your account has been updated')
        input()
        academy.update_student(student.get_info())
    elif choice == 5:
        academy.remove_student(student.get_info())
        if student.course_complete:
            print('Your deposit amount (Rs. 20000) will be returned')
        else:
            print('Your have not completed the course so deposit amount (Rs. 20000) will not be returned')
        input()
    elif choice == 6:
        break
