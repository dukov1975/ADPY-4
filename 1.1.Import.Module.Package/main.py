from application.salary import calculate_salary
from db.people import get_employees



def main():
    for employe in get_employees():
        calculate_salary(employe)


if __name__ == '__main__':
    main()