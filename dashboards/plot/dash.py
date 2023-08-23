from bokeh.plotting import figure
from bokeh.embed import components

def plot_ts(x, y):
    plot = figure(plot_width=600, plot_height=400, title="ZtiltPos - Time Series")
    plot.line(x, y, color="navy", alpha=0.5)
    plot.xaxis.axis_label = 'DMJD'
    plot.yaxis.axis_label = 'ZtiltPos'
    script, div = components(plot)
    return script, div

def plot_fft_r(x, y):
    plot = figure(plot_width=600, plot_height=400, title="ZtiltPos - FFT (Real)")
    plot.line(x, y, color="navy", alpha=0.5)
    plot.xaxis.axis_label = 'DMJD'
    plot.yaxis.axis_label = 'ZtiltPos'
    script, div = components(plot)
    return script, div

def plot_fft_i(x, y):
    plot = figure(plot_width=600, plot_height=400, title="ZtiltPos - FFT (Imaginary)")
    plot.line(x, y, color="navy", alpha=0.5)
    plot.xaxis.axis_label = 'DMJD'
    plot.yaxis.axis_label = 'ZtiltPos'
    script, div = components(plot)
    return script, div