
# could also have been: /usr/bin/python

# this link for converting *.pdf to *.txt:
# https://pdf.wondershare.com/pdf-knowledge/pdf-to-text-python.html

# Poppler from here:
# https://pypi.org/project/pdftotext/
# like this on iOS:
# brew install pkg-config poppler python
# like this on Linux:
# sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
# sudo apt install python3-pip
# pip3 install pdftotext

# passing argument to python, look here:
# https://machinelearningmastery.com/running-and-passing-information-to-a-python-script/


import pdftotext, re
import sys

regulation = sys.argv[1]

# regulation = 'rammeforskriften'
file_in = f"{regulation}{'_n.pdf'}"
file_tmp = f"{regulation}{'_n.tmp'}"
file_out = f"{regulation}{'_n.txt'}"

# Load your PDF
with open(file_in, "rb") as f:
    pdf = pdftotext.PDF(f)

# Save all text to a txt file.
with open(file_tmp, 'w') as f:
    f.write("\n\n".join(pdf))

no_p =len(pdf)

print('\nNumber of pages in file: ',no_p,'\n')
#print(pdf[0])

# Read all the text into one string
#print("\n\n".join(pdf))

page_list = range(no_p)
print(page_list)
page_string = ''

with open(file_out, 'w') as fo:
    with open(file_tmp, 'r') as ft:
        lines = ft.readlines()

    for line in lines:
        lin_txt = line.strip()
        #lin_txt = line.lstrip()
        if lin_txt == '':           # lines with no text wil be removed
            print('Removing an empty line of text')
        elif (not '§' in line) and (len(lin_txt) <= 2):     # lines with 2 or less caracters will 
                                                            # be checked for page numbers and removed
                                                            # this could cause trouble if real text line is short!
                                                            # Actually, it initially did remove the first 9 sections §1 - §9!
           #print(len(lin_txt)) 
           for i in page_list:
                if str(i+1) == lin_txt:
                    print('Removing the page number',lin_txt)
                    break
        else:
            fo.write(lin_txt)
            fo.write('\n')





