#!/usr/bin/env python

from util import read_input

fasta = read_input('./rosalind_data/rosalind_grph.txt')

sequences = {} #make a dictionary with id:sequence
current_id = ""
for line in fasta:
    if line[0] == ">": # could also be: if line.startswith(">"):
        header = line
        # this is a header
        # we only care about this header from now on
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        sequence = line
        # it is a sequence
        sequences[current_id] = sequences[current_id] + sequence


def overlap(sequences):
    output = []
    overlap_size = 3
    sequence_list = list(sequences.items()) #need a list for index

    for i in range(len(sequence_list)):
        for j in range(len(sequence_list)):
            id1, seq1 = sequence_list[i]
            id2, seq2 = sequence_list[j]

            if i == j: #dont compare with itself
                continue

            if seq1[-overlap_size:] == seq2[:overlap_size]:
                output.append((id1, id2))

    return output

output = overlap(sequences)
for id in output:
    print(id[0], id[1])