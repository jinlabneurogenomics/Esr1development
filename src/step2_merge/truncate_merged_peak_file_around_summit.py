import pandas as pd
import argparse

# NOTE: be sure to set this to the correct value for your species of interest.
num_autosomes = 19    # mouse

def parse_args():
    parser=argparse.ArgumentParser("truncated a narrowPeak file to specified interval around summit")
    parser.add_argument("--input_bed")
    parser.add_argument("--summit_flank",type=int,default=100)
    parser.add_argument("--outf")
    return parser.parse_args()


def main():
    args=parse_args()
    data=pd.read_csv(args.input_bed,header=None,sep='\t')
    print("loaded data!")
    new_start=[]
    new_end=[]
    new_summit=[]
    for index,row in data.iterrows():
        macs_summit = int(row[1]) + int(row[9])
        start=max(macs_summit-args.summit_flank, 0)
        end=macs_summit+args.summit_flank
        new_start.append(start)
        new_end.append(end)
        new_summit.append((end-start)//2)
    data[1] = new_start
    data[2] = new_end
    data[9] = new_summit
    print("got the adjusted coordinates")
    valid_chroms=['chr' + str(i) for i in range(1,num_autosomes+1)] + ['chrX', 'chrY']
    data=data.loc[data[0].isin(valid_chroms)]
    data.sort_values(by=[0,1,2], inplace=True)
    data.to_csv(args.outf,sep='\t',header=False,index=False)


if __name__=="__main__":
    main()