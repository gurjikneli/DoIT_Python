# ================= საშინაო დავალება 4 ===================

# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

st = input("Enter a string: ")
st = st.encode()
print(st)


# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.

# მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"

st1 = input("Enter a string: ")
st1 = st1.strip().lower() + ' Python'
if "python" in st1:
    st1 = st1[0:st1.index('python')] + 'P' + st1[st1.index('python')+1:]
print(st1)


# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

st1 = input("Enter a string: ")
st2 = st1[0:(len(st1)//2)]
print(st2)


# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.

import string

latin_letters = string.ascii_letters
digits = string.digits
forbidden_symbols = '!~#$'

contains_latin_letters = False
contains_digits = False
contains_forbidden_symbols = False

st = input("Enter a string: ")

for char in st:
    if char in latin_letters:
        contains_latin_letters = True
    if char in digits:
        contains_digits = True
    if char in forbidden_symbols:
        contains_forbidden_symbols = True

if contains_latin_letters and contains_digits and not contains_forbidden_symbols:
    print('This is valid string')
else:
    print('This is not valid string')


# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

st = input("Enter a string: ")
st1 = st.encode()
print(st1)
st2 = st1.decode()
print(st2)


