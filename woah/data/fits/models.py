from django.db import models


class FITS(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

class HDU(models.Model):
    fits_name = models.ForeignKey(FITS, on_delete=models.CASCADE)
    hdu_num = models.IntegerField()

class FITSHeader(models.model):
    fits_hdu = models.ForeignKey(HDU, on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    val = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)

class FITSData(models.model):
    fits_hdu = models.ForeignKey(HDU, on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    val = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    dtype = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)