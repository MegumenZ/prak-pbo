class Mhs:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.daftar_nilai = []
        
    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)
            
    def hitung_rata_rata(self):
        if not self.daftar_nilai:
            return 0
        total_nilai = sum(self.daftar_nilai)    
        return total_nilai / len(self.daftar_nilai)
        
    def status_lulus(self):
        rata_rata = self.hitung_rata_rata()
        return rata_rata > 68


# Contoh penggunaan:
if __name__ == "__main__":
    Mhs = Mhs("Luthfiandri Ardanie", "122140089")
    Mhs.tambah_nilai(84)
    Mhs.tambah_nilai(84)
    Mhs.tambah_nilai(85)
    
    print("Mhs: ", Mhs.nama, "(", Mhs.nim, ")")
    print("Rata-rata nilai: ", Mhs.hitung_rata_rata())
    if Mhs.status_lulus():
        print("Status kelulusan: Lulus")
    else:
        print("Status kelulusan: Tidak Lulus")
