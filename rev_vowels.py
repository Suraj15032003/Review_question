s = str(input())

s_vow=""
rev_vow=""
vow ="a","e","i","o","u","A","E","I","O","U"

for i in s:
    if i in vow:
        s_vow+=i
        #print(i)
#print(s_vow)

#rev_vow=list(s_vow)
#rev_vow.reverse()
for i in range(len(s_vow)-1,-1,-1):
    rev_vow+=s_vow[i]
#print(rev_vow)

s_list =list(s)
j=0

for i in range(len(s)):
    if s[i] in vow:
        s_list[i]=rev_vow[j]
        j+=1
s=''.join(s_list)
print(s)