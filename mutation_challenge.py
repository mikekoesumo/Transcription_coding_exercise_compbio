original_dna = "TACCGATTTACCACT"
mutated_dna = "TACCGATATACCACT"

original_mrna = transcription(original_dna)
mutated_mrna = transcription(mutated_dna)

original_codons = find_codons(original_mrna)
mutated_codons = find_codons(mutated_mrna)

original_protein = translate_sequence(original_codons)
mutated_protein = translate_sequence(mutated_codons)

print("Original protein:", " ".join(original_protein))
print("Mutated protein:", " ".join(mutated_protein))
print("Mutation changes protein:", original_protein != mutated_protein)
