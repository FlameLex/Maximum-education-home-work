s = 'Шалаш'
def is_palindrome(s):
    s = s.lower() #переводим в нижний регистр
    return s == s[::-1] #сравниваем строку с ее перевернутой версией
print(is_palindrome(s))
