# Fungsi untuk menghitung total dan menyimpan ke database
def p(items, d):
    # Hitung total harga
    t = 0
    for i in items:
        t += i['price']
    
    # Cek diskon
    if d == "PROMO10":
        t = t - (t * 0.1)
    
    print(f"Total: {t}")

    # Simpan ke file (ceritanya database)
    f = open("db.txt", "a")
    f.write(f"Order: {t}\n")
    f.close()
    
    return t
