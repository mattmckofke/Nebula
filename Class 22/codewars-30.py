def DNA_strand(dna):
    compliment = ""
    for char in dna:
        match char:
            case "A":
                compliment += "T"
            
            case "T":
                compliment += "A"
                
            case "C":
                compliment += "G"
                
            case "G":
                compliment += "C"
        
    return compliment

print(DNA_strand("ATTGC"))

def DNA_strand2(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))

print(DNA_strand2("ATTGC"))