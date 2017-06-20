#!/usr/bin/env python3

n=int(input("Please input the n: "))
x=1
sum=0
output="The result formula is: "
while(x<=n):
    sum+=1/x
    print("Sub-total {:03d} is: {:000.3f}".format(x, sum))
#    output+="1/" + str(x)
#    if(x <= n - 1):
#        output+=" + "
    x += 1
print("\nThe summary is {:.4f}".format(sum))
#print(output)