from django.contrib import admin
from .models import Sekolah, Jurusan, Siswa, Pendaftaran

# Register your models here.
admin.site.register(Sekolah)
admin.site.register(Jurusan)
admin.site.register(Siswa)
admin.site.register(Pendaftaran)