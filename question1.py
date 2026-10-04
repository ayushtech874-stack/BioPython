# 1 b. Using the Seq class from Biopython, create a DNA sequence object and: i. Slice the
#sequence to extract a specific region (e.g., from index 3 to 10). ii. Concatenate this sequence with
#another sequence. iii. Transcribe and translate the concatenated sequence into RNA and protein
#sequences.
from Bio.Seq import Seq
dna_seq = Seq("ATGCTAGCTAGCTAGCTG")
print("Original DNA Sequence : ",dna_seq)
sliced_dna = dna_seq[3:11]
print("Sliced DNA Sequence : ",sliced_dna)
another_Seq = Seq("GGCTAG")
concatenated_seq = dna_seq + another_Seq

print("Concatenated Sequence : ",concatenated_seq)
trim_len = len(concatenated_seq) - (len(concatenated_seq)%3)
trimmed_seq = concatenated_seq[:trim_len]

rna_sequence = trimmed_seq.transcribe()
print("RNA Sequence  : ",rna_sequence)

protein_seq = rna_sequence.translate()
print("Protein Sequence : ",protein_seq)