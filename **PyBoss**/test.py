#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[2]:


file = "./Resources/employee_data.csv"


# In[4]:


table = []
with open(file, "r") as io:
    file_text = io.read()
    rows = file_text.split("\n")
    for row in rows:
        data = row.split(",")
        if len(data) == 5:
            table.append(data)


# In[6]:


header = table.pop(0)


# In[24]:


new_table = []
new_table.append(["ID", "First Name", "Last Name", "DOB", "SSN", "State"])
for row in table:
    new_row = []
    
    new_row.append(row[0])
    
    name = row[1].split(" ")
    new_row += name
    
    DOB = row[2]
    new_DOB = "/".join(DOB.split("-"))
    new_row.append(new_DOB)
    
    SSN = row[3]
    new_SSN = f"***-**-{SSN[-4:]}"
    new_row.append(new_SSN)
    
    state = row[4]
    new_state =us_state_abbrev[state]
    new_row.append(new_state)
    
    new_table.append(new_row)


# In[25]:


for i in range(10):
    print(new_table[i])


# In[26]:


new_rows = []
for row in new_table:
    new_rows.append(",".join(row))
results_string = "\n".join(new_rows)
with open("results.csv", "w") as results:
    results.write(results_string)


# In[ ]:




