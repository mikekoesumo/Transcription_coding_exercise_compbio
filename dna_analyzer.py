def transcription(dna):
    rna = ""

    for base in dna:
        if base == "A":
            rna += "U"
        elif base == "T":
            rna += "A"
        elif base == "C":
            rna += "G"
        elif base == "G":
            rna += "C"

    return rna


def find_codons(sequence):
    codons = []

    for i in range(0, len(sequence), 3):
        codons.append(sequence[i:i+3])

    return codons


genetic_code = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C",
    "UGA": "*", "UGG": "W",

    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def translate_codon(codon):
    return genetic_code.get(codon, "?")


def translate_sequence(codons):
    protein = []

    for codon in codons:
        amino_acid = translate_codon(codon)

        if amino_acid == "*":
            break

        protein.append(amino_acid)

    return protein


def find_orf(dna):
    start = dna.find("ATG")

    if start == -1:
        return None

    for i in range(start, len(dna) - 2, 3):
        codon = dna[i:i+3]

        if codon in ["TAA", "TAG", "TGA"]:
            return {
                "start_position": start,
                "stop_position": i,
                "stop_codon": codon,
                "orf": dna[start:i+3]
            }

    return None


# Get DNA sequence from the user
dna = input("Enter a DNA sequence: ")

# Convert to uppercase and remove spaces
dna = dna.upper().replace(" ", "")

# Transcription
mrna = transcription(dna)

# Find codons and translate protein
codons = find_codons(mrna)
protein = translate_sequence(codons)

# Find ORF
orf_result = find_orf(dna)


# Display results
print("\nDNA:", dna)
print("mRNA:", mrna)
print("Codons:", " | ".join(codons))
print("Protein:", " ".join(protein))


if orf_result:
    print("Start codon position:", orf_result["start_position"])
    print("Stop codon position:", orf_result["stop_position"])
    print("Stop codon:", orf_result["stop_codon"])
    print("ORF:", orf_result["orf"])
    print("Valid ORF:", True)
else:
    print("Start codon position: Not found")
    print("Stop codon position: Not found")
    print("ORF: Not found")
    print("Valid ORF:", False)