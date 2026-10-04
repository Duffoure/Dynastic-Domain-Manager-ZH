import re
import json

# Read english file
with open('english/ddm_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# Dict for translated keys
tr = {}

def add(k, v):
    tr[k] = v

# Load existing json or section definitions if any, then populate remaining.
# Let's populate the comprehensive translation mapping dictionary!

