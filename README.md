# neurodev_collab
Companion code for "Conserved and dynamic ESR1 signaling in developing cortex mediates  early postnatal social behavior" (Liu et al., 2024)
## Software requirements
- R 4.3.3
- Platform: x86_64-conda-linux-gnu (64-bit), CentOS Linux 7 (Core)
- Seurat 5.1.0
- Signac 1.13.0
- SeuratObject 5.0.2
- Azimuth 0.5.0
- GenomeInfoDb 1.38.8
- BSgenome.Mmusculus.UCSC.mm10_1.4.3
- EnsDb.Mmusculus.v79_2.99.0
- tidyverse 2.0.0
## Processing workflow

### Directories
1) **Cell Ranger ATAC pipeline** to generate ```fragments.tsv.gz``` files:
``` 
cellranger-atac count --id=$ID \
                      --reference=$REFERENCEPATH \
                      --fastqs=$FASTQPATH \
                      --sample=$SAMPLENAME
```
2) **```step1_qc/atac```**: ```.ipynb``` notebooks to process sample ```fragments.tsv.gz``` files (biological replicates E1, E2, V1, V2), yielding a Seurat object containing filtered nuclei (Version ```5.0.2```).
3) **```step2_merge```**: ```.ipynb``` notebooks to nerge E1, E2, V1, V2 objects (first E1+E2, V1+V2, then altogether), producing one merged Seurat object (E1+E2+V1+V2).
4) **```step3_chromvar```**: ```.ipynb``` notebook to perform ChromVAR analysis on the merged object from 3).