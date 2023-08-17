
#This code is linked to the file named "Account_Transactions_Project_Plan". Please open that file to get more sense of this code 
#I used pandas because it is great and easy tool for reading CSV files

import pandas as pd


#numpy will enable me to calculate cummulative sum later
import numpy as np

#The next line of code reads the CSV file (Note: I have to insert the CSV file in the same directory as my IDE so that my IDE can locate the CSV file)
read_CSV = pd.read_csv(r'Final_Intern-Account_Transactions.csv')

#This input enable the user to search for a particular customer using the customer ID
customer_id = input("Enter the Customer ID: ")


if customer_id == 'C231':
    #if the user picks a customer with ID number C231, the next line of code only reads the "Amount" session from column 2 to 31 in the CSV file.
    location = read_CSV.loc[0:29, ["Amount"]]

    #List is easier to use than data frame - This next line of code convert dataframe data into a list of data
    list_location = location.values.tolist()

    #Using import numpy, the next code calculates the cumulative sum (used for calculating the ending balance).
    #Note: The output of the cumulative sum is a list
    cumulative_sum = np.cumsum(list_location)

    #This prints out the minimum balance from the cumulative sum
    print(f"Minimum Balance of Customer with ID number {customer_id} is {min(cumulative_sum)}")

    #This prints out the maximum balance from the cumulative sum
    print(f"Maximum Balance of Customer with ID number {customer_id} is {max(cumulative_sum)}")

    #This prints out the ending balance (Note: The ending balance is typically the last item in the cumulative sum list
    print(f"Ending Balance of Customer with ID number {customer_id} is {cumulative_sum[-1]}")

elif customer_id == 'C865':

    #else if the user picks a customer with ID number C865, the next line of code only reads the "Amount" session from column 33 to 62 in the CSV file.
    location = read_CSV.loc[31:60, ["Amount"]]
    list_location = location.values.tolist()


    cumulative_sum = np.cumsum(list_location)


    print(f"Minimum Balance of Customer with ID number {customer_id} is {min(cumulative_sum)}")

    print(f"Maximum Balance of Customer with ID number {customer_id} is {max(cumulative_sum)}")

    print(f"Ending Balance of Customer with ID number {customer_id} is {cumulative_sum[-1]}")

elif customer_id == 'C409':

    #if the user picks a customer with ID number C409, the next line of code only reads the "Amount" session from column 64 to 93 in the CSV file.
    location = read_CSV.loc[62:91, ["Amount"]]

    list_location = location.values.tolist()


    cumulative_sum = np.cumsum(list_location)


    print(f"Minimum Balance of Customer with ID number {customer_id} is {min(cumulative_sum)}")

    print(f"Maximum Balance of Customer with ID number {customer_id} is {max(cumulative_sum)}")

    print(f"Ending Balance of Customer with ID number {customer_id} is {cumulative_sum[-1]}")

else:
    #This raises an error if the user input a customer ID that is not located in the CSV file
    raise ValueError("Sorry, no such Customer Id exist")
