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
    site_id = models.TextField(verbose_name="Site ID")
    source_id = models.TextField(verbose_name="Source ID")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(verbose_name="Notes")
    status = models.TextField(verbose_name="Status")

    class Meta:
        managed = False
        db_table = "oss_data"
