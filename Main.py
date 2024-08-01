import datetime
import salary
import people

def main():
    time_now = datetime.datetime.now()
    print(f'Current time now: {time_now}')

    salary_info = salary.calculate_salary()
    print(f'Salary info: {salary_info}')

    employees_info = people.get_employees()
    print(f'People info: {employees_info}')

if __name__=="__main__":
    main()