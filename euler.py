import datetime

sun = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        d = datetime.date(year, month, 1)
        if d.weekday() == 6:
            sun = sun + 1

print sun

#===================================
import math
 phi = (1 + pow(5, 0.5)) / 2
 b = math.log10(5) / 2
 logp = math.log10(phi)
 n = 1
while True:
     if n * logp - b >= 999:
        print n
         break
     n = n + 1