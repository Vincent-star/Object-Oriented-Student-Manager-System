class Student(object):
    def __init__(self, stu_id, name, gender, tel):
        self.id = stu_id
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.id}, {self.name}, {self.gender}, {self.tel}'
