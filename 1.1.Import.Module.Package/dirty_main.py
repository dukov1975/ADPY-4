from salary2.people import get_employees as all_emp
from salary2.salary import *

def main():
    for employe in all_emp():
        calculate_salary(employe)


if __name__ == '__main__':
    main()