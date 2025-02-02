# Generated by Django 5.0.3 on 2024-06-11 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppdb_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='sekolah_tujuan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calon_siswa', to='ppdb_app.sekolah'),
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurusan', to='ppdb_app.sekolah')),
            ],
        ),
        migrations.AddField(
            model_name='siswa',
            name='jurusan_tujuan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calon_siswa', to='ppdb_app.jurusan'),
        ),
    ]
