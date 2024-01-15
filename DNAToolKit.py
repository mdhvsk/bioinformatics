
nucleotides = ["A", "C", "T", "G"]


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
