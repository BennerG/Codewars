# Provided Instructions:
# In DNA strings, symbols "A" and "T" are complements
# of each other, as "C" and "G". You have function with
# one side of the DNA (string, except for Haskell); you
# need to get the other complementary side. DNA strand
# is never empty or there is no DNA at all (again, 
# except for Haskell).

# clear
def DNA_strand1(dna):
    answer = ""
    for base in dna:
        if base == 'A':
            answer += 'T'
        elif base == 'T':
            answer += 'A'
        elif base == 'G':
            answer += 'C'
        else: # base == 'C'
            answer += 'G'
    return answer

# succinct
def DNA_strand2(dna):
    bases = {'A':'T','T':'A','C':'G','G':'C'}
    return "".join(bases[base] for base in dna)

# pythonista
def DNA_strand(dna):
    return dna.translate("".maketrans("ACTG","TGAC"))

print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))