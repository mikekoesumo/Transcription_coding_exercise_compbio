def validate_dna (dna_seq):
    """ Checks if DNA sequence is valid. Returns True is sequence is valid, or False otherwise.. """
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + 
seqm.count("T")
    if valid == len(seqm): return True
    else: return False

>>> validate_dna("atagagagatctcg")
True
>>> 