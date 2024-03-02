pi = 3.14

def luasLingkaran(jari_jari):
    return pi * jari_jari**2

def kelilingLingkaran(jari_jari):
    return 2 * pi * jari_jari

jari_jari = int(input("Masukkan jari-jari lingkaran: "))

if jari_jari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    luas = luasLingkaran(jari_jari)
    keliling = kelilingLingkaran(jari_jari)

print(f"Luas lingkaran: {luas}")
print(f"Keliling lingkaran: {keliling}")
