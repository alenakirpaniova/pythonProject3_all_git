# Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome(s):
    return s[::-1] == s

while True:
    s = input("Enter a palindrome: ")
    print(f"{s} is palindrome!" if palindrome(s) else "not a palindrome")

