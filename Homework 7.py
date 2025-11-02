# ================= საშინაო დავალება 7 ===================

# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).

sequence = input('Enter a sequence seperated by comma: ')
unique_set = set(sequence.split(','))
print(unique_set)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი
# იქნება (frozenset).

sequence = input('Enter a sequence seperated by comma: ')
unique_set = frozenset(sequence.split(','))
print(unique_set)

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).

set_1 = {60,50,6,7,80,9}
set_2 = {64,55,6,7,40,92}
print(tuple(set_1.union(set_2)))

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით
# (list).

a = eval(input('Enter a sequence seperated by comma: '))
# a = '21, 51, 65, 45, 48, 36, 8, 45, 36, 21'
print(list(set(a)))


# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:

# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

lst = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for i in lst:
    print(f'Name: {i[0]}, Age: {i[1]}')


# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.


lst_1 = ["Irakli", "Giorgi", "Nona", "Oto"]
lst_2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

print(set(lst_1).intersection(set(lst_2)))

