from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from dashboards.plot.dash import *
#from dashboards.tables import OSSTable
from dashboards.oss.core import *

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the dashboards home page")

def ZtiltPos(request):
    ptitle = 'ZtiltPos'
    data = pd.read_csv('/home/sandboxes/vcatlett/repos/local/ztilt-dashboard/ztilt/data/ZtiltPos-147-archive.csv')
    data = data.sort_values(by="DMJD")
    script_ts, div_ts = plot_ts(data['DMJD'], data['ZtiltPos'])
    script_fft_r, div_fft_r = plot_fft_r(data['DMJD'], data['ZtiltPos'])
    script_fft_i, div_fft_i = plot_fft_i(data['DMJD'], data['ZtiltPos'])

    dash_dict = {
        'ptitle':ptitle, 
        'script_ts': script_ts, 
        'div_ts': div_ts,
        'script_fft_r': script_fft_r, 
        'div_fft_r': div_fft_r,
        'script_fft_i': script_fft_i, 
        'div_fft_i': div_fft_i
        }
    return render(request, 'dashboards/ztilt.html', dash_dict)

def OSS(request):
    #fill_oss_db()

    ptitle = 'OSS'
    #data_table = OSSTable()

    dash_dict = {
        'ptitle':ptitle, 
        #'table': data_table, 
        }

    return render(request, 'dashboards/oss.html', dash_dict)