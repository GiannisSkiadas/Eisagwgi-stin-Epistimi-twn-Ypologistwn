sen=raw_input('Give a sentence: ')
sen=sen+""
l=list(sen)
a= len(sen)

for i in range(a-1,-1,-1):
	if ((l[i]=="!")&(i!=(a-1))):
		if (l[i+1]!="!"):
			del(l[i])
	
sen="".join(l)
print sen			


			
	
			
		

