# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Rasya Islami Kautsar]  
NIM: [230202777]  
Kelas: [5IKRB]  

---

## 1. Tujuan

1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan. 

---

## 2. Dasar Teori

Analisis serangan kriptografi membahas berbagai cara penyerang mencoba melemahkan atau memecahkan sistem kriptografi tanpa mengetahui kunci rahasia. Secara umum, serangan dapat diklasifikasikan berdasarkan informasi yang dimiliki penyerang, seperti ciphertext-only attack, known-plaintext attack, dan chosen-plaintext/ciphertext attack. Semakin banyak informasi yang dimiliki penyerang, semakin besar peluang untuk menemukan kelemahan pada algoritma atau implementasinya.

Selain serangan berbasis teori matematika, terdapat pula serangan praktis seperti brute force attack dan side-channel attack. Brute force mencoba semua kemungkinan kunci hingga menemukan yang benar, sehingga dapat dicegah dengan penggunaan panjang kunci yang cukup besar. Side-channel attack memanfaatkan informasi fisik dari proses komputasi, seperti waktu eksekusi, konsumsi daya, atau pola elektromagnetik, yang sering kali muncul akibat kelemahan implementasi, bukan algoritmanya.

Oleh karena itu, analisis serangan kriptografi tidak hanya berfokus pada kekuatan algoritma, tetapi juga pada cara penerapannya dalam sistem nyata. Sistem kriptografi yang aman harus menggunakan algoritma standar yang telah diuji, panjang kunci yang memadai, serta implementasi yang benar untuk meminimalkan peluang terjadinya serangan.

---

## 3. Alat dan Bahan

- Python 3.x
- Visual Studio Code
- Git dan akun GitHub
- Google chrome
- Library tambahan (misalnya pycryptodome, jika diperlukan)

---

## 4. Langkah Percobaan

### Langkah 1 — Identifikasi Serangan
Kasus nyata: Serangan brute force pada hash MD5 (kebocoran database password)

Vaktor serangan:
Penyerang memperoleh database password hasil kebocoran (data breach) yang disimpan dalam bentuk hash MD5, lalu melakukan brute force atau dictionary attack secara offline menggunakan wordlist dan tools cracking.

Penyebab kelemahan:
MD5 merupakan algoritma hash yang sudah usang dan sangat cepat dihitung, sehingga memungkinkan penyerang mencoba jutaan password per detik. Selain itu, banyak sistem lama menggunakan MD5 tanpa salt, sehingga hash yang sama menghasilkan output yang sama dan mudah dicocokkan dengan tabel rainbow. Kombinasi algoritma lemah, tidak adanya salt, dan password pengguna yang sederhana membuat serangan ini sangat efektif.

### Langkah 2 — Evaluasi Kelemahan
Analisis kelemahan algoritma (MD5):
MD5 memiliki kelemahan mendasar pada algoritmanya, yaitu mudah mengalami collision dan sangat cepat dihitung. Kecepatan ini justru berbahaya untuk penyimpanan password karena memungkinkan brute force dan dictionary attack dilakukan secara efisien. Selain itu, MD5 sudah tidak lagi direkomendasikan untuk tujuan keamanan kriptografi.

Sumber kelemahan:
Kelemahan utama berada pada algoritma kriptografi itu sendiri karena MD5 sudah terbukti tidak aman. Namun, kerentanan semakin parah akibat implementasi dan konfigurasi sistem yang buruk, seperti penggunaan MD5 tanpa salt, tanpa key stretching, dan tanpa kebijakan password yang kuat. Jadi, kasus ini merupakan kombinasi kelemahan algoritma dan kesalahan implementasi.

### Langkah 3 — Rekomendasi Solusi

Algoritma MD5 sebaiknya diganti dengan SHA-256 untuk fungsi hashing.

Alasan dan dampak terhadap keamanan:
SHA-256 memiliki tingkat keamanan yang jauh lebih tinggi dibanding MD5 karena lebih tahan terhadap collision dan tidak mudah dipecahkan dengan brute force. Penggunaan SHA-256 meningkatkan keandalan proses hashing sehingga data lebih sulit dimanipulasi atau dipalsukan, serta memperkecil risiko kebocoran informasi akibat serangan kriptografi.

---

## 5. Source Code


---

## 6. Hasil dan Pembahasan

- **Pembahasan**

Berdasarkan hasil praktikum dan analisis yang telah dilakukan, dapat diketahui bahwa serangan brute force dan dictionary attack pada hash MD5 terjadi akibat penggunaan algoritma kriptografi yang sudah tidak lagi aman. MD5 memiliki kelemahan pada desain algoritmanya, terutama sifat collision dan kecepatan komputasi yang tinggi, sehingga memungkinkan penyerang melakukan percobaan password dalam jumlah besar secara efisien. Hal ini menunjukkan bahwa MD5 tidak lagi layak digunakan untuk pengamanan password dalam sistem informasi modern.

Selain kelemahan algoritma, faktor implementasi dan konfigurasi sistem juga berperan besar dalam meningkatkan risiko serangan. Penggunaan MD5 tanpa salt, tidak adanya mekanisme key stretching, serta kebijakan password yang lemah memperbesar peluang keberhasilan serangan. Oleh karena itu, keamanan sistem kriptografi harus memperhatikan pemilihan algoritma yang sesuai standar terkini, penerapan konfigurasi yang benar, dan pembaruan sistem secara berkala. Dengan menerapkan algoritma yang lebih kuat seperti SHA-256, tingkat keamanan sistem dapat ditingkatkan dan risiko kebocoran data dapat diminimalkan.

---

## 7. Jawaban Pertanyaan

1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?

Karena menggunakan algoritma hash yang lemah atau usang (seperti MD5/SHA-1) tanpa salt, tidak menerapkan pembatasan percobaan login, serta memiliki kebijakan password yang lemah. Selain itu, sistem lama jarang diperbarui karena keterbatasan biaya dan kompatibilitas, sementara pada saat sistem tersebut dibuat, kesadaran terhadap keamanan siber masih rendah sehingga aspek perlindungan password belum menjadi prioritas. 

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?  

Kelemahan algoritma adalah masalah yang berasal dari desain atau konsep dasar algoritma itu sendiri, sehingga tetap tidak aman meskipun diimplementasikan dengan benar (misalnya algoritma kriptografi yang sudah terbukti mudah dipecahkan). Sementara itu, kelemahan implementasi terjadi karena kesalahan dalam cara algoritma tersebut diterapkan, seperti konfigurasi yang salah, penggunaan parameter yang lemah, atau praktik pemrograman yang buruk, padahal algoritma dasarnya sebenarnya aman.

3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?

Menggunakan algoritma dan protokol yang direkomendasikan standar terbaru, menerapkan update dan patch keamanan secara rutin, serta melakukan audit dan uji keamanan berkala. Selain itu, penting menerapkan manajemen kunci yang baik, kebijakan password dan autentikasi kuat, serta memantau perkembangan ancaman dan kemajuan teknologi (seperti komputasi kuantum) agar sistem dapat segera dimigrasikan ke solusi kriptografi yang lebih aman saat diperlukan.

---

## 8. Kesimpulan

Berdasarkan analisis yang dilakukan, serangan brute force pada hash MD5 terjadi karena penggunaan algoritma kriptografi yang sudah usang dan implementasi sistem yang kurang aman. MD5 tidak lagi layak digunakan untuk penyimpanan password karena rentan terhadap collision dan brute force. Penggantian algoritma ke metode hashing yang lebih kuat seperti SHA-256 dapat meningkatkan keamanan sistem secara signifikan dan mengurangi risiko kebocoran data.

---

## 9. Daftar Pustaka

- Katz, J., & Lindell, Y. Introduction to Modern Cryptography. CRC Press.
- Stallings, W. Cryptography and Network Security: Principles and Practice. Pearson Education.
- Kahn Academy. Cryptographic Hash Functions.
- Panduan Praktikum Kriptografi Minggu ke-14: Analisis Serangan Kriptografi.

---

## 10. Commit Log

```
commit week14-analisis-serangan
Author: Rasya Islami Kautsar <rasyakautsar01@gmail.com>
Date:   2026-01-23

    week14-analisis-serangan: Analisis Serangan Kriptografi
```
