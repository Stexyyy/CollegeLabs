##
## Astonomy lab for CS 150B.
##
## In this lab, you will be using string formating and writing basic methods
##
##
## @author YOUR_NAME
##         YOUR_EMAIL
## @version 202010

# STEP 1 - CALCULATEINCOME
# Review: Calculate salary  - pay period based on
# parameters passed in   - takes int monthly salary, and multiplier  -  just returns value (no  print)
def calculate_income(rate, period):
    return rate*period


# STEP 2 - FORMATNAME
# Format Name -  takes in first and last name and  returns it as Last, First Name
def format_name(firstname, lastname):
    return f'{lastname}, {firstname}'



# STEP 3 - EMPLOYEEINFO
# Employee Info with Salary - Uses Format Name, Uses Calculate Salary, also includes department and email
def employee_info(firstname, lastname, department, email, rate, period):
    return f'{format_name(firstname, lastname)}\n${calculate_income(rate, period)}\n{department}\n{email}'





def main():
    '''
    Write your own tests here!! :)
    '''
    #example tests
    print(calculate_income(100000,4))
    print(format_name('Bill','Nye'))
    print(employee_info('Nicolaus', 'Copernicus','Astonomy Lab', 'copernicus@astonomylab.edu',123456,1))


if __name__ == "__main__":
    main()
