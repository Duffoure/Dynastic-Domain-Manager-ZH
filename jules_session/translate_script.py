import re
import sys

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# We will build a translation mapping dictionary for all keys
# Let's write out the translations in python data structures.

