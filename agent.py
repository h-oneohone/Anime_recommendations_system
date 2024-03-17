import numpy as np
import pandas as pd
import scipy
import os
import gdown
import zipfile

class Agent():
    def __init__(self, dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True):

        if not os.path.exists(dataset_path) and download_dataset:
            gdown.download('https://drive.google.com/uc?id=1UPHCJPnJ3DyN4exFDKo2R2_mWclRpuWx', 'dataset.zip', quiet=False)
            with zipfile.ZipFile('dataset.zip', 'r') as zip_ref:
                zip_ref.extractall(dataset_path)

        if not os.path.exists(weight_path) and download_weight:
            os.mkdir(weight_path)
            gdown.download('https://drive.google.com/uc?id=1guGze0nCE8i0JPOzlToW_CzBQhUk_2-x', weight_path + '/weight.npy', quiet=False)
            gdown.download('https://drive.google.com/uc?id=1a2V11vnThZjZrdfj9t7xXCPL65MyeK6h', weight_path + '/anime_index.npy', quiet=False)

        self.weight = np.load(weight_path + '/weight.npy')
        self.anime_index = np.load(weight_path + '/anime_index.npy')
        self.anime_df = pd.read_csv(dataset_path + '/anime.csv')
        self.anime_df = self.anime_df.loc[self.anime_df['MAL_ID'].isin(self.anime_index)]
        self.anime_df = self.anime_df.sort_values(by=['MAL_ID'])

    def act(self, id: int = None, name: str = None, k=10, return_df=False):
        if isinstance(id, int):
            index = self.anime_df[self.anime_df.MAL_ID == id].index[0]
        elif isinstance(name, str):
            index = self.anime_df[self.anime_df.Name == name].index[0]
        else: raise Exception('id or name arguments not suitable, type(id) is int or type(name) is str')

        index_res = (-self.weight[index]).argsort()[:k]

        if return_df: return self.anime_df.loc[index_res]

        if isinstance(id, int):
            return self.anime_df.loc[index_res].MAL_ID.tolist()
        return self.anime_df.loc[index_res].Name.tolist()
