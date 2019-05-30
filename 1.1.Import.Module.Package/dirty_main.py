from salary2.people import *
from salary2.salary import *

def main():
    for employe in get_employees():
        calculate_salary(employe)


if __name__ == '__main__':
    main()