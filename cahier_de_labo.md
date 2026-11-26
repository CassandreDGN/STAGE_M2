## 20-11-26

### 1. Workspace setup

- Created a link between home and data stored on pig and modified the .gitignore accordingly

### 2. Proteomes download

- Downloaded the proteomes for 81 species : 
```
wget -b -r -np -nd -A "*.fasta.gz" -R "*_DNA.fasta.gz,*_additional.fasta.gz" ftp://ftp.ebi.ac.uk/pub/databases/reference_proteomes/QfO/
```

## 23-11-26

- Generated 81 embeddings with `protT5_embedding.py`
    - Embeddings were generated using ProtT5-XL-Uniref50 with mean pooling.
    - Extracted protein-level embeddings (per_protein=True, per_residue=False) using batching (max_batch=100, max_residues=4000) and individual processing for sequences >1000 residues (max_seq_len=1000) to optimize GPU memory usage.


# 26-11-26

- Checked a few embeddings using `/home/cassandre/stage/Cassandre/M1_INTERNSHIP/Code/PHASE1_OUTLIERS/umap_outliers.py` to see if it made sense (it did)
- 



