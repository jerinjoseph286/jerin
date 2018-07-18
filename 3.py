a=int(raw_input())
y=a
rev=0
while (a>0):
	digit=a%10
	rev=rev*10+digit
	a=a/10
if (y==rev):
	print("yes")
else:
	print("no")
