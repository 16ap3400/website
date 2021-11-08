import io

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from google.colab import files
from pdb import set_trace as bp
def upload():
  print('Upload Content Image')
  file_dict = files.upload()
  file_path = io.BytesIO(file_dict[next(iter(file_dict))])
  return file_path

img_path = upload()
