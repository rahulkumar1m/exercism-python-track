def to_rna(dna_strand):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'A': 'U',
        'T': 'A'
    }
    rna_strand = []

    for chara in dna_strand:
        rna_strand.append(dna_to_rna[chara])
    
    return ''.join(rna_strand)
