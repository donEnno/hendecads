import pandas as pd 
from Bio import SeqIO
from deepcoil import DeepCoil

data = '/ebio/abt1_share/prediction_hendecads/data/new_prot_fam_data/stretches.fasta'

inp = {str(entriy.description): str(entriy.seq) for entriy in SeqIO.parse(data, 'fasta')}
inp_ = {k: inp[k] for k in list(inp)[:1000]}

dc = DeepCoil(use_gpu=False)

result_df = pd.DataFrame(columns=['id', 'sequence', 'cc', 'hept'])

CHUNK = 1000

for i in range(0, len(inp), CHUNK):
    print(f"Processing sequences {i+1}-{min(i+CHUNK, len(inp))}", end='\r')

    tmp_keys = list(inp.keys())[i:i+CHUNK]
    tmp_inp = {k: inp[k] for k in tmp_keys}

    preds = dc.predict(tmp_inp)
    
    for k in tmp_keys:
        result_df = result_df.append({'id': k, 'sequence': inp[k], 'cc': preds[k]['cc'], 'hept': preds[k]['hept']}, ignore_index=True)

result_df.to_csv('/ebio/abt1_share/prediction_hendecads/repo/deepcoil_analysis/deepcoil_results.csv', index=False)