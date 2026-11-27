#!/bin/bash
#SBATCH --job-name=orthofinder3
#SBATCH --cpus-per-task=32
#SBATCH --mem=128G
#SBATCH --output=/home/cassandre/M2STAGE/log_output/slurm_out/slurm-%J.out
#SBATCH --error=/home/cassandre/M2STAGE/log_output/slurm_out/slurm-%J.err

module load singularity

singularity exec -B /data /biolo/orthofinder/orthofinder-3.0.1b1/orthofinder_3.0.1b1.sif \
  orthofinder \
  -f /data/cassandre/01_qfo_raw/fastas \
  -s /data/cassandre/01_qfo_raw/qfo_species_tree_fastaname.nwk \
  -t 32 \
  -o /data/cassandre/02_orthofinder_group