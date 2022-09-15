##  JAWABAN TUGAS 2
Mohamad Arvin Fadriansyah - 2006596996
 ---
### Pertanyaan 1
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
### Answer
<img src="https://i.postimg.cc/0yVmLg02/Screenshot-2022-09-15-071007.png" width="300" height="300">  <img src="https://i.postimg.cc/sXdpJYJp/Screenshot-2022-09-15-073207.png" width="500" height="300">

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

---
### Pertanyaan 3
Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
### Answer
1. Masuk ke https://github.com/pbp-fasilkom-ui/assignment-repository dan pilih aksi Use this template. Kamu akan dialihkan ke suatu halaman untuk membuat repositori baru dengan template yang sama seperti repositori template Django.
2. Masukkan nama repositori sesuai dengan keinginanmu. Pastikan repositori kamu bersifat public sehingga nantinya dapat diperiksa oleh asisten dosen. Bagian Include all branches tidak perlu dicentang.
3. Clone repositori baru tersebut ke komputer dengan perintah git clone `<URL_REPOSITORI>` dengan keterangan `<URL_REPOSITORI>` disesuaikan dengan tautan repositori yang baru saja kamu buat.
4. Masuk ke dalam repositori yang sudah kamu clone di komputermu dan buatlah sebuah virtual environment dengan perintah berikut.
```
python -m venv env
``` 
5. Nyalakan virtual environment dengan perintah yang sesuai dengan jenis operating system yang kamu gunakan.
```
Windows:
env\Scripts\activate.bat
``` 
6. Install dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah `pip install -r requirements.txt`.
7. Coba jalankan proyek Django yang telah kamu buat dengan perintah python manage.py runserver dan bukalah http://localhost:8000 di browser favoritmu untuk mengetes apakah proyek Django dapat berjalan dengan baik.
8. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
9. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
10. Jalankan perintah `python manage.py loaddata initial_catalog_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.
11. Buka `views.py` yang ada pada folder `katalog` dan buatlah sebuah fungsi yang menerima parameter request dan mengembalikan `render(request, "katalog.html")`. Contohnya adalah sebagai berikut.
```
def show_wishlist(request):
    return render(request, "katalog.html")
```
12. Isi berkas di dalam folder aplikasi `katalog` bernama `urls.py` untuk melakukan routing terhadap fungsi `views` yang telah kamu buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser-mu. Isi dari `urls.py` tersebut adalah sebagai berikut.
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
13. Daftarkan juga aplikasi `katalog` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`.
```
...
path('katalog/', include('katalog.urls')),
...
```
14. Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah http://localhost:8000/katalog/ di browser favoritmu untuk melihat halaman yang sudah kamu buat
15. Pada fungsi views yang telah kamu buat, import models yang sudah kamu buat sebelumnya ke dalam file `views.py`. Kamu akan menggunakan class tersebut untuk melakukan pengambilan data dari database. Contohnya adalah sebagai berikut.
```
from django.shortcuts import render
from katalog.models import CatalogItem
...
```
16. Tambahkan potongan kode di bawah ini ke dalam fungsi `show_katalog` yang sudah kamu buat sebelumnya. Potongan kode ini berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
```
data_catalog_item = CatalogItem.objects.all()
context = {
    'list_barang': data_catalog_item,
    'nama' : 'Mohamad Arvin Fadriasnyah',
    'id'   : '2006596996'

}
```
17.Tambahkan `context` sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah kamu buat sebelumnya. Data yang ada pada variabel `context` tersebut akan ikut di-render oleh Django sehingga nantinya kamu dapat memunculkan data tersebut pada halaman HTML.
```
return render(request, "katalog.html",context)
```
18. Ubah Fill me! yang ada di dalam HTML tag `<p>` menjadi `{{nama}}` dan `{{id}}` untuk menampilkan nama kamu di halaman HTML. Contohnya adalah sebagai berikut.
```
...
<h5>Name: </h5>
<p>{{nama}}</p>

<h5>Student ID: </h5>
<p>{{id}}</p>
...
```
19. Untuk menampilkan daftar barang ke dalam tabel, kamu perlu melakukan iterasi terhadap variabel `list_barang` yang telah kamu ikut render ke dalam HTML. Perhatikan bahwa kamu tidak dapat memanggil daftar barang tersebut secara langsung seperti yang kamu lakukan pada langkah 2 sebab variabel `list_barang` merupakan sebuah kontainer yang berisikan objek. Kamu juga perlu memanggil nama variabel/atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut. Contohnya adalah sebagai berikut.
```
...
{% comment %} Add the data below this line {% endcomment %}
    {% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.item_rating}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
{% endfor %}
...
```
20. Salin API Key dari akun kamu. API Key dapat kamu temukan di Account Settings -> API Key. Simpanlah API Key beserta informasi tentang aplikasi Heroku kamu pada file teks dengan format berikut:
```
HEROKU_API_KEY: d234262b-75d8-4041-8bc0-656031d3a405
HEROKU_APP_NAME: tugas-2-pbp
```
21. Tambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang akan kamu buat dapat kamu ambil dari informasi yang kamu catat pada file teks sebelumnya. Contohnya adalah sebagai berikut.
```
(NAME)HEROKU_APP_NAME
(VALUE)APLIKASI-SAYA
``` 
22. Simpan variabel-variabel tersebut.
23. Bukalah tab GitHub Actions dan jalankan kembali workflow yang gagal. 

Setelah workflow kamu jalankan kembali dan status deployment menjadi sukses (dapat kamu lihat terdapat simbol centang hijau pada repositori kamu), kamu dapat mengakses aplikasi milikmu di `https://tugas-2-pbp.herokuapp.com.` Selamat! Sekarang aplikasi Django milikmu dapat diakses di Internet.



