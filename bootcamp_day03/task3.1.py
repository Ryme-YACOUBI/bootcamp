print("Tap your name :")
ch = input()
ch = ch[0].upper()+ch[1:len(ch):1].lower()
print(f"Hello {ch}")