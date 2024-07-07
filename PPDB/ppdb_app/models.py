from django.db import models

# Create your models here.
class Sekolah(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=255)
    telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class Jurusan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE, related_name='jurusan')

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    telepon = models.CharField(max_length=15)
    sekolah_tujuan = models.ForeignKey(Sekolah, on_delete=models.CASCADE, related_name='calon_siswa', null=True, blank=True)
    jurusan_tujuan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, related_name='calon_siswa', null=True, blank=True)

    def __str__(self):
        return self.nama

class Pendaftaran(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    tanggal_daftar = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.siswa.nama} - {self.sekolah.nama}: {self.status}"
