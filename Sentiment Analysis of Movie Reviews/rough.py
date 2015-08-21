import re
import collections

def word(text):
    return re.findall('[a-z]', text.lower( ))

print word('this seems to be a nice film')
