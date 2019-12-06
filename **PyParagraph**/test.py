#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re


# In[2]:


resource_path = "./Resources"
extension = ".txt"


# In[3]:


def text(file):
    file_text = ""
    with open(file, "r") as io:
        file_text = io.read()
    io.close()
    return file_text


# In[4]:


def word_count(txt):
    words = re.split("[-\s]",txt)
    return len(words)


# In[5]:


def letter_count(txt):
    letters = re.findall("[a-zA-Z]",txt)
    return len(letters)


# In[6]:


def sentence_count(txt):
    sentences = re.split("[.?!]+",txt)
    sentences.pop()
    return len(sentences)


# In[7]:


def report_text(txt):
    lcount = letter_count(txt)
    wcount = word_count(txt)
    scount = sentence_count(txt)
    print("Paragraph Analysis")
    print("-"*20)
    print(f"Approx. Word Count: {wcount}")
    print(f"Approx. Sentence Count: {scount}")
    print(f"Average Word Length (letters): {format(lcount/wcount, '.1f')}")
    print(f"Average Sentence Length (words): {format(wcount/scount, '.1f')}")


# In[8]:


validFile = False
txt = ""
while not validFile:
    file_name = input("Please enter the name of a resource file (eg. paragraph_1)")
    file = os.path.join(resource_path, file_name + extension)
    try:
        with open(file,"r") as io:
            txt = io.read()
        io.close()
    except:
        txt = ""
        print("File not found: Please check file name and try again.")
    else:
        validFile = True
    


# In[9]:


report_text(txt)


# In[ ]:




