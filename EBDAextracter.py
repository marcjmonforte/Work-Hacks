#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:09:52 2017

@author: mmonforte

This should be used after 'EBDAformater.py' to quicky extract IDs!
Input: Your clipboard should have results from EBDAformater.py.
Output: Formatted IDs for MSTR.

"""

# Import modules, define variables.
import pyperclip, re
copied_text = pyperclip.paste()


# Regex to target the tabs and retrieve CRID in the middle.
cridList = []
cridRegex = re.compile(r'(\d*)([\t]{3})(\w*)([\t])')
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