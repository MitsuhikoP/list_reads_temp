# list_reads
list up the number of reads of all files in the directory.

## Dependency
- python3
- R
- ggplot2
- tidyr

If you don't install these R packages, they are automatically installed.

## Usage
```
python3 list_reads.py [-o output_root] [-s float] dir [dir...]
```
Put list_reads.r on the same directory with list_reads.py

`-o output_root` Output file name. output_root.txt and output_root.pdf. Default is MIGreads.

`-s float` file size of output_root.pdf. Default is 7. When you use many samples and see sample name, overlap of sample names are  avoided by large size PDF (but same font size).

