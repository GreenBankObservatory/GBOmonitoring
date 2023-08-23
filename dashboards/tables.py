from dashboards.models import OSSData
from table import Table
from table.columns import Column

class OSSTable(Table):
    site_id = Column(field='site_id') 
    source_id = Column(field='source_id') 
    start_time = Column(field='start_time') 
    end_time = Column(field='end_time') 
    notes = Column(field='notes') 
    status = Column(field='status') 
    class Meta:
        model = OSSData