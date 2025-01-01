import sys

s = ''
for line in sys.stdin:
    s += ' '.join([word for word in line.split()]).strip()

s = s.lower() 
s = s.replace('?', '.')
s = s.replace('!', '.')
s = s.replace('. ', '.')
s = s.replace(' . ', '.')
s = s.replace('.', '.')
res = s.split('.')
for x in res: 
    print(x.capitalize())

    