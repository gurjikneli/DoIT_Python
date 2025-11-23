# =========== სტუდენტების მართვის სისტემა ==================

class Student:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
    # ეს ფუნქცია (__str__) მჭირდება საერთოდ?????????
    def __str__(self):
        return f"{self.name}, roll number: {self.roll_number}, grade: {self.grade}"



class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        try:
            self.students.append(student)
            print("\n***** NEW STUDENT ADDED SUCCESSFULLY! *****")
        except Exception as e:
            print("\n***** STUDENT ADDITION FAILED! *****")
            print(e)

    def list_students(self, color_list):
        if not self.students:
            print("\n***** NO STUDENTS AVAILABLE! *****")
            return
        print("\n***** ALL STUDENTS *****\n")
        format_output()
        count = 1
        for student in self.students:
                print(f"{color_list[0]}{student.name:<20}{student.roll_number:^10}{student.grade:^20}{color_list[1]}")
                if count < len(self.students):
                    print("-" * 45)
                    count += 1
        print("#" * 45)

    def search_by_roll_number(self, roll_number):
        found = [student for student in self.students if student.roll_number == roll_number]
        return found

    def update_student_grade(self, roll_number):
        grade = input("\nEnter the student grade: ")
        if grade.isalpha() and grade in ["A", "B", "C", "D", "E", "F"]:
            for student in self.students:
                if student.roll_number == roll_number:
                    student.grade = grade
            print("\n***** STUDENT'S GRADE UPDATED SUCCESSFULLY! *****\n")
        else:
            print("Please enter a valid grade! ('A', 'B', 'C', 'D', 'E', 'F')")




def get_valid_student():
    while True:
        roll_number = input("\nEnter the student roll number: ")
        if roll_number.isdigit() and 1 < int(roll_number) <= 100:
            return int(roll_number)
        else:
            print("Please enter a valid roll number!")


def format_output():
    print(f"{'NAME':<20}{'ROLL NUMBER':^12}{'GRADE':^15}")
    print("#" * 45)




def main():
    green = "\033[32m"
    reset = "\033[0m"
    color_list = [green, reset]

    manager = StudentManager()
    while True:
        print(f"{'\n' * 3}===== STUDENT MANAGEMENT PLATFORM =====\n")
        print("1. Add new student")
        print("2. Show all students")
        print("3. Search by roll number")
        print("4. Update student grade")
        print("5. Exit")
        print("=" * 40, '\n')
        choice = input("Please select an option: ")
        if choice == "1":
            name = input("\nEnter the student name: ").strip()
            roll_number = get_valid_student()
            grade = input("\nEnter the student grade: ").strip()
            student = Student(name, roll_number, grade)
            manager.add_student(student)

            # student_1 = Student(name="Peter Gibson", roll_number=47, grade="D")
            # student_2 = Student(name="Nicholas Smith", roll_number=27, grade="C")
            # student_3 = Student(name="Heather Johnson", roll_number=97, grade="A")
            # student_4 = Student(name="Joseph Smith", roll_number=94, grade="A")
            # student_5 = Student(name="Michelle Robertson", roll_number=55, grade="D")
            # manager = StudentManager()
            # for i in [student_1, student_2, student_3, student_4, student_5]:
            #     manager.add_student(i)

        elif choice == "2":
            manager.list_students(color_list)

        elif choice == "3":
            roll_number = get_valid_student()
            results = manager.search_by_roll_number(roll_number)
            if results:
                for student in results:
                    print("\n***** FOUND STUDENT *****:\n")
                    format_output()
                    print(f"{color_list[0]}{student.name:<20}{student.roll_number:^10}{student.grade:^20}{color_list[1]}")
            else:
                print("\n***** STUDENT NOT FOUND! *****")

        elif choice == "4":
            roll_number = get_valid_student()
            manager.update_student_grade(roll_number)

        elif choice == "5":
            print("\n***** THANKS FOR USING OUR PLATFORM! *****")
            break
        else:
            print(" Please enter the correct option (1–5)!")



if __name__ == "__main__":
    main()
