#!perl
#**********************************************************
#*                                                        *
#*     XTD2XYZ - Convert XTD files into XYZ ormat        *
#*                                                        *
#**********************************************************
# Version: 0.1
# Author: Andrea Minoia
# Date: 08/09/2010
#
# Convert MS trajectory xtd file into xYZ trajectory file.
# Backup of files that are about to be overwritten is managed
# by MS. The most recent file is that with higher index number (N)
# The script has to be in the same directory of the
# structure to modify and the user has to update the
# variable $doc (line 27) according to the name of the
# file containing the trajectory.
# The xmol trajectory is stored in trj.txt file and it is not
# possible to rename the file within MS, nor it is possible to
# automatically export it as xyz or car file. You should manage
# the new trajectory manually for further use (e.g. VMD)

use strict;
use Getopt::Long;
use MaterialsScript qw(:all);

#open the multiframe trajectory structure file or die 


my $doc = Documents->ActiveDocument;
# $変数 %ハッシュ @配列 ll 
my %Args;
GetOptions(\%Args, "Element1=s", "Element2=s", "Element3=s", "Element4=s",
		"Element5=s","Atomcount=i");

my $El1 = $Args{"Element1"};			# Frame to start from
my $El2  = $Args{"Element2"}; 			# Frame to end on, 0=last
my $El3   = $Args{"Element3"}; 
my $El4   = $Args{"Element4"};
my $El5   = $Args{"Element5"};
my $Atomcount   = $Args{"Atomcount"};

# The trajectory document
my $filename = $doc->Name;
$doc = $Documents{"$filename.xsd"};
my $word1 ="  0.00000D-00";

my $xmolFile=Documents->New("coordinate_xyz.txt");
$xmolFile->Append(sprintf "%9s\n",$word1); 
    




my $newStudyTable = Documents->New("$filename"."_Count.std");
my $dataSheet = $newStudyTable->Sheets->Item(0);
$dataSheet->Title = "Statistics";


$dataSheet->ColumnHeading(0) = "Setname";


$dataSheet->Cell(0, 0) = $El1;
$dataSheet->Cell(1, 0) = $El2;
$dataSheet->Cell(2, 0) = $El3;
$dataSheet->Cell(3, 0) = $El4;
$dataSheet->Cell(4, 0) = $El5;

my @Element;

for (my $i=0; $i<$Atomcount; $i++)

{
	push @Element, $dataSheet->Cell($i, 0);

}


    
     # loops over the frames 
   my $lattice = $doc->SymmetryDefinition;
       $lattice->VectorA->X,
       $lattice->VectorA->Y,
       $lattice->VectorA->Z;
   
 
 my $lattice = $doc->SymmetryDefinition;
my $lX=$lattice->LengthA;
my $lY=$lattice->LengthB;
my $lZ=$lattice->LengthC;
 



for (my $i=0; $i<$Atomcount; $i++)
{
  
   
     my @atoms;
    foreach my $atom (@{$doc->UnitCell->Atoms}) {
    if($atom->ElementSymbol eq $Element[$i]){
my    $CdtX=$atom->XYZ->X;
my     $CdtY=$atom->XYZ->Y;
my      $CdtZ=$atom->XYZ->Z;
my $number=$i+1;

while($CdtX > $lX){
$CdtX -= $lX
}
while($CdtX < 0){
$CdtX += $lX
}
while($CdtY > $lY){
$CdtY -= $lY
}
while($CdtY < 0){
$CdtY += $lY
}
while($CdtZ > $lZ){
$CdtZ -= $lZ
}
while($CdtZ < 0){
$CdtZ += $lZ
}
$xmolFile->Append(sprintf "%5d%25.17e%25.17e%25.17e\n", "$number", ($CdtX-$lX/2)*0.0000000001,($CdtY-$lY/2)*0.0000000001,($CdtZ-$lZ/2)*0.0000000001); 
    }
   }

   }       	 
        	
         
  