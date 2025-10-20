from ddgs import DDGS 

masukan = input().lower().split()
l_list = []
r_list = []

with open("dataset.txt", "r") as items:
    for i in items:
        i = i.strip()
        if i:
          if "," in i:
            l, r = i.split(",", 1)
            l_list.append(l.strip())
            r_list.append(r.strip())

for x in masukan:
      if x in  l_list:
        index = l_list.index(x)
        print(l_list[index])
        print(r_list[index])
      else: 
        link = []
        with DDGS() as ddgs:
            hasil = ddgs.text(x, max_results=5)
            for url in hasil:
                temp = url["href"]
                link.append(temp)
                print(temp)


    



