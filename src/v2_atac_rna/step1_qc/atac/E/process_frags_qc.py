import os
import random
import sys


# ALLOWED CHROS
allowed_chros = [f"chr{i}" for i in range(1, 20)] + ["chrX", "chrY"]

# PARSE INPUT
sample = str(sys.argv[1])
basedir = str(sys.argv[2])
input_fragments_file_path = str(sys.argv[3])

# SET UP FILENAMES
out_pseudorepT_file = f"{basedir}/{sample}_Tn5_sites.tsv"


# PARSE FRAGMENTS FILE
num_matches = 0
with open(input_fragments_file_path, 'r') as f_f_in, open(out_pseudorepT_file, 'w') as f_pT_out:
	for line in f_f_in:
		chro, start, end, barcode, reads = line.strip().split("\t")
		start = int(start); end = int(end)
		if chro in allowed_chros:
			num_matches += 1
			# Output pseudorepT
			f_pT_out.write(f"{chro}\t{start}\t{start+1}\t{barcode}\t{reads}\n")
			f_pT_out.write(f"{chro}\t{end-1}\t{end}\t{barcode}\t{reads}\n")



print(f"{sample} {num_matches} read pairs")