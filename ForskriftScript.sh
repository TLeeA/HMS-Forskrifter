#! /bin/bash

# Bash file to run re-structuring of PSA regulations documents from PDF to CSV (and into Spreadsheet)

# This script works on one file at a time.
# Using either:
# 'rammeforskriften'
# 'styringsforskriften'
# 'innretningsforskriften' or
# 'aktivitetsforskriften'

# passing "stuff" to the bash script, look at:
# https://linuxhandbook.com/bash-arguments/


# convert from .pdf to .txt and remove empty lines and page numbers
python3 ConvertFormat.py $1

# Then perform the main scanning of file and structure the CSV format using \ as separator
# Note that the scan presently needs help to start at first line (manual actionm required for new files :( )
python3 TextProcess.py  $1 >  $1.csv

# then polish the output (remove '-  ' where there were linebreaks)
python3 CSVpolish.py  $1

# Now we are ready to import in spreadsheet:

