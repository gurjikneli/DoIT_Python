# შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0


# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას(id,name,age,grade,subject_name,mark) და თქვენ
# სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.
import os, csv


def func1(filename, student_data):
    student_data.sort(key=lambda x: x['id'])
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(student_data[0].keys())
        for student in student_data:
            writer.writerow(student.values())


# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის
# ინფორმაციის წაკითხვა ფაილიდან.
def func2(filename, student_data):
    w1, w2 = 10, 20
    lines = 66
    counter = 0
    print('-' * lines)
    headers = list(student_data[0].keys())
    student = input("Enter student's ID or 'all' to print students: ")
    print('\n')
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if student == "all":
                print(f"  {row[0]:<{w1}}{row[1]:<{w1}}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w2}}{row[5]}")
                print("=" * lines if counter == 0 else "-" * lines)
                counter += 1
            elif student == row[0]:
                print(
                    f"  {headers[0]:<{w1}}{headers[1]:<{w1}}{headers[2]:<{w1}}{headers[3]:<{w1}}{headers[4]:<{w2}}{headers[5]}")
                print("=" * lines)
                print(f"  {row[0]:<{w1}}{row[1]:<{w1}}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w2}}{row[5]}")
                print("-" * lines)


# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.
#
def func3(filename, student_data):
    mark_dict = {}
    count_dict = {}
    for student in student_data:
        mark_dict[student['subject_name']] = 0
        count_dict[student['subject_name']] = 0

    for k in mark_dict.keys():
        for student in student_data:
            if student['subject_name'] == k:
                mark_dict[k] += student['mark']
                count_dict[k] += 1
    print(mark_dict)
    print(count_dict)

    for k in mark_dict.keys():
        mark_dict[k] = round(mark_dict[k] / count_dict[k], 2)
    print(mark_dict)


# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი
# შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

def func4(filename, student_data):

    continue_update = True
    while continue_update:
        id = int(input("Enter student's ID: "))
        subject_name = input("Enter student's subject name: ")
        mark = int(input("Enter student's mark: "))
        grade = input("Enter student's grade: ")

        for student in student_data:
            if student['id'] == id:
                student['subject_name'] = subject_name
                student['mark'] = mark
                student['grade'] = grade

        another_student = input("Do you want to update another student's info 'y/n': ")
        if another_student == 'n':
            continue_update = False

    func1(filename, student_data)
    func2(filename, student_data)


# -------------------MAIN-------------------

student_data = [{'id': 32, 'name': 'Tom', 'age': 18, 'grade': 'A', 'subject_name': 'Math', 'mark': 92},
                {'id': 5, 'name': 'John', 'age': 20, 'grade': 'B', 'subject_name': 'Physics', 'mark': 86},
                {'id': 44, 'name': 'Amm', 'age': 19, 'grade': 'A', 'subject_name': 'Literature', 'mark': 95},
                {'id': 10, 'name': 'Mike', 'age': 21, 'grade': 'C', 'subject_name': 'Physics', 'mark': 78},
                {'id': 12, 'name': 'Mary', 'age': 20, 'grade': 'B', 'subject_name': 'Literature', 'mark': 82},
                {'id': 60, 'name': 'Connor', 'age': 19, 'grade': 'D', 'subject_name': 'Math', 'mark': 68},
                {'id': 50, 'name': 'Ilia', 'age': 21, 'grade': 'A', 'subject_name': 'Math', 'mark': 100},
                ]

path = "files"
filename = "students.txt"
os.makedirs(path, exist_ok=True)
filename = os.path.join(path, filename)

# func1(filename, student_data)
# func2(filename, student_data)
# func3(filename, student_data)
func4(filename, student_data)



