# Overloading
# Pada bahasa pemrograman lain yang mendukung paradigma OO seperti C# ataupun Java, 
# polymorphism juga dapat diterapkan melalui sebuah fitur yang dikenal dengan istilah metode overloading.
# Metode overloading mengizinkan sebuah class untuk memiliki sekumpulan fungsi dengan nama yang sama dan parameter yang berbeda. 
# Berkaitan dengan hal ini, Python tidak mengizinkan pendeklarasian fungsi (baik pada class ataupun tidak) dengan nama yang sama.
# Untuk mengimplementasikan method overloading pada Python, aku dapat menggunakan sebuah teknik yang dikenal dengan function default parameters.

class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    # usia akan di-set nilainya menjadi 21 saat tidak
    # dispesifikasikan dan pendapatan akan di-set nilainya
    # menjadi 5000000 saat tidak dispesifikasikan
    def __init__(self, nama, usia=21, pendapatan=5000000): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Karyawan baru pertama yang bernama Budi
karyawan_baru1 = Karyawan('Budi')
print(karyawan_baru1.nama)
print(karyawan_baru1.usia)
print(karyawan_baru1.total_pendapatan())
# Karyawan baru ke-2 yang bernama Didi, umur 25
karyawan_baru2 = Karyawan('Didi', 25)
print(karyawan_baru2.nama)
print(karyawan_baru2.usia)
print(karyawan_baru2.total_pendapatan())
# Karyawan baru ke-3 yang bernama Hadi, pendapatan 8000000          
karyawan_baru3 = Karyawan('Hadi', 8000000)
print(karyawan_baru3.nama)
print(karyawan_baru3.usia)
print(karyawan_baru3.total_pendapatan())