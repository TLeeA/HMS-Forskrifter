#! /usr/bin/python3

# Final 'polish' of details:
# Python script to remove word breaks caused by original line breaks in regulation file
# Look for '-  ' (dash with double space after seems to be good and also avoid textual use of -)
# Replace by '' (nothing)

# help and hints via Google pointed to:
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

import sys

regulation = sys.argv[1]

# creating a variable and storing the text
# that we want to search
search_text = "-  "
  
# creating a variable and storing the text
# that we want to add
replace_text = "" # just for testing
  
# Opening our text file in read only
# mode using the open() function
edit_file = f"{regulation}{'.csv'}"
with open(edit_file, 'r') as file:
  
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
  
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_text, replace_text)
  
# Opening our text file in write only
# mode to write the replaced content
with open(edit_file, 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)
  
# Printing Text replaced
print("Text replaced in", regulation)