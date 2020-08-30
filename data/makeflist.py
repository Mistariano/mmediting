import cv2
import glob
from tqdm import tqdm
import os
base_dir = 'DIV2K/DIV2K_train_HR'
meta_fname = 'DIV2K_meta_info_DIV2K800sub_GT.txt'


flist = glob.glob(base_dir+'/*.png')

print(flist)

with open(meta_fname, 'w') as f:
    for fpath in tqdm(flist):
        img = cv2.imread(fpath)
        if img is None:
            print('None:', fpath)
            continue
        size = img.shape
        fname = os.path.split(fpath)[-1]
        print(fname)
        line = f"{fname} {size}\n"
        f.write(line)

