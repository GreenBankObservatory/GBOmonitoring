import requests
import pandas as pd
from visualization.models import OSSData

def fetch_urls(url_selection):
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    urls = pd.read_csv('/home/sandboxes/gbosdd/oss/config/urls.csv')
    if url_selection == 'read':
        return_url = urls['read_url'][0]
    elif url_selection == 'write':
        return_url = urls['write_url'][0]
    else:
        response_url = None
        print('Invalid URL selection. Must pick \'read\' or \'write\'.')
    return return_url

def read_oss_db():
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    read_url = fetch_urls('read')
    try:
        response = requests.get(read_url, timeout=5).json()
    except requests.exceptions.Timeout:
        response = None
    except requests.exceptions.ConnectionError:
        response = None
    return response

def fill_oss_df():
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    oss_data = read_oss_db()

    pd_site_id = []
    pd_src_id = []
    pd_src_start_utc = []
    pd_src_end_utc = []
    pd_status = []
    pd_notes = []

    for li in oss_data['oss_data']:
        pd_site_id.append(li['site_id'])
        pd_src_id.append(li['src_id'])
        pd_src_start_utc.append(li['src_start_utc'][0:19])
        pd_src_end_utc.append(li['src_end_utc'][0:19])
        try:
            pd_status.append(li['status'])
        except:
            pd_status.append('-')
        pd_notes.append(li['notes'])

    live_df = pd.DataFrame({
        'pd_site_id':pd_site_id, 
        'pd_src_id':pd_src_id, 
        'pd_src_start_utc':pd_src_start_utc,
        'pd_src_end_utc':pd_src_end_utc,
        'pd_status':pd_status,
        'pd_notes':pd_notes
        })
    live_df['pd_src_start_utc'] = pd.to_datetime(live_df['pd_src_start_utc'])
    live_df['pd_src_end_utc'] = pd.to_datetime(live_df['pd_src_end_utc'])

    return live_df

def fill_oss_db():
    '''
    Fills a database with the current OSS information

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    oss_df = fill_oss_df()

    for i in range(len(oss_df['pd_site_id'])):
        OSSData.objects.create(
            site_id = oss_df['pd_site_id'][i],
            source_id = oss_df['pd_src_id'][i],
            start_time = oss_df['pd_src_start_utc'][i],
            end_time = oss_df['pd_src_end_utc'][i],
            notes = oss_df['pd_status'][i],
            status = oss_df['pd_notes'][i],
        )