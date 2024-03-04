import gdown
import zipfile

dataset_path = 'dataset'
gdown.download('https://drive.google.com/uc?id=1UPHCJPnJ3DyN4exFDKo2R2_mWclRpuWx', 'dataset.zip', quiet=False)
url = 'https://drive.google.com/uc?id=1_xbWxVDFCe_j7xd7XyfB-MTpAytZIBoU'
gdown.download('https://drive.google.com/uc?id=1_xbWxVDFCe_j7xd7XyfB-MTpAytZIBoU', 'weight.h5', quiet=False)
with zipfile.ZipFile('dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(dataset_path)
