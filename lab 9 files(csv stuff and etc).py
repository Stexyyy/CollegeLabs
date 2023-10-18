##
## Files and CSV lab for CS 150B.
##
## In this lab, you will get practice opening files and using the data in those files
##
## @author YOUR_NAME
##         YOUR_EMAIL
## @version 202102

import csv  ## remove comment before import when starting step 3


# Step 1
def file_addition(filename):
     with open(filename, 'r') as yeah:
         num1 = yeah.readline()
         num2 = yeah.readline()
         
         return int(num1) + int(num2)
         



# Step 2
def line_counter(filename):
    with open(filename, 'r') as nah:
        uh = nah.readlines()
        
        return len(uh)


# Step 3
def csv_data(filename):
    count = 0
    max_row_length = 0
    with open(filename, 'r') as myfile:
        csv_reader = csv.reader(myfile) #remember import csv at the top of the file
        for row in csv_reader:
            count+=1
            if len(row) > max_row_length:
                max_row_length = len(row)
        
    return count, max_row_length  # returns a tuple of the two values


# Step 4
def get_filtered_CSV(filename, filter_by):
    lst = []
    with open(filename, 'r') as aoao:
        csv_reader = csv.reader(aoao) #remember import csv at the top of the file
        for row in csv_reader:
            if row[0] == filter_by:
                lst.append(row)
        return lst


# Step 5
def find_flight(filename, airlines, city, earliest, latest):
    lst = get_filtered_CSV(filename, airlines)


# Add your own tests to this method
def run():
    print(file_addition("num.txt"))
    print(line_counter("harryPotter.txt"))
    print(csv_data("myfile.csv"))
    print(get_filtered_CSV("Airport.csv", "United"))
    print(find_flight("Airport.csv", "United", "Portland", "0000", "2400"))


if __name__ == '__main__':
    print()
    run()
