import csv


class Academy:
    def display_course(self, filename):
        with open(filename, mode='r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for row in csvreader:
                if line_count == 0:

                    line_count += 1
                else:
                    print(f'Course: {row[0]} Fee: {row[1]} ')
                    line_count += 1
        print('Student Registration with Rs. 20000 (deposit). Students are allowed to pay in two installments with '
              'Rs. 10000 each.')

    def registration(self, filename):
        new_list = []
        with open(filename, mode='r') as file:
            csvreader = csv.reader(file, delimiter=',')
            Rows = list(csvreader)
            new_id = len(Rows) + 1
        with open(filename, mode='a+') as add:
            csvWriter = csv.writer(add)
            new_list.append(new_id)
            new_list.append((input('Name: ')))
            new_list.append(input('Interested Course: '))
            new_list.append(int(input('Payment: ')))
            new_list.append(2000 - new_list[-1])
            new_list.append(False)
            csvWriter.writerow(new_list)

    def display_info(self, filename):
        with open(filename, mode='r') as file:
            csvreader = csv.reader(file, delimiter=',')
            line_count = 0
            for row in csvreader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    print(f'ID: {row[0]} \tName: {row[1]}\tCourse: {row[2]}\tDeposit: {row[3]}\tDue: {row[4]}\tGraduated: {row[5]}')

    def individual_info(self,filename,sid):
        with open(filename, mode='r') as file:
            csvreader = csv.DictReader(file, delimiter=',')
            for row in csvreader:
                if int(row['id']) == sid:
                    print(f'ID: {row["id"]} \t Name: {row["name"]}\t Course: {row["course"]}'
                          f'\t Deposit: {row["deposit"]} \t  Due: {row["due"]}. ')


    def updater(self,filename, sid ):
        new_list = []
        with open(filename, mode='r') as file:
            csvreader = csv.reader(file, delimiter=',')
            lines = list(csvreader)
            for row in csvreader:
                if int(row['id']) == sid:
                    print("Choose update option: \n1) Update Name \n2) Pay left Fees")
                    choice = int(input("Enter your Choice: "))
                    if choice == 1:
                        new_name = input('Enter name')
                        lines[sid][1] = new_name
                    elif choice == 2:
                        amount = int(input('enter amount'))
                        lines[sid][2] += amount
                        lines[sid][3] -=amount
            writer = csv.writer(open(filename, 'w'))
            writer.writerows(lines)


















if __name__ == "__main__":
    operation = Academy()
    with open("courseInfo.csv", 'w', newline='') as courseInfo:
        fieldnames = ['Course', 'Amount']
        writer = csv.DictWriter(courseInfo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Course': 'Full Stack Web Developer ', 'Amount': 50000})
        writer.writerow({'Course': 'AR/VR', 'Amount': 45000})
        writer.writerow({'Course': 'AL/MI', 'Amount': 50000})
        writer.writerow({'Course': 'Android App Development', 'Amount': 40000})
        writer.writerow({'Course': 'CLoud Computing', 'Amount': 35000})
        writer.writerow({'Course': 'IOS App Development', 'Amount': 35000})

    with open('studentInfo.csv', 'w', newline='') as studentinfo:
        fieldnames = ['id', 'name', 'course', 'deposit', 'due', 'completion']
        writer = csv.DictWriter(studentinfo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {'id': 1, 'name': 'Shreya Baidya', 'course': 'Full Stack Web Developer', 'deposit': 1000, 'due': 1000,
             'completion': False})
        writer.writerow(
            {'id': 2, 'name': 'Sankalpa Pokhrel', 'course': 'Android App Development', 'deposit': 2000, 'due': 0,
             'completion': True})
        writer.writerow(
            {'id': 3, 'name': 'Ankit Shrestha', 'course': 'IOS App Development', 'deposit': 1000, 'due': 1000,
             'completion': False})
        writer.writerow({'id': 4, 'name': 'Shraddha Amatya', 'course': 'CLoud Computing', 'deposit': 1000, 'due': 1000,
                         'completion': False})
        writer.writerow(
            {'id': 5, 'name': 'Alisha Thakuri', 'course': 'AR/VR', 'deposit': 2000, 'due': 0, 'completion': False})

    operation.display_course('courseinfo.csv')
    # operation.registration('studentinfo.csv')
    operation.display_info('studentinfo.csv')
    operation.individual_info('studentinfo.csv',2)
    operation.updater('studentinfo.csv', 2)

