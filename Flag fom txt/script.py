l = []
with open("1.txt") as f:
    for i in f:
        i=i.split(":")
        l.append(i)
j=0
with open("2.txt") as f:
        for j in f:
            str=f.read()
            l1=[str.replace(" ","")]
            l1=l1[0].split("\n")
# print(l)
# print(len(l1[0]))
# print(l1[0][5:6])
# print(l[0][2])
# print(l[7])
link=[]
for k in l:
    # print(k[1])
    link.append(l1[int(k[1])-1][(int(k[2])-1):(int(k[2]))])
print(''.join(link))

