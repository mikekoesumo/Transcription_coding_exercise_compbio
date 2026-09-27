def find_orf(dna):
    start = dna.find("ATG")

    if start == -1:
        return None

    codons = []

    for i in range(start, len(dna), 3):
        codon = dna[i:i+3]

        if len(codon) < 3:
            break

        codons.append(codon)

        if codon in ["TAA", "TAG", "TGA"]:
            return {
                "start_position": start,
                "codons": codons,
                "stop_codon": codon,
                "orf": dna[start:i+3]
            }

    return None

dna = "CCGATGAAACCGTACGGGTAACTG"

result = find_orf(dna)

if result:
    print("Start codon position:", result["start_position"])
    print("Codons:", " | ".join(result["codons"]))
    print("Stop codon:", result["stop_codon"])
    print("ORF:", result["orf"])
else:
    print("No valid ORF found.")