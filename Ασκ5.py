
def gin(num):
	xil=1
	ekat=1
	dek=1
	mon=1
	if (num/1000!=0):
		xil= num/1000
	if (num/100!=0):
		ekat= num/100
		# epeidi to megisto einai to 1000 douleuei. Alliws 8a eixe provlima stous tetra4ifious me ekatontada to 0
	dek= (num%100)/10
	mon= (num%100)%10
	ginomeno= xil*ekat*dek*mon
	if ginomeno!=0:
		di= num/(ginomeno * 1.0)
		if(di == round(di)):
			return True
		else:
			return False
	
def isHarshad(num):
  num_string = str(num)
  num_list = list(num_string)
  num_int_list = []
  num_sum = 0
  for x in num_list:
    num_sum += int(x)
  num_result = num/(num_sum*1.0)
  if (num_result == round(num_result)): 
    
    return True
  else:
    return False

	

harshad_numbers = []  
gin_numbers = []

for num in range(1,1001):
  if isHarshad(num) == True:
    harshad_numbers.append(num)
  if gin(num) == True:
	gin_numbers.append(num)
print ("Harshad numbers from 1 to 1000: ")
print(harshad_numbers)
print ("")
print("Numbers that can be divided by multiplying their digits from 1 to 1000: ")
print(gin_numbers)
