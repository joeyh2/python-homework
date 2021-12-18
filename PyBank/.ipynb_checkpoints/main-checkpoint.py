#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import the pathlib and csv library
from pathlib import Path
import csv


# In[6]:


# Set file path
csvpath = Path("Resources/budget_data.csv")


# In[7]:


# Initialize first variables to hold budget data
months = []
total_months = 0
net_profit_loss = 0
average_change_pl = []
greatest_inc_profit = ["", 0]
greatest_dec_profit = ["",999999999]

# Open input path as a file object
with open (csvpath, 'r') as csvfile:
    
    # Pass in csv file to csv.reader() function 
    # with ',' as delimiter
    csvreader =  csv.reader(csvfile, delimiter = ',')
    
    # Assign header
    header = next(csvreader)
    
    # Assign first row and update total_months and net_profit_loss (as integer) with first row values
    first_row = next(csvreader)
    total_months += 1
    net_profit_loss += int(first_row[1])
    
    # Set prev_value to first row's p/l data as integer
    prev_value = int(first_row[1])
    
    # Initialize for loop to iterate rows
    for row in csvreader:
        
        # Update total_months and net_profit_loss (as integer)
        total_months += 1
        net_profit_loss += int(row[1])
        
        # Create/update net_change variable and add each iterance to average_change_pl 
        net_change = int(row[1]) - prev_value
        average_change_pl.append(net_change)
        
        # Set prev_value to update to given row's p/l data as integer at end of each iterance
        prev_value = int(row[1])
        
        # Create conditional to update or retain date and p/l of greatest increase in profit
        if net_change > greatest_inc_profit[1]: 
            greatest_inc_profit[0] = row[0]
            greatest_inc_profit[1] = net_change
       
        # Create conditional that updates or retains date and p/l of greatest decrease in profit 
        if net_change < greatest_dec_profit[1]:
            greatest_dec_profit[0] = row[0]
            greatest_dec_profit[1] = net_change

# Calculate average in changes in profit/losses for entire period to 2 decimal places
average_change_pl = round(sum(average_change_pl) / len(average_change_pl), 2)

# Assign metrics to variable "results"
results = f'''Financial Analysis \n------------------\n 
Total Months: {total_months} \n 
Total: ${net_profit_loss} \n  
Average Change: ${average_change_pl} \n
Greatest Increase in Profits: {greatest_inc_profit[0]} (${greatest_inc_profit[1]}) \n
Greatest Decrease in Profits: {greatest_dec_profit[0]} (${greatest_dec_profit[1]})'''

# Display results in terminal
print(results)


# In[8]:


output_path = Path('PyBank.txt')
with open(output_path, 'w') as file:
    file.write(results)


# In[ ]:




