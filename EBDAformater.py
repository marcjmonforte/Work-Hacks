#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:32:39 2017

@author: mmonforte

For use when you get an EBDA email; will format it cleanly for Google Sheets.
INPUT: Your clipboard should be the lines of data from the EBDA email.
OUTPUT: Tabbed data, which should be easy to insert into Google Sheets.
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
fixRegex = re.compile(r'\n(?!\d{4}:\d+)')
fixedData = fixRegex.sub(',', data)


# Swap colon and space for tab.
fixedData = fixedData.replace(':', '\t')
fixedData = fixedData.replace(' ', '\t')

# Regex to replace networkID with actual ID name.
networkRegex = re.compile('(\d{4})([\t])(\d+)')
for groups in networkRegex.findall(fixedData):
    if groups[0] in dsp.dsp:
        fixedData = fixedData.replace(groups[0],dsp.dsp[groups[0]])

# Replace networkID with actual ID name.
# networkRegex = 

# Print results, update clipboard.
print('The following data is ready for use:')
print(fixedData)
pyperclip.copy(fixedData)