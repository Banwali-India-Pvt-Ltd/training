#regular expression
import re
s = 'Today is Wendnesday and tomorrow is Thursday'
#re.match(pattern string, flogs flags<optional>
p = re.match('today.*', s, re.I)
if p:
    print 'found match'
else:
    print 'no match'




import re
s = 'Kuldeep khatik  banwali'
p = re.match('kuldeep.*',s, )
if p:
   print 'found match'
else:
    print  'no match'