# A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

filepath = "./rosalind_ini5.txt"

with open(filepath, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())

for l in lines[1::2]:
    print(l.strip())