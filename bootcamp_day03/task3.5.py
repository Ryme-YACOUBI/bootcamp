print("Print a text :")
ch1 = input()
ch=ch1.lower()
count=0
ecarts = {
    "french": 0,
    "english": 0,
    "spanish": 0,
    "german": 0
}
french = {'e':15,'a':8,'i':8,'n':7,'o':5,'r':7,'s':8,'t':7,'l':5,
               'd':4,'u':6,'m':3,'c':3,'p':3,'v':2,'f':1,'q':1,'é':2}

english = {'e':13,'a':8,'i':7,'n':7,'o':8,'r':6,'s':6,'t':9,'l':4,
                'd':4,'u':3,'m':2,'c':3,'p':2,'h':6,'g':2,'b':1,'f':2,'y':2,'w':2}

spanish ={'e':14,'a':13,'i':6,'n':7,'o':9,'r':7,'s':8,'t':5,'l':5,
                'd':6,'u':4,'m':3,'c':5,'p':3,'g':1,'b':1}

german = {'e':17,'a':7,'i':8,'n':10,'o':3,'r':7,'s':7,'t':6,'l':3,
               'd':5,'u':4,'m':3,'c':3,'h':1,'g':5,'k':3,'b':2,'f':1,'z':2,'w':1}
et=0
mon_dic = {}
for i in range(0,len(ch)):
    if ch[i]>='a' and ch[i]<='z' and ch[i] not in mon_dic:
        mon_dic[ch[i]] = 0
    if ch[i] in mon_dic:
        mon_dic[ch[i]]+=1
    if ch[i]>='a' and ch[i]<='z':
        count+=1
for couple in mon_dic:
    mon_dic[couple]=mon_dic[couple]/count * 100
for couple in mon_dic:
  if couple in french:
    ecarts["french"] += abs(mon_dic[couple]-french[couple])
  if couple in english:
    ecarts["english"] += abs(mon_dic[couple]-english[couple])
  if couple in spanish:
    ecarts["spanish"] += abs(mon_dic[couple]-spanish[couple])
  if couple in german:
    ecarts["german"] += abs(mon_dic[couple]-german[couple])
min_ecart=min(ecarts.values())
for valeurs in ecarts:
    if ecarts[valeurs]==min_ecart:
        print(valeurs)
    
    
    