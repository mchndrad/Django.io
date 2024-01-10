# Generated by Django 4.2.6 on 2024-01-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kerangka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nomor_handphone', models.CharField(max_length=15)),
                ('kota_tujuan', models.CharField(max_length=50)),
                ('pemilihan_paket', models.CharField(max_length=20)),
                ('paket', models.CharField(max_length=50)),
                ('tanggal_keberangkatan', models.DateField()),
                ('lokasi_anda', models.CharField(max_length=100)),
            ],
        ),
    ]
