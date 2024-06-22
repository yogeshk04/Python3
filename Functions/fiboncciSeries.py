import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())

df.head()
