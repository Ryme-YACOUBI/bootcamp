print("Tap a string :")
ch = input()
ch1 = ""
for i in range(0,len(ch)):
    if i!=len(ch)-1 and ch[i]==' ' and ch[i+1]!=' ':
        ch1 =ch1 + ch[i+1]
    if i==0 and ch[0]!=" ":
        ch1 = ch[0]
print(ch1) 