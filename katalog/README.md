##  JAWABAN TUGAS 2
Mohamad Arvin Fadriansyah - 2006596996
 ---
### Pertanyaan 1
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
### Answer
<img src="https://i.postimg.cc/0yVmLg02/Screenshot-2022-09-15-071007.png" width="300" height="300">  <img src="https://i.postimg.cc/sXdpJYJp/Screenshot-2022-09-15-073207.png" width="500" height="300">
![urls.py, views.py, models.py, dan berkas htm ](https://i.postimg.cc/sXdpJYJp/Screenshot-2022-09-15-073207.png | width=100)

1. Client/ User akan meinta request melalui Internet berupa HTTP request
2. HTTP request akan masuk ke urls.py yang ada di django
3. urls.py yang ada di project_django akan meminta request ke urls.py yang ada di katalog
4. urls.py yang ada di katalog akan meminta tampilan kepada views.py
5. views.py akan meminta format penampilan kepada berkas html
6. berkas html akan meminta input data dari views.py
7. views.py akan meminta data dari models.py
8. models.py meminta data dari database
9. data dari databse diolah / dimodelkan  oleh model agar bisa digunakan oleh html
10. views.py akan menampilan HTTP response
---
### Pertanyaan 2
Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
### Answer
Alasan kita menggunakan virtual environment adalah proyek yang kita kerjakan bisa saja menggunakan external library yang berbeda dari yang ada di server atau komputer lain atau komputer kita pribadi.Misal project meminta django versi 3.8 untuk digunakan tetapi kita mengerjakan suatu proyek menggunakan django versi 4.1. Sementara teman kita yang juga mengerjakan project sama bagian yang lain menggunakan versi 3.6 agar kedua belah pihak bisa mengerjakan proyek yang sama dengan versi yang berbeda maka keduanya dapat menggunakan virtual environment. Kita bisa saja tidak menggunakan virtual environment. kita bisa saja tidak menggunakan virtual environment jika versi external library kita telah bersesuaian sama depedency yang diperlukan pada proyek tersebut.
