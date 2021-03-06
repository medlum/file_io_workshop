####### Question 1 #######
# Read the opening and closing prices data from `dbs_data_1.csv` 
# and `dbs_data_2.csv` in the current folder. 
# Compute the average opening price and average closing price after
# reading the data. 
# When the program is executed, it will print the following statement:
# "Average opening and closing price of DBS shares:  $xx.x, $xx.x"

####### Solution for Question 1 #######

# import Path function from pathlib module
from pathlib import Path
# import csv module
import csv

# create a path object to current working directory
# as the csv files are located in the same folder as file_io.py.
fp_read = Path.cwd()

# create 2 global variables to store opening and closing prices.
open = []
close = []

# iterate over the path object using a for loop
# glob("*.csv") method is used to search any files with csv extension
for file in fp_read.glob("*.csv"):
    # in each loop:
    ## 1. open each csv file in read mode
    with file.open(mode="r", encoding="UTF") as dbs_shares:
        ## 2. create a reader object using reader() method from csv module
        reader = csv.reader(dbs_shares)
        ## 3. use next() function to skip header in first row
        next(reader)
        ## 4. iterate over the reader object to read data in each row
        for row in reader:
            ## 5. append opening price in index position 1 
            open.append(float(row[1]))
            ## 6. append closing price in index position 2
            close.append(float(row[2]))

# compute average opening and closing price
# round the values to 1 decimal place 
# create 2 global variables for the computed prices.
avg_open = round(sum(open)/len(open),1)
avg_close =  round(sum(close)/len(close),1)

# create a global variable to store the statement
statement = "Average opening and closing price of DBS shares: "

# print using f-string with the variables.
print(f"{statement} ${avg_open}, ${avg_close}")


####### Question 2 #######
# Write the average opening and closing prices of DBS shares 
# from Question 1 to a text file.
# Name the text file as "dbs_avg_price.txt"


####### Solution for Question 2 #######
# create a path object with file name: "dbs_avg_price.txt"
# in the current working directory.
fp_write = Path.cwd()/"dbs_avg_price.txt"
# create the file "dbs_avg_price.txt" in 
# current working directory using touch() method
fp_write.touch()

# open text file in write mode
with fp_write.open(mode = "w", encoding="UTF-8") as text_file:
    # write prices to text file
    text_file.write(f"{statement} ${avg_open}, ${avg_close}")
