import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
import umap # type: ignore

print("Let's go")
df = pd.read_csv('/ebio/abt1_share/prediction_hendecads/3_CLANS/nxnblast', sep='\t', header=None)
df.columns = ['i', 'j', 'score']

print("Start matrix")
# Create a matrix
matrix = np.zeros((df['i'].max()+1, df['j'].max()+1))

for i, j, score in df.values:
    matrix[int(i), int(j)] = score
    matrix[int(i), int(j)] = score

print("Matrix done")

# Standardize the matrix
scaler = StandardScaler()
matrix = scaler.fit_transform(matrix)
print("Scaler done")
# UMAP
print('UMAP')
reducer = umap.UMAP()
embedding = reducer.fit_transform(matrix)

# Plot
print('Plot')
plt.scatter(embedding[:, 0], embedding[:, 1], s=1)
plt.savefig('/ebio/abt1_share/prediction_hendecads/1_repo/1_seq_analysis/umap.png')
