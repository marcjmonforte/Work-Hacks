#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:57:29 2017

@author: mmonforte
"""

# Import modules, define variables.
import pyperclip, re, dsp
copied_text = pyperclip.paste()
copied_list = []

# Begin by removing trailing spaces, newlines.
copied_text = copied_text.split('\n')
for item in copied_text:
    if item != '':
        copied_list.append(item.rstrip())     
data = '\n'.join(copied_list)

# If line does not start with Network ID, shift it up.
fixRegex = re.compile(r'\n(?!\d{4}:\w+)')
fixedData = fixRegex.sub(',', data)

# Swap colon and space for tab.
fixedData = fixedData.replace(':', '\t\t\t')
fixedData = fixedData.replace(' ', '\t')

# Regex to replace networkID with actual ID name.
networkRegex = re.compile('(\d{4})([\t])(.+)')
for groups in networkRegex.findall(fixedData):
    if groups[0] in dsp.dsp:
        fixedData = fixedData.replace(groups[0],dsp.dsp[groups[0]])

# Print results, update clipboard.
print('The following data is ready for use:')
print(fixedData)
pyperclip.copy(fixedData)

# Prompt to continue to EBDAextracter.py
next = input('Press any button to continue: ')
if next != 'ThisIsAnImpossibleThingToType':
    
    # Redfine variables.
    copied_text = pyperclip.paste()

    # Regex to target the tabs and retrieve CRID in the middle.
    cridList = []
    cridRegex = re.compile(r'(\d*)([\t]{3})(.*)([\t])')
    for groups in cridRegex.findall(copied_text):
        matches = groups[2]
        cridList.append(matches)
        crids = '\n'.join(cridList)
    
    # Removes new lines and formats for MSTR search.
    if "\n" in crids:
        crids = crids.replace('\n', "','")
        crids = "'" + crids + "'"
    
    # Print results, update clipboard.
    pyperclip.copy(crids) 
    print("The following ID's are formatted for MSTR:")
    print(crids)
    
else:
    print('Why.')