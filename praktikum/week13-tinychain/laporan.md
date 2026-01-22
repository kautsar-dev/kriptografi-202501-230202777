# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Rasya Islami Kautsar]  
NIM: [230202777]  
Kelas: [5IKRB]  

---

## 1. Tujuan

1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori

TinyChain – Proof of Work (PoW) adalah mekanisme sederhana untuk memastikan bahwa setiap blok dalam blockchain dibuat secara sah. Setiap blok harus memiliki hash yang memenuhi aturan tertentu, misalnya diawali dengan beberapa nol. Untuk mendapatkannya, sistem mencoba berbagai nilai (nonce) hingga menemukan hash yang sesuai, sehingga pembuatan blok membutuhkan usaha komputasi.

PoW pada TinyChain berfungsi menjaga keutuhan data. Jika isi satu blok diubah, maka nilai hash-nya juga berubah dan blok tersebut menjadi tidak valid. Hal ini menyebabkan keterkaitan dengan blok berikutnya rusak, sehingga perubahan data tidak bisa dilakukan dengan mudah.

Secara teori, keamanan PoW berasal dari sifat fungsi hash yang sulit ditebak dan satu arah. Semakin sulit aturan hash yang ditetapkan, semakin besar usaha komputasi yang dibutuhkan. Meskipun TinyChain berskala kecil dan bersifat edukatif, konsep PoW ini tetap menggambarkan cara blockchain menjaga integritas dan keamanan data.

---

## 3. Alat dan Bahan

- Python 3.x
- Visual Studio Code
- Git dan akun GitHub
- Google chrome
- Library tambahan (misalnya pycryptodome, jika diperlukan)

---

## 4. Langkah Percobaan

1. Membuat file tinychain.py di folder praktikum/week13-tinychain/src/.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah python tinychain.py
4. Mengerjakan laporan.md
5. Membuat file hasil.png di folder praktikum/week13-tinychain/sreenshoot/
6. Mengupload hasil praktikum di dalam folder tersebut.

---

## 5. Source Code
### Langkah 1 dan 2 — Membuat Blokchain
```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
```

**Hasil uji coba (Output program)**
```
Mining block 1...
Block mined: 0000036e345420a41d942bdc0079a78880339d9f8354be03a30b44054746735c
Mining block 2...
Block mined: 0000dd4ec208cec73117e23dc0e9a719bb0366dc9f4bf929e0207a7aac30ec12
```

### Langkah 3 — Analisis Proof of Work

Berdasarkan hasil eksekusi program, setiap blok harus melewati proses mining sebelum dapat dimasukkan ke dalam blockchain. Proses ini menggunakan mekanisme Proof of Work (PoW), yaitu mencari nilai nonce yang menghasilkan hash dengan awalan nol sesuai tingkat difficulty yang ditetapkan (dalam program ini bernilai 4).

Output program memperlihatkan bahwa hash blok yang berhasil selalu diawali dengan “0000”. Hal ini menunjukkan bahwa sistem melakukan perhitungan hash berulang kali hingga menemukan nilai yang memenuhi kriteria. Semakin tinggi difficulty, semakin banyak percobaan yang dibutuhkan sehingga waktu mining menjadi lebih lama.

Penerapan PoW membuat blockchain lebih aman karena perubahan pada satu blok akan mengubah hash dan mengharuskan penambangan ulang blok-blok berikutnya. Dengan demikian, manipulasi data menjadi sulit dilakukan dan integritas blockchain tetap terjaga, seperti terlihat pada proses mining blok 1 dan blok 2.

---

## 6. Hasil dan Pembahasan

- **Hasil eksekusi Langkah 1 dan 2 — Membuat blokchain**
![Hasil Eksekusi](screenshots/tinychain.png)

- **Pembahasan**

Pada percobaan ini dibuat sebuah blockchain sederhana menggunakan Python dan fungsi hash SHA-256. Setiap blok berisi data, timestamp, previous hash, dan nonce, serta diawali dengan genesis block sebagai blok pertama.

Penambahan blok dilakukan melalui proses mining menggunakan Proof of Work (PoW). Sistem mencari nilai nonce hingga menghasilkan hash yang sesuai dengan tingkat difficulty, yang ditunjukkan oleh hash berawalan “0000”.

Percobaan ini menunjukkan bahwa keterkaitan antarblok dan proses PoW menjaga keutuhan data. Perubahan pada satu blok akan mengubah hash dan membuat blockchain tidak valid, sehingga konsep dasar keamanan blockchain dapat dipahami dengan jelas.

---

## 7. Jawaban Pertanyaan

1. Mengapa fungsi hash sangat penting dalam blockchain?

Karena berfungsi untuk menjaga keaslian dan keutuhan data. Setiap blok memiliki hash unik yang akan berubah jika data di dalam blok diubah, sehingga manipulasi data dapat langsung diketahui.

Selain itu, hash digunakan untuk menghubungkan satu blok dengan blok sebelumnya. Jika satu blok diubah, maka semua blok setelahnya menjadi tidak valid. Fungsi hash juga menjadi dasar mekanisme keamanan seperti Proof of Work, yang membuat pembuatan blok membutuhkan usaha komputasi dan tidak mudah dipalsukan.

2. Bagaimana Proof of Work mencegah double spending? 

Dengan memastikan bahwa setiap transaksi hanya bisa dicatat satu kali dalam blockchain yang sah. Untuk memasukkan transaksi ke dalam blok, penambang harus melakukan proses mining yang membutuhkan usaha komputasi. Jika ada yang mencoba menggunakan aset yang sama dua kali, ia harus menambang ulang blok dan mengalahkan rantai yang sudah ada, yang memerlukan biaya dan waktu sangat besar. Karena itu, upaya double spending menjadi sulit dan tidak efektif.

3. Apa kelemahan dari PoW dalam hal efisiensi energi?

Kebutuhan daya komputasi yang sangat besar. Proses mining mengharuskan banyak percobaan hash secara terus-menerus untuk menemukan nilai yang sesuai, sehingga mengonsumsi listrik dalam jumlah tinggi. Sebagian besar energi tersebut sebenarnya terbuang karena hanya satu penambang yang berhasil, sementara usaha penambang lain tidak digunakan. Akibatnya, PoW dianggap boros energi dan kurang ramah lingkungan, terutama jika diterapkan dalam skala besar.

---

## 8. Kesimpulan

Berdasarkan percobaan yang dilakukan, dapat disimpulkan bahwa mekanisme Proof of Work (PoW) pada TinyChain berhasil mensimulasikan proses pembuatan blok dalam blockchain. Setiap blok harus melalui proses mining untuk menghasilkan hash yang sesuai dengan tingkat difficulty yang ditentukan. Selain itu, penggunaan fungsi hash terbukti menjaga integritas data karena perubahan pada satu blok akan memengaruhi seluruh rantai blok, sehingga manipulasi data menjadi sulit dilakukan.

---

## 9. Daftar Pustaka

- Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System.
- Antonopoulos, A. M. (2017). Mastering Bitcoin: Programming the Open Blockchain. O’Reilly Media.
- Paar, C., & Pelzl, J. (2010). Understanding Cryptography: A Textbook for Students and Practitioners. Springer.
- Kahn Academy. (n.d.). Cryptographic Hash Functions.
- Panduan Praktikum Kriptografi Minggu ke-13: TinyChain – Proof of Work (PoW).

---

## 10. Commit Log

```
commit week13-tinychain
Author: Rasya Islami Kautsar <rasyakautsar01@gmail.com>
Date:   2026-01-22

    week13-tinychain: TinyChain – Proof of Work (PoW) 
```
