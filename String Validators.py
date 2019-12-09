s=input()
res1 = ""
res2=""
res3=""
res4=""
res5=""
for i in s: 
    if i.isalpha(): 
        res1 = "".join([res1, i])
    if i.isdigit():
        res2="".join([res2,i])
    if i.isupper():
        res3="".join([res3,i])
    if i.islower():
        res4="".join([res4,i])
    if i.isalnum():
        res5="".join([res5,i])
    
print(res5.isalnum())
print(res1.isalpha())
print(res2.isdigit())
print(res4.islower())
print(res3.isupper())

