#Script for Extracting Proteins and their Isoelectric Points (pI)#
import numpy as np
import scipy as sp

# Set Vectors for peptides and their experimental Isoelectric points and those predicted by other algorithms
peptide_names = []
exp_pI = []
theory_pI = []

# Import Peptide Sequence and Isoelectric points
peptides = open('Pep_pIs2.csv', 'r')

# Looping through .CSV file, splitting into Peptide Chain, Experimental and algorithmic pI values
while 1:

    csv_line = peptides.readline()

    if csv_line.__contains__('(ox') == False:

        if len(csv_line) != 0:
            csv_pep = str(csv_line)
            csv_split = csv_pep.split(';')


            # append to peptide names
            acbegin = ['#']
            nhbegin = ['@']

            csv_peptide = csv_split[0]
            csv_peptide = list(csv_peptide)
            prefix = csv_peptide[0] + csv_peptide[1] + csv_peptide[2] + csv_peptide[3]


            if prefix.__contains__('_(ac') == True:
                del csv_peptide[0:5]
                csv_peptide = acbegin + csv_peptide
                csv_peptide = ''.join(csv_peptide)

            if prefix.__contains__('_(ac') == False:
                del csv_peptide[0]
                csv_peptide = nhbegin + csv_peptide
                csv_peptide = ''.join(csv_peptide)

            csv_peptide = csv_peptide.replace('_', '$')


            peptide_names.append(csv_peptide)
            # peptide_names.append(csv_peptide2)

            # append to experimental pI values
            csv_exp_pI = float(csv_split[1])
            exp_pI.append(csv_exp_pI) #pIs determined by experimentation

            # append to pI values from other algorithms
            csv_theo_pI = float(csv_split[2].strip('\n'))
            theory_pI.append(csv_theo_pI) #pIs before, predicted by other algorithms

    if len(csv_line) == 0:
        break

# Loop for replacing leading '_' and '_(ac)' with '@' and '#' respectively. Also replacing ending '_' with '$'




print(peptide_names)
print(len(peptide_names))
