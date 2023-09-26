##
## Modulo lab for CS 150B.
##
## In this lab, you will get practice using while loops and modulos.
##
## @author YOUR_NAME
##         YOUR_EMAIL (i really dont want to put irl info)
## @version 202102

# step 1
# Only add your one line of code, do not change anything else
def factorial(num1):
    total = 1
    while (num1>0):
        total = total * num1
        num1 -= 1
    return total

# step 2
def moduloPractice(num1):
    total = num1 % 9
    return total # TODO
   
# step 3
def evenNum(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    return num1 # TODO

# step 4
def oddNum(num1):
    if num1 % 2 == 1:
        return True
    else:
        return False
    return num1 # TODO

# step 5
def checkNum(num1):
    if (evenNum(num1)):
        return 'even'
    else:
        return 'odd'
    return 'none' # TODO

def run():
    num1 = int(input())
    print("Factorial:",factorial(num1))
    print("Modulo:",moduloPractice(num1))
    print("Even:",evenNum(num1))
    print("Odd:",oddNum(num1))
    print("Even or Odd:",checkNum(num1))

if __name__ == '__main__':
    print()
    run()
