low=int(input("Enter a low Number: "))
high=int(input("Enter a high Number: "))

if low%2==0 & high%2==0:
    result =(high+1)-low
    print(result//2)
else: 
    low%2==1 & high%2==1
    result =(high+1)-(low-1)
    print(result//2)