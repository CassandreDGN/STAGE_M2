#!/home/cassandre/M2STAGE/conda/speciestree/bin/python
#SBATCH --job-name=speciestree
#SBATCH --output=/home/cassandre/M2STAGE/log_output/slurm_out/slurm-%J.out --error=/home/cassandre/M2STAGE/log_output/slurm_out/slurm-%J.err

from ete4 import NCBITaxa, PhyloTree
import pandas as pd

df = pd.read_csv('/data/cassandre/01_qfo_raw/qfo_metadata.tsv', sep='\t')
taxids = df['Tax_ID'].astype(int).tolist()

ncbi = NCBITaxa()
tree = ncbi.get_topology(taxids, intermediate_nodes=False)

euk_arch = PhyloTree()
for child in list(tree.children):
    first_leaf_taxid = int(next(child.leaves()).name)
    if 2 not in ncbi.get_lineage(first_leaf_taxid):
        euk_arch.add_child(child.detach())

tree.add_child(euk_arch)

tree.write(outfile='/data/cassandre/01_qfo_raw/qfo_species_tree.nwk', parser=1)

taxid_to_fastaname = dict(zip(df['Tax_ID'].astype(str), df["Proteome_ID"] + '_' + df["Tax_ID"].astype(str)))

for leaf in tree.leaves():
    leaf.name = taxid_to_fastaname[leaf.name]

tree.write(outfile='/data/cassandre/01_qfo_raw/qfo_species_tree_fastaname.nwk', parser=1)