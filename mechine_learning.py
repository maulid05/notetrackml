from ddgs import DDGS 
from deep_translator import GoogleTranslator

def ddgs_handler(items):
    
        x = items
        with DDGS() as ddgs:
            hasil = ddgs.text(x, max_results=5)
            for url in hasil:
                temp = url["body"]
                deepsearch(x, temp, l_list, r_list)


def deepsearch(kata, kategori, l_ist, r_list):
  temp = kategori.split()
  
  list = []
  with open("temp.txt", "r")as f:
    for i in f:
      list.append(i)       
  
  for x0 in temp:
    if x0 in r_list:
      print(x0)
      for x1 in temp:
        if x1 != x0 :
          tempsave(x1)
          if x1 in list:
            print(x0, x1)
          elif x1 in list :
            print(x0, x1)
          ddgs_handler(x1)

def tempsave(data):
  with open('temp.txt', 'w', encoding='utf-8')as f:
    for item in data:
      f.write(*item)

def datasave(x, kategori):
    
        
                            
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
        ddgs_handler(x)
                
                


    



