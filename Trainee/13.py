"""
Напишите скрипт, который пишет в консоль "Hello, <имя> <фамилия>! Nice to see you here!"
На вход скрипт принимает имя и фамилию, которые в последствии и используются в скрипте.
"""

firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")

print("Hello, {} {}! Nice to see you here!".format(firstname, lastname))
