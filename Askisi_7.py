from json import loads
from collections import Counter
   
with open("sample.txt", "r") as document:
    d = []
    content = document.read()
    lista = content.split("\n")
    for item in lista:       
        dict_item = loads(item)
        d.append(dict_item)

while True:
    kleidi = input("Give me a key: ")
    if kleidi == "x":
        max = d[0][kleidi]
        min = d[0][kleidi]
        date_counts = Counter(i[kleidi] for i in d)
        most_common = date_counts.most_common(1)[0][0]
        print(most_common)
        for i in range(len(d)):
            if max <= d[i][kleidi]:
                max = d[i][kleidi]
            if min >= d[i][kleidi]:
                min = d[i][kleidi]
        print(max)
        print(min)
            
    elif kleidi == "y":
        max = d[0][kleidi]
        min = d[0][kleidi]
        date_counts = Counter(i[kleidi] for i in d)
        most_common = date_counts.most_common(1)[0][0]
        print(most_common)
        for i in range(len(d)):
            if max <= d[i][kleidi]:
                max = d[i][kleidi]

            if min >= d[i][kleidi]:
                min = d[i][kleidi]
        print(max)
        print(min)

    elif kleidi == "name":
        max = d[0][kleidi]
        min = d[0][kleidi]
        date_counts = Counter(i[kleidi] for i in d)
        most_common = date_counts.most_common(1)[0][0]
        print(most_common)
        for i in range(len(d)):
            if max <= d[i][kleidi]:
                max = d[i][kleidi]

            if min >= d[i][kleidi]:
                min = d[i][kleidi]
        print(max)
        print(min)
    
    elif kleidi=="1":
        break




# with open("sample.txt", "r") as f:

#     cont = f.readlines()
#     for i in cont:
#         d = loads(i) 
#         print(d.keys(), d.values())
