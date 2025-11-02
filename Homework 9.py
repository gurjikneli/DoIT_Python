# # ================= საშინაო დავალება 9 ===================
#
# # 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად
# # და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.
#
# def global_function(number):
#     int_list.append(number)
#     print(int_list)
#
# int_list = [10,20,30,40]
# global_function(98)
#
# # 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა
# # მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].
#
# def sum_of_numbers(*arr):
#     sum = 0
#     for number in arr:
#         sum += number
#     return sum
#
#
# array = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# result = sum_of_numbers(*array)
# print(result)
#
# # 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით
# # რაც გლობალურ ცვლადს აქვს  (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.
#
# def function():
#     gl_str = "Local"
#     return gl_str
#
# gl_str = "Global"
# print(function())
#
# # 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  ციფრების ჯამს
# # (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
#
# def sum_of_numbers(num):
#     if num < 10:
#         return num
#     else:
#         return int(str(num)[0]) + sum_of_numbers(int(str(num)[1:]))
#
# result = sum_of_numbers(12345)
# print(result)
#
# # 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ
# # (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)
#
# def reverse_function(str1):
#     if len(str1) == 1:
#         return str1
#     return str1[-1] + reverse_function(str1[:-1])
#
# print(reverse_function('Hello'))



# def fibonacci(num):
#     if num in (0, 1):
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
# n = 10
# result = fibonacci(n)
# print(result)
#
# for i in range(n + 1):
#     print(fibonacci(i), end=' ')



# def fibonacci2(n, f=[0, 1]):
#     if len(f) == n:
#         return f
#     f.append(f[-1] + f[-2])
#     return fibonacci2(n, f)
#
# num = 10
# result = fibonacci2(num + 1)
# print(result)



# def flatten(arg):
#     for item in arg:
#         if isinstance(item, (list, tuple, set, frozenset)):
#             yield from flatten(item)
#         elif isinstance(item, dict):
#             yield from flatten(item.values())
#         else:
#             yield item
#
# arr = [1, 2, (3, [[4, 5, 6], "Text", 7], 8), {'title': 'the wolf', 'pages': 256}, [9, 0], {15, True, 0}, frozenset({15, 23, 0.098})]
# arr = list(flatten(arr))
# print(arr)


# student_data_lst = [1, 'Tom', 24, 'A', 'Math', 92]
# student_data_lst.sort(key=lambda x: x[0])

student_data = [{'id': 32, 'name': 'Tom', 'age': 18, 'grade': 'A', 'subject_name': 'Math', 'mark': 92},
                {'id': 5, 'name': 'John', 'age': 20, 'grade': 'B', 'subject_name': 'Physics', 'mark': 86},
                {'id': 44, 'name': 'Ann', 'age': 19, 'grade': 'A', 'subject_name': 'Literature', 'mark': 95},
                {'id': 10, 'name': 'John', 'age': 21, 'grade': 'C', 'subject_name': 'Programming', 'mark': 78},
                {'id': 12, 'name': 'Mary', 'age': 20, 'grade': 'B', 'subject_name': 'Biology', 'mark': 82}
                ]

student_data.sort(key=lambda x: x['id'])
for student in student_data:
    print(student)
# print(student_data)
