#!/usr/bin/env python3
"""
Duplicate a set of templates for each team member.
"""
import os
import shutil

ORIGINALS_DIR = './originals/'
FINALS_DIR = './final/'
ORIGINAL_TEXT = '(template)'

# Get the list of names to include in the duplicated file names.
names = []
with open('names.txt', 'r') as name_list:
    for name_txt in name_list.readlines():
        names.append(name_txt.rstrip('\r\n'))
name_list.close()

# Read each original and duplicate one per name.
for original in os.listdir(ORIGINALS_DIR):
    if not original.endswith('.pdf'):
        continue

    # Make one set of copies for each name.
    for name in names:
        # Make new file name prefix.
        dupe_text = 'ITS-IAM - ' + name + ' -'
        # Make new file name.
        dupe_name = original.replace(ORIGINAL_TEXT, dupe_text)
        final = FINALS_DIR + dupe_name
        # Duplicate
        shutil.copyfile(ORIGINALS_DIR + original, final)
