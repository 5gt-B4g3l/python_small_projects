#Biomolecular sequencing program
#goal is to calculate GC content, G & C correlated with DNA stability

#initial fragment of DNA
insulin = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC"

#compute length
l = len(insulin)
print("The lenghth is:", l)

#compute # of C and G
numC = insulin.count('C')
numG = insulin.count('G')
print('number of C nucleotides:', numC)
print('Number og G nucleotides:', numG)

#compute GC content:
gc = (numC + numG) / l
#convert to percentage by multiplying by 100:
gcPercent = gc * 100
print('GC content is:', gcPercent)

