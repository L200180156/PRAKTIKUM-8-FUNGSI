##kegiatan 1
pilihan = {'nama':'aulia putri', 'nim': 'L200180156', 'alamat':'mojokerto', 'kode pos':'61315', 'email':'alputrir@gmail.com', 'prodi':'informatika', 'fakultas':'komunikasi dan informatika'}
def nim ():
     "fungsi ini untuk menampilkan NIM"
     print ('NIM :', pilihan['nim'])
     return

def nama ():
     "fungsi ini untuk menampilkan nama"
     print ('Nama :', pilihan['nama'])
     return

def alamat():
     "fungsi ini menampilkan alamat"
     print ('alamat :', pilihan['alamat'])
     return

def asal ():
     "fungsi ini menampilkan asal"
     print ('kode pos:', pilihan['kodepos'])
     return

def email ():
     "fungsi ini menampilkan email"
     print ('email:', pilihan['email'])
     return

def hobi ():
     "fungsi ini menampilkan hobi"
     print ('prodi:', D['prodi'])
     return

def prodi ():
     "fungsi ini menampilkan hobi"
     print ('fakultas:', D['fakultas'])
     return

print ('pilihan yang tersedia:' +
       '\nb menampilkan bantuan ini'+
       '\nN menampilkan NIM'+
       '\na menampilkan nama'+
       '\nA menampilkan alamat'+
       '\nK menampilkan kode pos'+
       '\ne menampilkan email'+
       '\np menampilkan prodi'+
       '\nf mrenampilkan fakultas'+
       '\nk keluar')
d= str(input('pilihan saudara: '))
while d != 'k':
    if d == 'b' :
        print ('pilihan yang tersedia:' +
       '\nb menampilkan bantuan ini'+
       '\nN menampilkan NIM'+
       '\na menampilkan nama'+
       '\nA menampilkan alamat'+
       '\nK menampilkan kode pos'+
       '\ne menampilkan email'+
       '\np menampilkan prodi'+
       '\nf mrenampilkan fakultas'+
       '\nk keluar')
    elif d == 'a' :
        print ('nama:', pilihan['nama'])
    elif d == 'N':
        print ('NIM:', pilihan['nim'])
    elif d == 'A':
        print ('alamat:', pilihan['alamat'])
    elif d == 'K':
        print ('kode pos:', pilihan['kode pos'])
    elif d == 'e':
        print ('email:', pilihan['email'])
    elif d == 'p':
        print ('prodi:', pilihan['prodi'])
    elif d == 'f':
        print ('fakultas:', pilihan['fakultas'])
    else:
        print ('perintah tidak dikenal')
    d= str(input('pilihan saudara: '))
if d == 'k':
    print ('terimakasih')
##kegiatan 2
def konversisuhu(c=0, f=0):
    "mengkonversi suhu dari celcius ke fahrenheit dan sebaliknya"
    diketf = (f-32) * 5/9 #mengubah suhu dari fahrenheit ke celcius
    diketc = c * 9/5 + 32 #mengubah suhu dari celcius ke fahrenheit
    if f == 0: #jika diketahui celcius, diubah ke fahrenheit
        print ('suhu', c, 'celciius setara dengan', diketc, 'Fahrenheit' )
    elif c == 0: #jika diketahui fahrenheit, diubah ke celcius
        print ('suhu', f, 'fahrenheit setara dengan', diketf, 'Celcius')
