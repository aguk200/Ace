from datetime import datetime

password = "password123"
FN = "test.txt"

i = 2
fa = open(FN,'a')
fr = open(FN,'r')
b = len(fr.readlines())

a = datetime.now()
print ("Hello", a)

if (i==2):
    print ("Line ",b,": ",a, file=fa)

print (b)
fa.close()
fr.close()