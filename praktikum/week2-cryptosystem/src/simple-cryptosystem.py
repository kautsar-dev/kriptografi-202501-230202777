# file: praktikum/week2-cryptosystem/src/simple_crypto.py
def caesar_cipher(text, key, mode='enkripsi'):
    """
    Fungsi untuk melakukan enkripsi atau dekripsi menggunakan Caesar Cipher.
    """
    
    # Jika mode adalah dekripsi, gunakan kunci negatif untuk membalikkan pergeseran
    if mode == 'dekripsi':
        key = -key
    
    result = ""
    for char in text:
        if char.isalpha(): # Proses hanya untuk karakter huruf
            
            # Tentukan karakter awal ('a' untuk huruf kecil, 'A' untuk huruf besar)
            start_char = 'a' if char.islower() else 'A'
            
            # Hitung posisi abjad (0-25)
            char_index = ord(char) - ord(start_char)
            
            # Terapkan pergeseran dan pastikan hasilnya dalam rentang 0-25 (modulo 26)
            new_index = (char_index + key) % 26
            
            # Konversi kembali ke karakter
            new_char = chr(new_index + ord(start_char))
            result += new_char
        else:
            # Karakter selain huruf (spasi, angka, dll.) tidak diubah
            result += char
            
    return result

# --- Data Uji Coba ---
pesan_asli = "Saya sayang Rasya"
kunci_geser = 5 

# --- Simulasi Proses ---

# 1. ENKRIPSI
ciphertext = caesar_cipher(pesan_asli, kunci_geser, mode='enkripsi')

# 2. DEKRIPSI
pesan_dekripsi = caesar_cipher(ciphertext, kunci_geser, mode='dekripsi')

# --- Menampilkan Hasil (Tanpa Judul Simulasi) ---
print("=" * 40)
print(f"Pesan Asli (Plaintext): {pesan_asli}")
print(f"Kunci Rahasia (Key):    {kunci_geser}")
print("-" * 40)
print(f"Hasil Enkripsi (Ciphertext): {ciphertext}")
print("-" * 40)
print(f"Hasil Dekripsi: {pesan_dekripsi}")
print("=" * 40)