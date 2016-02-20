#!/usr/bin/env python
# Creation of a new article


import os
import sys
import platform
from datetime import datetime, timedelta

from slugify import slugify


DIR = os.path.dirname(os.path.realpath(__file__))
POSTS_DIR = os.path.join(DIR, '../content/')

# Read title
title = input('Article title? ').strip()
if not title:
    sys.exit('Error: No title provided.')

# Read author
if platform.system() == 'Darwin':
    author_suggestion = 'Honza'
elif platform.system() == 'Windows':
    author_suggestion = 'Zuzka'
else:
    author_suggestion = 'Zuzka a Honza'

author_prompt = 'Article author? [{}] '.format(author_suggestion)
author = input(author_prompt).strip() or author_suggestion

# Prepare file name
slug = slugify(title)
pub_date = datetime.now() + timedelta(hours=2)
file_name = '{:%Y-%m-%d}_{}.md'.format(pub_date, slug)

# Prepare file content
template = 'Title: {}\nDate: {:%Y-%m-%d %H:%M:%S}\nAuthor: {}\n\n'
file_content = template.format(title, pub_date, author)

# Write file content
path = os.path.join(POSTS_DIR, file_name)
with open(path, 'w') as f:
    f.write(file_content)
print('File created: {}'.format(path))
