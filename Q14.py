ch='yes'
lines=[]
while ch=='yes':
    text=input()
    if text=="":
        ch='no'
        break
    lines.append(text)
for i in lines:
    print(i)
print(lines)