from DNAToolKit import *
import random
from structures import *
from utilities import colored

rndDNA = ''.join([random.choice(nucleotides) for nuc in range(50)])

print(colored(rndDNA))
print(validateSeq(rndDNA))
print(countNucFrequency(rndDNA))
print(transcription(rndDNA))
print(reverse_complement(rndDNA))
print(gc_content(rndDNA))
print(gc_content_subset(rndDNA, k=5))
