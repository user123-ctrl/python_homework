#!/usr/bin/env python

from util import read_input
from util import complement

input_file = read_input("./rosalind_data/rosalind_orf.txt")

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

DNA = ''.join(input_file[1:])
forward_complement = ""
reversed_dna = DNA[::-1]
reversed_complement = ""


for x in DNA:
    forward_complement += complement(x)

for x in reversed_dna:
    reversed_complement += complement(x)


def find_orfs(dna):
    orfs = []
    stop_codons = ['TAA', 'TAG', 'TGA']

    for i in range(3):
        for j in range (i, len(dna)-2, 3):
            if dna[j:j+3] == 'ATG':
                for k in range(j + 3, len(dna)-2, 3):
                    if dna [k:k+3] in stop_codons:
                        orfs.append(dna[j:k+3])
                        break
    return orfs

forwards = find_orfs(DNA)
backwards = find_orfs(reversed_complement)
orfs = forwards + backwards

def translate(sequence):
    protein_sequences = ""
    for start in range(0, len(sequence), 3):
        codon = sequence[start:start+3]
        aminoacid = DNA_CODON_TABLE[codon]
        if aminoacid == "Stop":
            continue
        protein_sequences += aminoacid
    return protein_sequences

output = []
for orf in orfs:
    protein = translate(orf)
    if protein not in output:
        output.append(protein)

for protein in output:
    print(protein)