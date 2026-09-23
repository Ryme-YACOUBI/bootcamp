def compter_occ(ch,ch1,ch2,ch3):
    chl=ch.lower()
    chl1=ch1.lower()
    chl2=ch2.lower()
    chl3=ch3.lower()
    count=chl.count(chl1)+chl.count(chl1[::-1])+chl.count(chl2)+chl.count(chl2[::-1])+chl.count(chl3)+chl.count(chl3[::-1])
    print(f"{count}")
compter_occ("the CataCat attaCk a Cat","cat","garden","MICE")
compter_occ("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN","cat","garden","mice")