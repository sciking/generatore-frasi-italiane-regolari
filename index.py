verbi = ["and","ess","av","cant","parl","lavor"]
import random
vsuff = ["o","i","a","amo","ate","ano"]
prep = ["di", "a", "da", "in", "con","su","per","tra","fra"]
nomip = ["panettier", "calciator", "nipot", "fratell", "cugin", "insegnant"]
nsuff = ["o","a","i","e"]
def frase():
	a = verbi[random.randint(0,len(verbi)-1)] 
	b = vsuff[random.randint(0,len(vsuff)-1)]
	c = nomip[random.randint(0,len(nomip)-1)] 
	d = nsuff[random.randint(0,len(nsuff)-1)] 
	print a + b + " " + c + d
	raw_input("premi invio per fare una nuova frase")
	frase()
frase()
