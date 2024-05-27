#!/bin/bash

# Directory containing the files
DIRECTORY="../../1_RegEx/1_TMP/cd_out_5R"
DIRECTORY="../..//1_RegEx/0_data/test"

# P-value for run_clans.sh
PVAL="1E-2"

# Iterate over all .fasta files in the directory
find "$DIRECTORY" -type f -name "*.fasta" | while read -r FILE
do
  # Run 1_blast_all_vs_all.sh on the file
  ./1_blast_all_vs_all.sh "$FILE"

  # Extract the base name of the file
  BASE_NAME=$(basename "$FILE")

  # mv myfile.clans to basename.clans
  mv "myfile.clans" "${BASE_NAME}.clans"

  # Run run_clans.sh on the output of the previous script
  # ./run_clans.sh "${BASE_NAME}.clans" "$PVAL"
done