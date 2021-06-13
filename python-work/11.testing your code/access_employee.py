from employee import Employee



print("Testing the Employee class, enter 'q' to quit qntime/")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break
    salary = input("Enter the employee's salary: ")
    salary = int(salary)
    
    emp = Employee(first, last, salary)
    emp.display_names()
    emp.display_salary()
    choice= input("Do you want to give a raise to the employee?(y/n)")
    if choice == 'y':
        print(emp.give_raise(5700))