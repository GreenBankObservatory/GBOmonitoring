import pandas as pd
from astropy.io import fits
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from tqdm import tqdm

def bintable2pandas(bintbl):
    df_dict = {}
    img_arr = []
    for c in bintbl.columns:
        df_dict[c.name] = list(bintbl.data[c.name])
        if c.name != 'DMJD':
            img_arr.append(list(bintbl.data[c.name]))
    img_arr = np.array(img_arr)
    df = pd.DataFrame(df_dict)
    return df, img_arr

def make_plot(img, fname):
    plt.imshow(img)
    plt.savefig(f'/home/sandboxes/vcatlett/repos/github/GBOmonitoring/dashboards/samplers/tmp/{fname}.png')
    plt.close()

def make_gif(img, win=100):
    img_len = np.shape(img)[1]
    n_steps = int(np.floor(img_len/win))
    ci = 0
    print("Plotting images...")
    for ni in tqdm(range(n_steps)):
        make_plot(img[:, ci:ci+win], ni)
        ci += win
    img_gif = []
    print("Saving to GIF...")
    for f in tqdm(glob('/home/sandboxes/vcatlett/repos/github/GBOmonitoring/dashboards/samplers/tmp/*.png')):
        img_gif.append(imageio.imread(f))
    imageio.mimsave('/home/sandboxes/vcatlett/repos/github/GBOmonitoring/dashboards/samplers/test.gif', img_gif)
    for f in tqdm(glob('/home/sandboxes/vcatlett/repos/github/GBOmonitoring/dashboards/samplers/tmp/*.png')):
        os.remove(f)

colnames = [c.split('/')[-1] for c in glob("/home/gbtlogs/*")]

ant_files = glob('/home/gbtlogs/Antenna-AntennaManager-azElData/*.fits*')
data = fits.open(ant_files[0])
df, img = bintable2pandas(data[1])
data.close()
make_gif(img)