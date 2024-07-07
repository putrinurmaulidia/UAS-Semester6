from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Sekolah, Jurusan, Siswa, Pendaftaran
from .serializers import SekolahSerializer, JurusanSerializer, SiswaSerializer, PendaftaranSerializer

# view untuk sekolah dengan class base view
class SekolahList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        sekolah = Sekolah.objects.all()
        serializer = SekolahSerializer(sekolah, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SekolahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SekolahDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Sekolah.objects.get(pk=pk)
        except Sekolah.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        sekolah = self.get_object(pk)
        serializer = SekolahSerializer(sekolah)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        sekolah = self.get_object(pk)
        serializer = SekolahSerializer(sekolah, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        sekolah = self.get_object(pk=pk)
        sekolah.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk jurusan dengan class base view
class JurusanList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        jurusan = Jurusan.objects.all()
        serializer = JurusanSerializer(jurusan, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JurusanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JurusanDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Jurusan.objects.get(pk=pk)
        except Jurusan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        jurusan = self.get_object(pk)
        serializer = JurusanSerializer(jurusan)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        jurusan = self.get_object(pk)
        serializer = JurusanSerializer(jurusan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        jurusan = self.get_object(pk=pk)
        jurusan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view untuk siswa dengan class base view
class SiswaList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        siswa = Siswa.objects.all()
        serializer = SiswaSerializer(siswa, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiswaDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Siswa.objects.get(pk=pk)
        except Siswa.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = SiswaSerializer(siswa)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = SiswaSerializer(siswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        siswa = self.get_object(pk=pk)
        siswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# view untuk pendaftaran dengan class base view
class PendaftaranList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        pendaftaran = Pendaftaran.objects.all()
        serializer = PendaftaranSerializer(pendaftaran, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PendaftaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PendaftaranDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Pendaftaran.objects.get(pk=pk)
        except Pendaftaran.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        pendaftaran = self.get_object(pk)
        serializer = PendaftaranSerializer(pendaftaran)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        pendaftaran = self.get_object(pk)
        serializer = PendaftaranSerializer(pendaftaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pendaftaran = self.get_object(pk=pk)
        pendaftaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)