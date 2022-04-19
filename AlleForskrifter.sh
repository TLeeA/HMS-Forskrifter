#! /bin/bash

# Bash file to run re-structuring of all PSA regulations in norwegian

# get present version of regulations (and keep old ones as backup, just in case):
wget --backups=1 https://www.ptil.no/globalassets/regelverk/gjeldende-regelverk-2022/rammeforskriften_n.pdf
wget --backups=1 https://www.ptil.no/globalassets/regelverk/gjeldende-regelverk-2022/styringsforskriften_n.pdf
wget --backups=1 https://www.ptil.no/globalassets/regelverk/gjeldende-regelverk-2022/innretningsforskriften_n.pdf
wget --backups=1 https://www.ptil.no/globalassets/regelverk/gjeldende-regelverk-2022/aktivitetsforskriften_n.pdf

# Restructure (.pdf -> .csv, using \ as seperator):
bash ForskriftScript.sh rammeforskriften
bash ForskriftScript.sh styringsforskriften
bash ForskriftScript.sh innretningsforskriften
bash ForskriftScript.sh aktivitetsforskriften

# Import the .csv files into .xlsx
python3 Spreadsheets.py

echo "I'm done"