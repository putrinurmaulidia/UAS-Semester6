from rest_framework import serializers
from .models import Sekolah, Jurusan, Siswa, Pendaftaran

class SekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekolah
        fields = '__all__'

class JurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = '__all__'

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class PendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendaftaran
        fields = '__all__'
