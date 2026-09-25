"""
show the number of unique episodes in the dataset
"""

import argparse
import csv

parser = argparse.ArgumentParser()
# flags -> positional encoding of the arguments
parser.add_argument('-i', '--data', type=str, help='path to data file')
#parser.add_argument('o', '--output', type=str, help='path to output file')
# run with "python num_episode.py --i ../data/xxx.csv --o .../data/out"
args = parser.parse_args()
print('data file:', args.data)
#print('output', args.output)

episodes = set() #a set: a collection that stores unique values only.
with open(args.data, 'r') as fi:
    reader = csv.reader(fi)
    next(reader) #skip the first line
    for row in reader:
        episodes.add(row[0]) #episode

print('unique episodes:', len(episodes))
#print('episodes:', episodes)
#print('Friendship is Magic, part 1' in episodes)