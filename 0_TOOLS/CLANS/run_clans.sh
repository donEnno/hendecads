INPUT_FILE=$1
PVAL=$2

BASE_NAME=$(basename $INPUT_FILE)
OUTPUT_FILE="${BASE_NAME}_${PVAL}.clans"

java -Xmx8G -jar CLANSclans_20170324.jar -load $INPUT_FILE -cpu 12 -nographics true -dorounds 300 -pval $PVAL -cluster2d true -saveto /home/enno/uni/SS24/thesis/1_RegEx/1_TMP/clans_out_5R/$OUTPUT_FILE -initialize false
