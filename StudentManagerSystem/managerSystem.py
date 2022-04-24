from student import *


class StudentManager(object):
    def __init__(self):
        # the list used to store data
        self.student_list = []

    # 一、程序入口函数，启动程序后执行的函数
    def run(self):
        # 1. 加载学员信息
        self.load_student()
        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3. 用户输入功能符号
            menu_num = int(input('Please input the function number: '))
            # 4. 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    # 二、系统功能函数
    # 2.1 显示功能菜单，打印序号的功能对应关系 -- 静态方法
    @staticmethod
    def show_menu():
        print("Please select the following functions: ")
        print("1. add student")
        print("2. delete student")
        print("3. modify student information")
        print("4. search student information")
        print("5. show all student information")
        print("6. save student information")
        print("7. exit system")

    # 2.2 添加学员
    def add_student(self):
        # print("Add student")
        stu_id = input("Please input student ID: ")
        name = input("Please input student name: ")
        gender = input("Please input student gender: ")
        tel = input("Please input student tel: ")
        unique = True
        for i in self.student_list:
            if i.id == stu_id:
                unique = False
                break
        if unique:
            student = Student(stu_id, name, gender, tel)
            self.student_list.append(student)
            # print(self.student_list)
            print("Successfully added this student")
        else:
            print("This student ID has been exist")

        # print(student)

    # 2.3 删除学员
    def del_student(self):
        # print("Delete student")
        del_id = input("Please input the student ID that you wanna delete: ")
        for i in self.student_list:
            if i.id == del_id:
                self.student_list.remove(i)
                break
        else:
            print("Not found")

    # 2.4 修改学员信息
    def modify_student(self):
        # print("Modify student information")
        modify_id = input("Please input the student ID that you wanna modify: ")
        for i in self.student_list:
            if i.id == modify_id:
                i.name = input("name: ")
                i.gender = input("gender: ")
                i.tel = input("telephone: ")
                print(
                    f'Successfully modified student information, ID: {i.id} name: {i.name}, gender: {i.gender}, telephone: {i.tel}')
                break
        else:
            print("Not found")

    # 2.5 查询学员信息
    def search_student(self):
        # print("Search student information")
        search_id = input("Please input the student ID you wanna search: ")
        for i in self.student_list:
            if i.id == search_id:
                print(f'ID: {i.id}, name: {i.name}, gender: {i.gender}, telephone: {i.tel}')
                break
        else:
            print("Not found")

    # 2.6 显示所有学员信息
    def show_student(self):
        # print("Show all students information")
        print("ID\tname\tgender\ttelephone")
        for i in self.student_list:
            print(f'{i.id}\t{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        # print("Save student information")
        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()

    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['id'], i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()
