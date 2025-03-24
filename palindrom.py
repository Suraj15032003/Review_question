#s="madam"
s=str(input())
s_rev=""
for i in range(len(s)-1,-1,-1):
    s_rev+=s[i]
if s_rev==s:
    print("its a Palindrom")
else :
    print("Its not a plaindrom")