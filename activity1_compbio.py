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
    "AUG": "M",
    "GCU": "A",
    "AAA": "K",
    "UGG": "W",
    "UGA": "*"
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


# DNA template sequence
dna = "TACCGATTTACCACT"

# Transcription
mrna = transcription(dna)

# Divide mRNA into codons
codons = find_codons(mrna)

# Translation
protein = translate_sequence(codons)


print("DNA:", dna)
print("mRNA:", mrna)
print("Codons:", " | ".join(codons))
print("Amino-acid sequence:", " ".join(protein))
