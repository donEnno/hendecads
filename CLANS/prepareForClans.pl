#!/usr/bin/perl
#This script removes '-' characters from the FASTA formatted input file and 
#coverts sequences to upper case.

use strict;
use warnings;

#fasta formatted input file (e.g. nr)
my $inputFile  = $ARGV[0];
#fasta formatted output file
my $outputFile = $ARGV[1];
my $indexedFile = $ARGV[2];
my $index=0;

my $seq="";
my $firstVisit=0;
#file handle
open my $FH, '<', $inputFile or die "Could not open file $inputFile!";
open my $WH, '>', $outputFile or die "Could not open file $outputFile!";
open my $INDEXFILE, '>', $indexedFile or die "Could not open file $indexedFile!";


while (my $line = <$FH>){
    #remove ^M and ^A
    $line =~ s/(\r|\x01)//g;

    if( $line =~ /^>/ ){
	if($firstVisit == 0){
		$firstVisit=1;
	}
	else {
		#write sequence to output file
		print $WH $seq."\n";
		print $INDEXFILE $seq."\n";
		$seq="";
	}
	#write header to the output file
	print $WH $line;
	print $INDEXFILE ">".$index."\n"; 
	$index++;
    }
    else {
	chomp $line;
	#remove '-'
	$line=~ s/-//g;

	#convert to upper case
	#$line = uc $line;

	#concatenate sequence split into multiple lines
	$seq = $seq.$line;
    }
}
#Write the last sequence to the output file
print $WH $seq."\n";
print $INDEXFILE $seq."\n";

#close file handles
close $FH;
close $WH;
close $INDEXFILE;
