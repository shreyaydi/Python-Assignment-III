import json


class Academy:
    def __init__(self):
        self.courses = [
            'Introduction to programming',
            'Getting started',
            'Basics of programming',
            'Fundamentals of programming',
            'Introduction to loops',
            'File and error handling']
        try:
            with open("students.txt", "r") as file:
                self.students = json.load(file)
            file.close()
        except:
            self.students = []

    def inquiry_course(self):
        print("Courses are: ")
        for course in self.courses:
            print(course)

    def get_student_from_roll(self, roll):
        for i in range(len(self.students)):
            if roll == self.students[i]['roll']:
                return self.students[i]
        print('Roll no error!')

    def register_student(self, student):
        for i in range(len(self.students)):
            if student.roll == self.students[i]['roll']:
                print("You have already registered. Thank you!")
                return
        self.students.append(student.get_info())
        with open("students.txt", "w") as file:
            json.dump(self.students, file)
        print(self.students)
        file.close()

    def get_roll(self):
        if len(self.students) == 0:
            return 1
        else:
            return self.students[-1]['roll'] + 1

    def remove_student(self, student):
        for i in range(len(self.students)):
            if student["roll"] == self.students[i]["roll"]:
                self.students.pop(i)
                with open("students.txt", "w") as file:
                    json.dump(self.students, file)
                print('Thank you for staying with us for this long.')
                file.close()
                return
        print('You are not registered!')

    def update_student(self, student):
        for i in range(len(self.students)):
            if student['roll'] == self.students[i]['roll']:
                self.students[i] = student

                with open("students.txt", "w") as file:
                    json.dump(self.students, file)
                file.close()

                return
        print('Register before update.')
        return
