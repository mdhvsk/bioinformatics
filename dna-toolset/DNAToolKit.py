from structures import *


def validateSeq(dna_seq):
    tempSeq = dna_seq.upper()
    for nuc in tempSeq:
        if nuc not in nucleotides:
            return False
    return tempSeq


def countNucFrequency(dna_seq):
    freqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna_seq:
        freqDict[nuc] += 1
    return freqDict


def transcription(dna_seq):
    """DNA -> RNA transcription. Replacing Thymine with Uracil"""
    return dna_seq.replace("T", "U")


def reverse_complement(dna_seq):
    """swapping guamine with cytosine and adenine with thymine, then reversing the string"""
    return ''.join([DNA_complement[nuc] for nuc in dna_seq])[::-1]


def gc_content(seq):
    """G-C Content of DNA/RNA"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subset(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subset = seq[i: i + k]
        res.append(gc_content(subset))
    return res
