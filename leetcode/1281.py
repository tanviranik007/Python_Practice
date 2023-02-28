# t=int(input())
# i=0
# while(i<t):
#     a=int(input())

a=int(input("Enter a number:"))
w=str(a)
e=list(w)
output=0
prod=1
for ij in e:
    output=output+int(ij)
    prod=prod*int(ij)
print(output)
print(prod)
print(prod-output)
    # i=i+1