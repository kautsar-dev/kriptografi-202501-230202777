import hashlib
import time

# Coba import bcrypt dengan aman
try:
    import bcrypt
    BCRYPT_AVAILABLE = True
except ImportError:
    BCRYPT_AVAILABLE = False
    print("[!] Library bcrypt belum terpasang. Bagian bcrypt akan dilewati.")


# ================================
# BAGIAN 1: HASH PASSWORD (MD5)
# ================================
def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


# ================================
# BAGIAN 2: DICTIONARY ATTACK MD5
# ================================
def md5_dictionary_attack(target_hash, dictionary):
    print("\n[+] Memulai Dictionary Attack (MD5)")
    start = time.time()

    for word in dictionary:
        if hash_md5(word) == target_hash:
            end = time.time()
            print(f"[!] Password ditemukan: {word}")
            print(f"Waktu serangan: {end - start:.4f} detik")
            return word

    print("[!] Password tidak ditemukan")
    return None


# ================================
# BAGIAN 3: HASH PASSWORD AMAN (bcrypt)
# ================================
def hash_bcrypt(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def verify_bcrypt(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


# ================================
# SIMULASI STUDI KASUS
# ================================
if __name__ == "__main__":
    print("=== ANALISIS SERANGAN KRIPTOGRAFI ===")

    # Password asli (contoh sistem lama)
    real_password = "password123"

    # Hash MD5 (LEMAH)
    md5_hash = hash_md5(real_password)
    print("\n[MD5 HASH]")
    print("Password :", real_password)
    print("MD5 Hash :", md5_hash)

    # Dictionary sederhana
    wordlist = [
        "123456",
        "admin",
        "qwerty",
        "password",
        "password123",
        "letmein"
    ]

    # Serangan dictionary attack
    md5_dictionary_attack(md5_hash, wordlist)

    # ================================
    # SOLUSI AMAN
    # ================================
    if BCRYPT_AVAILABLE:
        print("\n==============================")
        print("SOLUSI: HASH AMAN DENGAN bcrypt")
        print("==============================")

        bcrypt_hash = hash_bcrypt(real_password)
        print("bcrypt Hash :", bcrypt_hash)

        # Verifikasi password
        check = verify_bcrypt("password123", bcrypt_hash)
        print("Verifikasi password benar:", check)

        check_false = verify_bcrypt("password_salah", bcrypt_hash)
        print("Verifikasi password salah:", check_false)
    else:
        print("\n[!] bcrypt tidak tersedia, bagian hash aman dilewati.")

    print("\n[SELESAI] Analisis serangan berhasil dijalankan.")
