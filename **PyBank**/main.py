#!/usr/bin/env python
# coding: utf-8

# In[46]:


#importing dependencies
import os
import csv


# In[3]:


#reference relative file path
file = "./Resources/budget_data.csv"


# In[34]:


table = []
with open(file, 'r') as csvfile:
    text = csvfile.read()

    rows = text.split("\n")

    for row in rows:
        table.append(row.split(","))


# In[34]:


csvfile.close


# In[35]:


header = table.pop(0)


# In[36]:


# In[42]:


#Removing invalid rows, changing datatype of profit column from string to integer
index = len(table) - 1
while index >= 0:
    if(len(table[index]) != 2):
        table.pop(index)
    else:
        table[index][1] = int(table[index][1])
    index-=1
    


# In[43]:



# In[64]:


total_profit = 0
running_max = table[1][1]-table[0][1]
running_min = table[1][1]-table[0][1]
running_arg_max = 1
running_arg_min = 1
month_count = len(table)
#looping over table to find max, min change, cumulative profit
for index, row in enumerate(table): 
    row_profit = row[1]
    total_profit += row_profit
    if index > 0:
        previous_profit = table[index-1][1]
        delta = row_profit-previous_profit
        if running_max < delta:
            running_max = delta
            running_arg_max = index
        if running_min > delta:
            running_min = delta
            running_arg_min = index
            
first_row = table[0]
final_row = table[month_count-1]

average_profit_change = format((final_row[1]-first_row[1])/(month_count-1), ".2f")


# In[72]:


#generating report based on calculated data
report_string = f"\nFinancial Analysis \n{'-'*20}\n"f"Total Months: {month_count}\n"f"Total Profit: {total_profit} \n"f"Average Change: {average_profit_change}\n"f"Greatest Increase in Profits: {table[running_arg_max][0]} (${running_max})\n"f"Greatest Decrease in Profits: {table[running_arg_min][0]} (${running_min})"


# In[73]:


#printing and writing report string to file
print(report_string)
with open("account_report.txt", "w") as report:
    report.write(report_string)
report.close()


# In[ ]:




