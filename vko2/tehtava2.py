import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("rivit", help="tulostettavien rivien lukumäärä", type=int)
args = parser.parse_args()

s3 = boto3.client("s3")
s3.download_file("mitja-checkpoint-vko2","checkpoint1.txt","checkpoint1.txt")

with open('checkpoint1.txt') as tekstitiedosto:
    nimilista = tekstitiedosto.readlines()[0:args.rivit]

nimilista.sort(key=len)
ordered_list = "".join(nimilista)

print(ordered_list)