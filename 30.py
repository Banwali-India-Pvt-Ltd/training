#regular expressions in python
import re
s = 'Today is Wednesday and tomorrow is Thursday'
#re.search(pattern, string, flags<optional>)
p = re.search('(.*) Wednesday and (.*) Thursday', s)
if p:
    print 'found:',  p.group()
    print 'group1:', p.group(1), ':', p.group(1).capitalize()
    print 'group1:', p.group(2), ':', p.group(1).capitalize()

else:
    print 'not found '