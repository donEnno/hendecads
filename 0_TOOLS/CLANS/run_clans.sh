INPUT_FILE=$1

java -Xmx8G -jar CLANSclans_20170324.jar -load /home/enno/uni/SS24/thesis/0_TOOLS/CLANS/5R_1MM_seq.clans -cpu 12 -nographics true -dorounds 3000 -pval 1 -cluster2d true -saveto ../1_seq_analysis/3/3R_5k.clans -initialize true
