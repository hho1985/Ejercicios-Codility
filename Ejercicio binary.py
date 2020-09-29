binary = bin(10)[2:]
count =0
maximo = 0
print (binary)

for i in binary:
    if i == '0':
        count+=1

    else:
        if count > maximo:
            maximo  = count
            count =0

print (maximo)
