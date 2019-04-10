#!/usr/bin/env python3
# copyright (c) 2019 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

def main():
    import os
    import sys
    import gzip
    from argparse import ArgumentParser,FileType
    parser=ArgumentParser(description="list up the number of reads of all files in the directory.",usage="python3 list_reads.py -o output_file.txt dir [dir...]")
    parser.add_argument("dirs", nargs="+", type=str, help="directory names")
    parser.add_argument("-o", type=str, default=sys.stdout, help="output file")
    args = parser.parse_args()

    labels="sample"
    outs={}

    for dir in args.dirs:
        labels += "\t" + dir.split("/")[-1]
        files=os.listdir(dir)
        out={}
        for file in sorted(files):
#            smpl=file.split("_L001_R1_001")[0].split("_L001_R2_001")[0]
            smpl=file.split("_")[0]
            
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
                for line in faq:
                    ID=line.rstrip()
                    faqs[ID]=faq.readline()
                    faqs[ID]+=faq.readline()
                    faqs[ID]+=faq.readline()
            elif ftype=="fasta":
                for line in faq:
                    ID=line.rstrip()
                    faqs[ID]=faq.readline()
                    
            if smpl in out:
                out[smpl] += len(faqs)
            else:
                out[smpl] = len(faqs)

        for o in out:
            if smpl in outs:
                outs[o] += "\t" + str(out[o])
            else:
                outs[o] = str(out[o])


    output=labels+"\n"
    for out in sorted(outs.keys()):
        output+=out+"\t"+outs[out]+"\n"
    fhw=open(args.o,"w")
    fhw.write(output)
    fhw.close()
    
if __name__ == '__main__': main()

