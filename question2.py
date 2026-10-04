#b. Python Script to Read Sequence Data from a FASTA File and Extract Both the Sequence and its
#Description (Header)
from Bio import SeqIO
fasta_file = "C:/BioPython/Sequence.fasta"
for record in SeqIO.parse(fasta_file , "fasta"):
    print("Description : ",record.description)
    print("Sequence : ",record.seq)
    print("-"*50)
