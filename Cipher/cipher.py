l = []
l1 = []
l2 = []
with open("text.txt") as f:
    for i in f:
        i = i.split(", ")
        l.append(i)
j=0
for j in range(len(l[0])):
    l1.append((l[0][j])[:3])
    j += 1

k=0
def octdec(num):
    decimal_value = 0
    base = 1
    while (num):
        last_digit = int(num) % 10
        num = int(num) / 10

        decimal_value += last_digit * base
        base = base * 8
    return decimal_value
def flag(l2):
    for s in l2:
        print(s, end ='')



while(k < len(l1)):
    num = l1[k]
    r = octdec(num);
    l2.append(chr(r))
    k += 1

x=0
while(x < len(l[0])):
    if((l[0][x])[4:] == "Y"):
        None
    elif((l[0][x])[4:] == "N"):
        l2[x] = l2[x].lower()
    else:
        l2[x] = " "
    x += 1
flag(l2);





