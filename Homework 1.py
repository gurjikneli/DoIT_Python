# საშინაო დავალება 1

# 1. კონსოლიდან შეიტანეთ ორი რიცხვი და დაბეჭდეთ ყველა არითმეტიკული ოპერაცია (მიმატება, გამოკლება, გამრავლება,
# ჩვეულებრივი გაყოფა, მთელზე გაყოფა, ნაშთის აღება, ახარისხება).

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print(f'მიმატება = {number1 + number2}')
print(f'გამოკლება = {number1 - number2}')
print(f'გამრავლება = {number1 * number2}')
print(f'გაყოფა = {number1 / number2}')
print(f'მთელზე გაყოფა = {number1 // number2}')
print(f'ნაშთის აღება = {number1 % number2}')
print(f'ახარისხება = {number1 ** number2}')


# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

diagonal_1 = float(input("Enter first diagonal: "))
diagonal_2 = float(input("Enter Second diagonal: "))

area = (diagonal_1 * diagonal_2) / 2
print(area)

# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში,
# მილიმეტრებში, მილში.

meters = float(input("Enter meters: "))

print(meters * 100)
print(meters * 10)
print(meters * 1000)
print(meters * 0.00062)

# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და
# ფუძის მნიშვნელობა.

base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))

area = (base * height) / 2
print(area)

# 5. კონსოლიდან შეიტანეთ ორნიშნა რიცხვი და დაბეჭდეთ ციფრთა ჯამი.

number1 = int(input("Enter Number: "))

zero_digit = number1 % 10
decimal_digit = int(number1 / 10)

print(decimal_digit + zero_digit)

