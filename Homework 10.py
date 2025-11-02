# # ================= საშინაო დავალება 10 ===================

# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით
# დააჯგუფეთ სიების ელემენტები.
#
# params: [1, 2, 3], ['a', 'b', 'c']
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def func(lst_num, lst_char):
    zipped = zip(lst_num, lst_char)
    return [str(i) for i in zipped]

lst_num = [1, 2, 3]
lst_char = ['a', 'b', 'c']
print(func(lst_num, lst_char))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში
# გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.
#
# params:[1, 2, 3, 4, 5]
# output: 120

from functools import reduce

def func2(numbers):
    try:
        return reduce(lambda x, y: x + y, numbers)
    except TypeError:
        return 'Parameter type is incorrect'


numbers = [5, 22, 10, 4, 98]
print(func2(numbers))



# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
#
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

numbers_list = [5, 22, 10, 4, 99, 7, 21]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_list))
print(odd_numbers)


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის
# ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია.
# გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
#
# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება
# რაღაც სიმბოლოებით...
#
# params: ['hello', 'world', 'coding', 'nod'], 'ing'
# outputs: ['coding']



def func3(string_list, str):
    try:
        return list(filter(lambda word: word.endswith(str), string_list))
    except TypeError as ex:
        print('Incorrect type', ex)
    except Exception as ex:
        print('ERROR', ex)


string_list = ['hello', 'world', 'coding', 'nod', 'ending', 'solving']
str = 'ing'

print(func3(string_list, str))


