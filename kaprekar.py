# Kaprekar's Constant is 6174. The speciality of this number is that when you take a random
# 4 digit number constituting atleast 2 distinct digits with each repeating a maximum of 2 times, the difference of the arrangement 
# of the digits of the number in descending order and in ascending order eventually converges to 6174
#
# ie if the digit is abcd, c>a>d>b then:
# perform cadb-bdac and continue
#
# eg: 7128
#
# 8721-1278=7443
# 7443-3447=3996
# 9963-3699=6264
# 6642-2466=4176
# 7641-1467=6174
#
# 6174 when applied to the same algorithm yields the same number: 7641-1467=6174

def kaprekar(a,b):
    n=0
    a=int("".join(map(str,a)))
    b=int("".join(map(str,b)))

    while(n!=6174):
        print(b," - ",a," = ",(b-a))
        n=b-a
        n=[int(x) for x in str(n)]
        a=sorted(n)
        b=sorted(n,reverse=True)
        a=int("".join(map(str,a)))
        b=int("".join(map(str,b)))
        n=b-a
    
    print(b," - ",a," = ",(b-a))
    print("\n6174 is the Kaprekar's Constant!")


n= input("Enter a 4 digit number with atleast 2 distinct digits and each digit repeated with a maximum of 2 times: ")
n=[int(x) for x in str(n)]
ascending=sorted(n)
descending=sorted(n,reverse=True)
kaprekar(ascending,descending)

