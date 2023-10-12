from django.db import models

class OSSData(models.Model):
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    obs_id = models.IntegerField(verbose_name="Obs ID")
    site_id = models.TextField(verbose_name="Site ID")
    src_id = models.TextField(verbose_name="Source ID")
    src_start_utc = models.DateTimeField("Start Time")
    src_end_utc = models.DateTimeField("End Time")
    src_ra_deg_j2000 = models.FloatField(verbose_name="RA")
    src_dec_deg_j2000 = models.FloatField(verbose_name="Dec")

    class Meta:
        managed = False
        db_table = "oss"
        app_label = "dashboards"

    def __str__(self):
        return self.src_id

class ZtiltData(models.Model):
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    ztilt_id = models.IntegerField(verbose_name="Ztilt ID")
    t = models.DateTimeField("Timestamp")
    sampler_value = models.FloatField(verbose_name="Sampler Value")

    class Meta:
        managed = False
        db_table = "ztilt"
        app_label = "dashboards"

    def __str__(self):
        return f"{self.t}"