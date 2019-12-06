#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing dependency
import os


# In[2]:


file = "./Resources/election_data.csv"


# In[6]:


poll_data = []


# In[7]:


with open(file, "r") as io:
    filetext = io.read()
    rows = filetext.split("\n")
    for row in rows:
        poll_data.append(row.split(","))
    


# In[11]:


header = poll_data.pop(0)


# In[12]:


print(header)


# In[16]:


def print_head(ls, num = 5):
    for i in range(num):
        print(ls[i])


# In[17]:


index = len(poll_data) -1
while index >= 0:
    if len(poll_data[index])!=3:
        poll_data.pop(index)
    index -= 1


# In[65]:


candidates = []
vote_counts = []
for row in poll_data:
    voter_id = row[0]
    county = row[1]
    candidate = row[2]
    
    try:
        i = candidates.index(candidate)
        vote_counts[i] += 1
    except:
        candidates.append(candidate)
        vote_counts.append(1)
        


# In[66]:


total_votes = sum(vote_counts)


# In[67]:


percentages = []
for count in vote_counts:
    percentage = format(100*count/total_votes, ".3f")
    percentages.append(percentage)


# In[68]:


running_arg_max = 0
running_max = vote_counts[0]
for i,v in enumerate(vote_counts):
    if running_max < v:
        running_max = v
        runnin_arg_max = i
winner = candidates[running_arg_max]
print(winner)


# In[69]:


report_string = "Election Results \n"
report_string += f"{'-'*20}\n"f"Total Votes: {total_votes}\n"f"{'-'*20}"
for i, v in enumerate(candidates):
    report_string += f"\n{v}: {percentages[i]}% ({vote_counts[i]})"
report_string += f"\n{'-'*20}"f"\nWinner: {winner}"f"\n{'-'*20}"


# In[70]:


print(report_string)


# In[ ]:




