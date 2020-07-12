# Provided Instructions:
# In DNA strings, symbols "A" and "T" are complements
# of each other, as "C" and "G". You have function with
# one side of the DNA (string, except for Haskell); you
# need to get the other complementary side. DNA strand
# is never empty or there is no DNA at all (again, 
# except for Haskell).

def DNA_strand(dna):
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

print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))