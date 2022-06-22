
####### Question 1 #######
# Write a program in the current working directory to extract
# the opening and closing prices data of `dbs_data_1.csv` and `dbs_data_2.csv`.
# After extracting the opening and closing price, the program will compute
# the average opening price and average closing price.
# When the program is executed, it will print the following:
# "Average opening and closing price of DBS shares:  $12.5, $12.3"

# import Path function from pathlib module
from pathlib import Path
# import csv module
import csv

# create a path object to current working directory
# as both csv files are located there.
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
        ## 2. create a reader object using reader() method in csv module
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
# round to 1 decimal place 
# create 2 global variables and assign them with the computed price.
avg_open = round(sum(open)/len(open),1)
avg_close =  round(sum(close)/len(close),1)
# create a global variable to store the statement
statement = "Average opening and closing price of DBS shares: "

# print using f-strings with the variables.
print(f"{statement} ${avg_open}, ${avg_close}")


