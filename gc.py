#!/usr/bin/env python

from util import read_input 

# if we had a dictionary of results, how would we pick the maximum GC%?

# if we had a FASTA file, how would we get id-sequencde pairs?
fasta = read_input('./rosalind_data/rosalind_gc.txt')

sequences = {}
current_id = ""
for line in fasta:
    if line[0] == ">":
        header = line
        # this is a header
        # we only care about this header from now on
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        sequence = line
        # it is a sequence
        sequences[current_id] = sequences[current_id] + sequence

#print(sequences)

# all that needs to be done is to calculate the GC% for every sequence


# if we had a sequence, how would we calculate the GC%?
# idea: calculate #Cs, #Gs, add up, divide by length of sequence, *100
# idea: we solved this problem before! see DNA.py --> paste solution

gc_values ={}

for id, dna in sequences.items():
     counts = {
     'A': 0,
     'T': 0,
     'C': 0,
     'G': 0,
 }
     for base in dna:
         counts[base] += 1
         gc = (counts['G'] + counts['C']) / len(dna) * 100
         gc_values[id] = gc

# # idea: loop over dictionary, see if current value is max

# # first define the placeholders for max value and corresponding id:
max_value = 0
max_id = ""

for seq_id, current_gc_value in gc_values.items():
     #print(f"current max value: {max_value} current max id: {max_id}")
     #print("input:", seq_id, current_gc_value)
     # is the maximum value smaller than the current value?
     if current_gc_value > max_value:
         # update the max_value:
         #print("input was greater than max!")
         max_value = current_gc_value
         max_id = seq_id
     #print(f"update: current max value: {max_value} current max id: {max_id}")
     #print("================")
print (max_id)
print ( max_value)