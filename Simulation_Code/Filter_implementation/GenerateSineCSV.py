import pandas as pd
from scipy.fft import fft, fftfreq,ifft
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from pathlib import Path




sin_W = 5* np.sin(np.linspace(0, 100, 5000))
t = np.linspace(0, 1, 5000)

df = pd.DataFrame({"t":t , "x": sin_W })

csv_path = (Path(__file__).parent.parent.parent) / "Data" / "SINCSV.csv"

df.to_csv(csv_path, index = False)