#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Dictionaries
from typing import Dict

dict_complement: Dict[str, str] = dict(A="T", T="A", G="C", C="G", a="t", t="a", g="c", c="g")


dict_transcibe = {'A': "A", 'T': "U", 'G': "G", 'C': "C", 'a': "a", 't': "u", 'g': "g", 'c': "c"} 


# In[59]:


#Right alphabet checking
def alph_check(input_seq):
    count_letter = len(input_seq)
    while count_letter != 0:
        for letter in input_seq:
            if letter in ["A","C","G","a","c", "g"]:
                count_letter -= 1
            elif letter in ["T", "t"] and "u" not in input_seq and "U" not in input_seq:
                count_letter -= 1
            elif letter in ["U", "u"] and "t" not in input_seq and "T" not in input_seq:
                count_letter -= 1
            else: 
                return False
    return True

#DNA sequence checking
def DNA_check(input_seq):
    count_letter = len(input_seq)
    while count_letter != 0:
        for letter in input_seq:
            if letter in dict.keys(dict_complement):
                count_letter -= 1
            else: 
                return False
    return True


# In[62]:


#The body of programm   
command = input("Enter command:")

while True:
    if command == "exit":
        print('Good luck!')
        break
        
    elif command == "reverse":
        input_seq = input("Enter sequence:")
        if alph_check(input_seq):
            print(input_seq[::-1])
            command = input("Enter command:")
        else:
            print("Invalid alphabet. Try again!")
        
    elif command == "transcribe":
        input_seq = input("Enter sequence:")
        if DNA_check(input_seq):
            output=''
            for letter in input_seq:
                output += dict_transcibe[letter]
            print(output)
            command = input("Enter command:")
        else:
            print("Invalid alphabet. Try again!")
        
    elif command == "complement":
        input_seq = input("Enter sequence:")
        if DNA_check(input_seq):
            output=''
            for letter in input_seq:
                output += dict_complement[letter]
            print(output)
            command = input("Enter command:")
        else:
            print("Invalid alphabet. Try again!")
        
    elif command == "reverse complement":
        input_seq = input("Enter sequence:")
        if DNA_check(input_seq):
            output=''
            for letter in input_seq[::-1]:
                output += dict_complement[letter]
            print(output)
            command = input("Enter command:")
        else:
            print("Invalid alphabet. Try again!")
        
    else:
        print("I don't understand what do you want")
        command = input("Enter command:")

