#!/bin/bash

input_dir="/home/enno/uni/SS24/thesis/1_RegEx/0_data/fasta"
output_dir="/home/enno/uni/SS24/thesis/1_RegEx/1_TMP/cd_out"

for input_file in "$input_dir"/*.fasta
do
    base_name=$(basename "$input_file" .fasta)
    output_file="$output_dir/$base_name"
    cd-hit -i "$input_file" -o "$output_file" -T 10 -M 10000 -n 5 -sc 1 -c 0.7 -d 50
done