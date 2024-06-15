s1=input("Enter string 1:")
s2=input("Enter string 2:")
rev=''
for i in range(len(s2)-1,-1,-1):
    rev+=s2[i]
if s1==rev:
    print("Anagram")
else:
    print("Not Anagram")