import mysql.connector
import datetime


class Student:

    def __init__(self, hostname, db, user, password):

        self.host = hostname
        self.db_name = db
        self.user_name = user
        self.password = password

    def connect(self):
        try:
            conn = mysql.connector.connect(host=self.host, database=self.db_name, user=self.user_name,
                                           password=self.password)
        except mysql.connector.Error as error:
            print(error)
        return conn

    def resultSet(self, query, args):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, args)
            result = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)
        conn.close()
        return result

    def prepareStatement(self, query, args):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        conn.close()

    def create_db(self):  # создает таблицы
        students = 'CREATE TABLE ' \
                   'student(id INT NOT NULL, ' \
                   'name VARCHAR(100) NOT NULL, ' \
                   'gpa DECIMAL(10,2) NULL, ' \
                   'birth DATETIME NULL)'
        courses = 'CREATE TABLE ' \
                  'course(id INT NOT NULL, ' \
                  'name VARCHAR(100) NOT NULL)'
        self.prepareStatement(students, '')
        self.prepareStatement(courses, '')

    def get_students(self, course_id):  # возвращает студентов определенного курса
        return self.resultSet(('SELECT ax.id, ax.name, ax.gpa, ax.birth, bx.name '
                               'FROM student ax JOIN course bx on(ax.id = bx.id and bx.id=%s)'),
                              [course_id])

    def add_students(self, course_id, students):  # создает студентов и
        # записывает их на курс
        args = list()
        args.append(course_id)
        args.append(students['name'])
        args.append(students['gpa'])
        args.append(students['birth'])
        insert_student = ('INSERT INTO student (id, name, gpa, birth) '
                          'VALUES (%s,%s,%s,%s)')
        self.prepareStatement(insert_student, args)

    def add_student(self, student):  # просто создает студента
        args = list()
        args.append(student['name'])
        args.append(student['gpa'])
        args.append(student['birth'])
        insert_student = ('INSERT INTO student (id, name, gpa, birth) VALUES (0,%s,%s,%s)')
        self.prepareStatement(insert_student, args)

    def get_student(self, student_id):  # Получить студента по ID
        return self.resultSet(('SELECT id, name, gpa, birth '
                               'FROM student WHERE id=%s'),
                              [student_id])

    def add_course(self, args):  # Добавляем курс
        insert_course = ('INSERT INTO course (id, name) VALUES (%s,%s)')
        self.prepareStatement(insert_course, args)

    def update_student(self, args):  # Привязываем курс к студенту
        update_student = ('UPDATE student SET id=%s WHERE name =%s')
        self.prepareStatement(update_student, args)


def main():
    student = Student('000.00.00.00', 'q', 'r', '75_')
    student.create_db()
    student.add_course([0, 'Не зачислен'])
    student.add_course([1, 'Основы Python'])
    student.add_course([2, 'Продвинутый курс Python'])
    student.add_course([3, 'Python Django'])
    student.add_students(0, dict(name='Дюков Дмитрий', gpa=0, birth=datetime.datetime.now()))
    student.add_students(0, dict(name='Кузимасов Михаил', gpa=0, birth='1975-06-05 00:00'))
    student.add_students(0, dict(name='Долбоящуров Степан', gpa=0, birth=datetime.datetime.now()))
    student.add_student(dict(name='Кондовый Роман', gpa=0, birth=datetime.datetime.now()))
    student.add_student(dict(name='Мозансон Елена', gpa=0, birth=datetime.datetime.now()))
    student.add_student(dict(name='Критинин Павел', gpa=0, birth=datetime.datetime.now()))
    student.update_student([2, 'Дюков Дмитрий'])
    student.update_student([1, 'Кузимасов Михаил'])
    student.update_student([1, 'Долбоящуров Степан'])
    student.update_student([2, 'Кондовый Роман'])
    student.update_student([3, 'Мозансон Елена'])
    student.update_student([3, 'Критинин Павел'])
    print(student.get_students(1))
    print(student.get_students(2))
    print(student.get_students(3))

    print(student.get_student(0))  # В этом методе смысл не понятен,
    # к ID мы пивязываем курс, у студента
    # нет в таблице уникального и автоинкрементного ID
    # в любом случае получится множество


if __name__ == '__main__':
    main()
