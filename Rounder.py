# IMPORTING LIBS
#region
import pandas as pd
import numpy as np
import os
import re
import glob
import csv
#endregion

# INPUT VARIABLES
#region
# Directory of the csv files you want to process
Input_path_CSVs = 'D:/algae/'

# Output of the processed CSV files
Output_path_processed_csv = 'D:/algae/output/'

# Can change to xlsx if needed, other changes will be nessesary to code
Extension = 'csv'

# Csv files seperator for input and output files..generally (,) or (|)
Delimiter = '|'
#endregion

# SAVE CSV FILENAMES IN A LIST AND DATAFRAME
#region
# Get the csv filenames into an array
os.chdir(Input_path_CSVs)
filenames = [i for i in glob.glob('*.{}'.format(Extension))]

# Get the number of csv files
NumFiles = len(filenames)
print(NumFiles, 'files will be processed')
#endregion

# LOOP THOUGH EACH FILE AND PROCESS IT, CREATE EXCEL REPORT ON CHANGES MADE
#region
# Get the csv filenames into an array
os.chdir(Input_path_CSVs)
filenames = [i for i in glob.glob('*.{}'.format(Extension))]


###################  START BIG LOOP  #######################################
# Loop through each csv file in the input directory
for filename in filenames:
    
    # Save an individual file as a DataFrame Object to analyse
    df_file = pd.read_csv(filename, sep=Delimiter, index_col=False, engine='python')
    # Delete Rows with everything missing in the row
    df_file = df_file.dropna(axis='index', how='all')
    
    # Round the whole dataframe
    df_file = df_file.round(8)

  
    ###################  PROCESSED FILE  ############################

    
    Output_filename = Output_path_processed_csv + filename
    df_file.to_csv(path_or_buf=Output_filename, sep='|', index=False)
    
    print(file made)
    
###################  END BIG LOOP  #######################################

print('DONE')
#endregion