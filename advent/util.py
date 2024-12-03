# a library of utility functions for Rosalind exercises

#reads out a file and puts the content in a list with one line
def read_input(filepath): 
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

#complements a Nucleotide 
def complement(x):
    if x == "A":
        return "T"
    elif x == "T":
        return "A"
    elif x == "G":
        return "C"
    elif x == "C":
        return "G"
    else:
        return None
    
#calculate gc content for a dna, returns id and gc content as a dictionary
def calculate_gc_content(dna):
    counts = {
     'A': 0,
     'T': 0,
     'C': 0,
     'G': 0,
 }
    for base in dna:
         counts[base] += 1
         gc = (counts['G'] + counts['C']) / len(dna) * 100
         return gc
