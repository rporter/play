# maths test generator
#
# Usage : python maths-test.py <name> <seed> [give me answers]
#
# html answers has page break for 2 sided printing

import random
import sys

rows, cols = 22, 3
user = sys.argv[1]

s=3
m=set()
for a in range(s,13):
 for b in range(s,13):
  m.update((tuple(sorted((a,b))),))

random.seed(int(sys.argv[2]))
q = [list(d) for d in m]
while len(q) <= (rows*cols) :
  q.append(random.choice(q))
for d in q : 
  random.shuffle(d)
random.shuffle(q)
out = sys.stdout

def table(q, ans=False):
  out.write('<h1>'+user+"'s "+('Answers' if ans else 'Sums')+'</h1><table>')
  for r in range(rows):
    out.write('<tr>')
    for c in range(cols):
      d=q.pop()
      d.append(d[0]*d[1])
      d = ['{:>3}'.format(str(d)) for d in d]
      if not(ans) : d[random.randrange(3)] = '___'
      out.write('<td><pre>{0} x {1} = {2}</pre></td>'.format(*d))
      if c < 2:
        out.write('<td class="break"/>')
    out.write('</tr>')
  out.write('</table>') 

out.write('''<html><head><style>
h1       { text-align : center }
table    { width : 100% }
td       { font-size:14pt; padding-bottom:14pt }
td.break { width:40pt }
@media print {
    .pagebreak { page-break-before: always; } /* page-break-after works, as well */
}
</style></head><body>''')
table(list(q))
out.write('<div class="pagebreak"/>')
table(q, True)
out.write('</body></html>')
