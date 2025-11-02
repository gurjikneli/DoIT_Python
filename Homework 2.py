# საშინაო დავალება 2

# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს
# თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

num = int(input("Enter a number: "))
if num in num_list:
    print("The number in list")
else:
    print("The number not in list")

# ===========================

# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ
# ტექსტი 'even' თუ კენტია 'odd'.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# ===========================

# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი
# "Same object", წინააღმდეგ შემთხვევაში "Different object"

str1 = 'String'
str2 = 'String'

if str1 is str2:
    print('Same object')
else:
    print('Different object')

# ===========================

# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:

# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი
# "More than list elements";

# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";

# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

num = int(input("Enter a number: "))

if num > num_list[2] and num < num_list[-1]:
    print('More than list elements')
elif num == num_list[5]:
    print('Equal')
else:
    print('None of the conditions were met')

# ===========================
