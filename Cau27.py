def ToiUuChuoi(s):
    return ' '.join(s.split()).title()

s='         trẦn THanh THẢN   '
print(s,'=>',len(s))
s=ToiUuChuoi(s)
print(s,'=>',len(s))