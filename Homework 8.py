# ================= საშინაო დავალება 8 ===================

# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def fibonacci(n):
    lst = [0,1]
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    else:
        for i in range(2, n):
            lst.append(lst[i - 1] + lst[i - 2])

    return lst

number = int(input("Enter a number: "))
print(fibonacci(number))


# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით).
# მაგ.: race და care ანაგრამებია.


def anagram(str1, str2):
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())
    return str1 == str2

str1 = "race"
str2 = "care"

print(anagram(str1, str2))

# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

number = int(input("Enter a number: "))
print(factorial(number))

# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს
# სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.

def func1(string1, symbol):
    lst = str1.split(symbol)
    print(lst)
    return len(lst) - 1

str1 = "rarcerrterrmr"
sym = 'r'
print(func1(str1, sym))




