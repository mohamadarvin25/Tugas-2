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
