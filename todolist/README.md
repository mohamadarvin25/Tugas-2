# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Tautan tugas 4 ada [di sini](https://sleepy-crag-41411.herokuapp.com/todolist).

## Kegunaaan `{% csrf_token %}` pada elemen `<form>`
CSRF adalah singkatan dari *Cross Site Request Forgery*, semacam *attack* yang memaksa pengguna *end user* untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka sudah terautentikasi di aplikasi web tersebut. Contoh kasusnya adalah apabila seorang *developer* membuat penghapusan akun suatu aplikasi tertentu dapat dilakukan melalui GET (seharusnya POST), maka bisa jadi ada orang mengirim sesuatu di aplikasi web kita (asumsi: aplikasi tersebut punya beberapa mekanisme untuk meninggalkan *feedback*) seperti ini:
```
Anda ingin kaya raya. Lihat gambar keren ini!
<img src='http://tugas2-pbp-afiq.herokuapp.com/ingin_kaya_raya_tapi_isinya_buat_ngapus_akun"/>
```
dengan setiap orang/akun yang mengklik gambar di atas, maka akun mereka akan terhapus. Apabila misalnya *malicious attack* ini dilakukan via POST dan bukan GET, bisa saja seseorang membuat *form* yang meminta data-data akun mereka lalu melakukan peretasan.

Apabila kita menggunakan CSRF token, hal semacam ini tidak mungkin terjadi.

## Apakah kita dapat membuat elemen `<form>` secara manual?
Bisa. Kita dapat membuat *form* secara manual melalui HTML dengan memanfaatkan atribut dari `<input>`. Konteks atribut dalam tugas ini adalah atribut `name`. *Value* dari `name` ini bisa diakses menggunakan `request.POST[name]`. Dengan demikian, masukan dari *user* pada *form* yang kita punya dapat diperoleh tanpa menggunakan *generator*.

## Proses alur data dari submisi yang dilakukan oleh pengguna melalui `HTML` *form*
Saat pengguna men-*submit* *task* pada *form* di halaman `create_task`, data akan dikirimkan via *request* POST dan diterima di fungsi `create_task` yang sudah dibuat di *views.py*. Di fungsi tersebut masukan dari *user* diproses dan ditmapung di variabel penampung lalu setelah itu disimpan di *database* menggunakan method `save()`.

## Implementasi pada *checklist*
Pertama, buat app Django baru dengan perintah `startapp` kemudian tambahkan aplikasi **todolist** ini ke INSTALLED_APPS di `settings.py`. Buat model di `models.py` sesuai dengan spesifikasi yang diminta soal lalu lakukan migrasi. 

Kedua, membuat halaman login, registrasi, dan logout sesuai yang ada di perintah lab 3. Lalu dibuat juga halaman create_task yang berisi form yang bersesuaian dengan fungsi create_task yang menerima argumen request dan id di `views.py`. Buat routing di `urls.py` untuk mengarahkan halaman-halaman tadi ke tautan yang sesuai.

Terakhir, melakukan add, commit, dan push ke GitHub kemudian membuat dua `user` dan tiga *dummy data* di kedua user tersebut. 

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework
## Perbedaan Inline, Internal, dan External CSS
- Inline: Ditulis langsung di atribut HTML-nya. Kelebihannya kita dapat melihat langsung perubahan styling tapi kekurangannya tidak efisien sebab hanya mengatur 1 elemen saja tiap kita menulis *inline* pada atribut HTML.
- Internal: Ditulis di bagian header dengan tag `<style>....</style>`. Cocok untuk halaman yang memerlukan styling yang berbeda-beda. Apabila ingin membuat CSS yang global untuk semua halaman, cara ini tidak efisien sebab hanya mengatur satu file HTML saja.
- External: Ditulis terpisah dari HTML dan di-import di bagian header. Kelebihannya kita bisa langsung mengatur semua elemen HTML kita untuk halaman yang banyak, tapi kalau mau mengatur CSS secara khusus untuk tiap halaman cara ini menjadi tidak efektif.

## Jelaskan tag HTML5 yang kamu ketahui
Ada banyak tag HTML5. Menurut saya, yang paling penting untuk dipahami adalah:
- `div`: menspesifikasikan section dalam dokumen HTML
- `img`: merepresentasikan gambar
- `input`: mendefinisikan input control
- `nav`: merepresentasikan suatu navigation bar
- `textarea`: mendefinisikan input multi-line
- `ul`: mendefinisikan unordered list
- `ol`: mendefinisikan ordered list
- `a`: mendefinisikan hyperlink

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- *selector tag*: digunakan untuk melakukan styling pada elemen berdasarkan nama tag-nya.
- *selector class*: digunakan untuk melakukan styling pada elemen berdasarkan nama class. Cara membuatnya adalah dengan memberi imbuhan titik di depan nama classnya. 
- *selector ID*: mirip dengan selector class tapi dalam konteks ini ID bersifat unik (hanya bisa digunakan pada 1 elemen saja). Cara membuatnya adalah dengan memberi imbuhan tanda pagar di depan nama classnya.
- *selector attribute*: digunakan untuk melakukan styling elemen berdasarkan atribut-atribut yang dimiliki elemen tersebut. 
- *selector universal*: digunakan untuk melakukan styling semua elemen pada HTML (scope-nya global). 

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
1. Meng-*import* Bootstrap ke dalam `base.html`
2. Menambahkan wrapper (pembungkus) yang telah didefinisikan Bootstrap ke setiap halaman (`register.html`, `create_task.html`, dll)
3. Melakukan *styling* seperlunya
4. Menambahkan desain *cards* pada setiap iterasi task yang ada pada *todolist*.
 
