#! /usr/local/bin/python3

# TLA 2022-04-07
# For AkerBP @ private initiative

# Load your PDF
#with open("rammeforskriften_n.txt") as f:
#    contents = f.read()
#print(contents.rstrip())

# Plan:
# Scan file in a line by line manner while checking if
# 'KAPITTEL' shows up to group in first level and check if 
# '§#' shows up to group in second level and
# join all lines until next 2nd level match
# so far its testing and a work-in-progress :)


##
## It would be good to strip away the page numbers and blank lines early in the process...
## Not sure how, but perhaps look for empty lines and also lines with incrementing numbers.
## perhaps also use the same prosedyre to strip away the front matter where §# shows up...
## ie ... awoiding the MAGIC number "139"
##

import sys

regulation = sys.argv[1]

#regulation = 'rammeforskriften'
file_name = f"{regulation}{'_n.txt'}" 
file_out = f"{regulation}{'_n.csv'}"
#with open("rammeforskriften_n.txt") as f:
with open(file_name) as f:
    lines = f.readlines()

lineno = 0
line_scan = 0
kapno = 0
secno = 1
#search_for = '§1'
search_kap = 'KAPITTEL'
search_sec = f"{'§'}{secno}"
secline = 0
maintxt = ''
txtfound = False

#print("searching for",search_kap)
#print(search_sec)


for line in lines:
    line_scan = line_scan + 1
#    print(line_scan)
    if line.strip() == 'KAPITTEL I':
#        print('start of main text found at line ',line_scan)
        break


#print(line_scan)

# Define a header:
#with open(file_out, 'w') as fo:
#    fo.write('Forskrift\\','Kapittel nummer\\','Kapittel linje\\','Paragraf nummer\\','Paragraf linje\\','Kapittel ID\\','Kapittel tittel\\','Paragraf ID\\','Paragraf tittel\\','Paragraf tekst\\', end = '')
print('Forskrift\\','Kapittel nummer\\','Kapittel linje\\','Paragraf nummer\\','Paragraf linje\\','Kapittel ID\\','Kapittel tittel\\','Paragraf ID\\','Paragraf tittel\\','Paragraf tekst', end = '')


for line in lines:
    lineno = lineno + 1
    #if lineno > 128:
 #   if lineno > 116:
    if lineno > line_scan-1:
 #   if lineno >= line_scan:
        if search_kap in line:      # here is the chapter and chapter text string in one line
            kapno = kapno + 1
            kapline = lineno
            kapid = line.strip()
#            print(regulation,'\\',kapline,'\\',kapno,'\\',kapid,'\\')
        elif lineno == (kapline + 1): # here is the chapter text string
            kaptxt =  line.strip()
#            print(regulation,'\\',kapline,'\\',kapno,'\\',kapid,'\\',kaptxt,'\\')
        elif search_sec in line:  # here is the section (§) marker
            secid = line.strip()
            secline = lineno
#            print(regulation,'\\',kapline,'\\',kapno,'\\',kapid,'\\',kaptxt,'\\',secline,'\\',secno,'\\',secid,'\\')
            # increment section counter:
            secno = secno + 1
            # A bug in the section/paragraph format of the regulations text (!!)
            if secno <= 9:
                search_sec = f"{'§'}{secno}"  # no space between is easier for searching
                #print(search_sec)
            else:
                search_sec = f"{'§'} {secno}"   # the space is also usen in running text ans can cause trouble...
                #print(search_sec)
        elif lineno == (secline + 1): # here is the section (§) text string
            sectxt =  line.strip()
#            print(regulation,'\\',kapline,'\\',kapno,'\\',kapid,'\\',kaptxt,'\\',secline,'\\',secno-1,'\\',secid,'\\',sectxt,'\\')
            print('\n',regulation,'\\',kapno,'\\',kapline,'\\',secno-1,'\\',secline,'\\',kapid,'\\',kaptxt,'\\',secid,'\\',sectxt,'\\', end = '')
#       Main text of the section (concaternate several lines) 
        else:
            txtfound = True
            txtpart = line.strip()
            maintxt = f"{maintxt} {txtpart}"
            print(txtpart,' ', end = '')
#            print(regulation,'\\',lineno,'\\',kapno,'\\',kaptxt,'\\',secno-1,'\\',secid,'\\',sectxt,'\\',maintxt)
#            print(regulation,'\\',lineno,'\\',kapno,'\\',kaptxt,'\\',secno-1,'\\',maintxt,'\\ \n')

#            print(regulation,'\\',lineno,'\\',kapno,'\\',kaptxt,'\\',secno-1,'\\',secid,'\\',sectxt,'\\')
#            print(line.strip())
#        if txtfound:
#            print(regulation,'\\',lineno,'\\',kapno,'\\',kaptxt,'\\',secno-1,'\\',secid,'\\',sectxt,'\\',maintxt)
