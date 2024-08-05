import datetime
from salary.salary import calculate_salary
from people.people import get_employees

def main():
    time_now = datetime.datetime.now()
    print(f'Current time now: {time_now}')

    salary_info = calculate_salary()
    print(f'Salary info: {salary_info}')

    employees_info = get_employees()
    print(f'People info: {employees_info}')

if __name__=="__main__":
    main()
