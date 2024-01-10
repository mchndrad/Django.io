from django.db import models

class Userdb(models.Model):
    name = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=12, null=True)
    
    class Meta:
        db_table = 'dbuser'
# Create your models here.

class Booking(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    handphone = models.CharField(max_length=15)
    kota_tujuan = models.CharField(max_length=50)
    pemilihan_paket = models.CharField(max_length=50)
    paket = models.CharField(max_length=50)
    tanggal_keberangkatan = models.DateField()
    lokasi_anda = models.CharField(max_length=100)

    class Meta:
        db_table = 'booking'
