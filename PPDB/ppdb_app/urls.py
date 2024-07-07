from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('sekolah/', views.SekolahList.as_view()),
    path('sekolah/<int:pk>/', views.SekolahDetail.as_view()),
    path('jurusan/', views.JurusanList.as_view()),
    path('jurusan/<int:pk>/', views.JurusanDetail.as_view()),
    path('siswa/', views.SiswaList.as_view()),
    path('siswa/<int:pk>/', views.SiswaDetail.as_view()),
    path('pendaftaran/', views.PendaftaranList.as_view()),
    path('pendaftaran/<int:pk>/', views.PendaftaranDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)