import argparse
import boto3

# argparserin setup, lisätty integer-tyyppinen argumentti "rivit"
parser = argparse.ArgumentParser()
parser.add_argument("rivit", help="tulostettavien rivien lukumäärä", type=int)
args = parser.parse_args()

# tiedoston lataaminen bucketista
s3 = boto3.client("s3")
s3.download_file("mitja-checkpoint-vko2","checkpoint1.txt","checkpoint1.txt")

# avaa ladatun tiedoston ja lisää uuteen listaan rivit nollasta komentoriviargumentin lukuun asti
with open('checkpoint1.txt') as tekstitiedosto:
    nimilista = tekstitiedosto.readlines()[0:args.rivit]

# yllä tehdyn listan sorttaus list itemin pituuden perusteella ja listan yhdistäminen stringiksi
nimilista.sort(key=len)
ordered_list = "".join(nimilista)

print(ordered_list)