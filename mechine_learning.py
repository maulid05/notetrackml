masukan = input().lower()
with open("dataset.txt", "r") as n:
  dataset = [line.strip() for line in n ]
cek = masukan.split()

ada = False

for x in cek:
  if x in dataset:
    print(x)
    ada = True


if not ada :
  tambah = input("tambah kategori: ").lower()
  with open("dataset.txt", "a") as n:
    n.write(tambah + "\n")
  print('data ditambahkan') 
      

    