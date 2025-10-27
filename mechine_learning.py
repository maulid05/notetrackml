from ddgs import DDGS
from deep_translator import GoogleTranslator
from collections import Counter

def deepsearch(query):
    print("============ " + query + " =========")
    save = {}

    with DDGS() as ddgs:
        result = list(ddgs.text(query, max_results=5))

    for i, item in enumerate(result, 1):
        print()
        body = item.get("body", "")
        potong = " ".join(body.split())
        output = GoogleTranslator(source='auto', target='id').translate(potong.lower())
        save[i] = output
    bahan(query, save)
     
def bahan(masukan, save):
    teks_list = list(save.values())

    semua_kata = []
    for teks in teks_list:
        semua_kata.extend(teks.split())

    nout = Counter(semua_kata)

    finalsearch(masukan, nout.most_common(10))

def finalsearch(masukan, bahan):
    print(masukan + " = " + str(bahan))


masukan = input("tanya ddgs: ").lower().split()
index = len(masukan)

for i in range(index - 1):
    deepsearch(masukan[i])
    deepsearch(masukan[i+1])
    for n in range(index -1):
        if masukan[i] != masukan[n+1]:
            cari = masukan[i]+ " " + masukan[n+1]
            deepsearch(cari)
