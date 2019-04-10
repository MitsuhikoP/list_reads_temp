#!/usr/bin/env python3
# copyright (c) 2019 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

def main():
    import os
    import sys
    import gzip
    import re
    from argparse import ArgumentParser,FileType
    parser=ArgumentParser(description="list up the number of reads of all files in the directory.",usage="python3 list_reads.py -o output_file.txt dir [dir...]")
    parser.add_argument("dirs", nargs="+", type=str, metavar="str", help="directory names")
    parser.add_argument("-o", type=FileType("w"), default=sys.stdout, help="output file name (default: stdout)")
    
    args = parser.parse_args()

    labels="sample"
    outs={}

    for dir in args.dirs:
        labels += "\t" + dir
        files=os.listdir(dir)
        out={}
        for file in sorted(files):
            smpl=file.split(".")[0]
            smpl=re.split("_S\d+_L001_R[12]_001", file)[0]
            
            faq=""
            ftype=""
            if file.endswith(".fastq.gz") or file.endswith(".fq.gz"):
                faq = gzip.open(dir+"/"+file,"rt")
                ftype="fastq"
            elif file.endswith(".fastq") or file.endswith(".fq"):
                faq = open(dir+"/"+file,"r")
                ftype="fastq"
            elif file.endswith(".fasta.gz"):
                faq = gzip.open(dir+"/"+file,"rt")
                ftype="fasta"
            elif file.endswith(".fasta"):
                faq = open(dir+"/"+file,"r")
                ftype="fasta"
            faqs={}
            ID=""
            if ftype=="fastq":
                ls, mod = divmod(len(faq.readlines()),4)
                if mod != 0:
                    print(file, "is illegal line numbers.")
                    sys.exit(1)
            elif ftype=="fasta":
                ls, mod = divmod(len(faq.readlines()),2)
                if mod != 0:
                    print(file, "is illegal line numbers.")
                    sys.exit(1)
                    
            if smpl in out:
                out[smpl] += ls
            else:
                out[smpl] = ls

        for o in out:
            if smpl in outs:
                outs[o] += "\t" + str(out[o])
            else:
                outs[o] = str(out[o])


    output=labels+"\n"
    for out in sorted(outs.keys()):
        output+=out+"\t"+outs[out]+"\n"
    fhw=args.o
    fhw.write(output)
    fhw.close()
    
if __name__ == '__main__': main()
