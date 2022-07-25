#!/usr/bin/env python3
"""
Duplicate a set of templates for each team member.
"""
import os
import shutil

orginals_dir = './originals/'
final_dir = './final/'
original_text = '(template)'

# Get the list of names to include in the duplicated file names.
names = []
with open('names.txt', 'r') as name_list:
    for name_txt in name_list.readlines():
        names.append(name_txt.rstrip('\r\n'))
name_list.close()

# Read each original and duplicate one per name.
for original in os.listdir(orginals_dir):
    if not original.endswith('.pdf'):
        continue

    # Make one set of copies for each name.
    for name in names:
        # Make new file name prefix.
        dupe_text = 'ITS-IAM - ' + name + ' -'
        # Make new file name.
        dupe_name = original.replace(original_text, dupe_text)
        final = final_dir + dupe_name
        # Duplicate
        shutil.copyfile(orginals_dir + original, final)
