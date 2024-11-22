#!/usr/bin/env python

from util import read_input

input_file = read_input("./rosalind_data/rosalind_subs.txt")
string = input_file[0] #reading only the the first part of the string
substring = input_file[1] #reading only the second part of the string

position_of_occurence = [] #positions of the substring in string

for i in range(len(string)): # we search on the whole length of string
    if string[i:i + len(substring)] == substring: #if string position i + lengh of substring = substring then we have an occurence
        position_of_occurence.append(i+1) # add this occurence to the positions list with +1 because we started counting at 0 not 1 (which we have to)

print (*position_of_occurence) #the * removes the comma between the numbers and gives me numbers with spaces inbetween
               
        

