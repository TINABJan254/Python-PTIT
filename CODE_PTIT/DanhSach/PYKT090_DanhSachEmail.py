with open('CONTACT.in', 'r') as fo:
    a = fo.readlines()

a = [line.strip().lower() for line in a]
a = sorted(set(a))
for x in a:
    print(x)