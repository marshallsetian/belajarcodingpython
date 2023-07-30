

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('belajar coding python pemula\n'
         'sedang tested running program \n'
         'semoga bisa belajar bertahap')



data1 = input("nama anda : \n")
#print ("nama anda adalah = ",data)
data2 = input("nama lengkap anda : \n")
"\n"
#print ("nama anda adalah = ",data)

data3 = input("berapa usia anda sekarang : \n")
#print ("usia anda adalah = ",data)

data4 = input("apakah anda sudah menikah : \n")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('konfirmasi data anda apakah sudah benar??\n'
       
         'semoga bisa belajar bertahap')
print ("konfirmasi data anda ?" )
print ("nama panggilan :",data1)
print ("nama lengkap :",data2)
print ("usia :",data3)
print ("status perkawinan :",data4)



