INPUT_FILE='/home/enno/uni/SS24/thesis/1_RegEx/1_TMP/cd_out/3R_2MM_seq.fasta'

SEQ_COUNT=$(egrep '^>' $INPUT_FILE | wc -l)

matrix_content="BLOSUM62"
clans_eval=1e-5
GAPOPEN=11
GAPEXT=1

threads=12

echo "#Performing ${SEQ_COUNT} X ${SEQ_COUNT} pairwise BLAST+ comparisons." > process.log

#cp $INPUT_FILE query.fas
./prepareForClans.pl $INPUT_FILE query.fasta indexedfile.fasta

#BLAST formatted database
makeblastdb -in indexedfile.fasta -dbtype prot

#NXN BLAST
blastp -query indexedfile.fasta \
       -db indexedfile.fasta \
       -outfmt "6 qacc sacc evalue" \
       -matrix $matrix_content \
       -evalue $clans_eval  \
       -gapopen ${GAPOPEN} \
       -gapextend ${GAPEXT} \
       -max_target_seqs ${SEQ_COUNT} \
       -max_hsps 1 \
       -out nxnblast \
       -seg no \
       -num_threads ${threads} \
       -lcase_masking

echo "done" >> process.log

echo "#Generating CLANS file." >> process.log

./blast2clans.pl $INPUT_FILE ${SEQ_COUNT}

#zip -q myfile.clans.zip myfile.clans

echo "done" >> process.log

