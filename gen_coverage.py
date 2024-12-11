import json
import os
import random
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-j', '--json', type=str, required=True)
parser.add_argument('-o', '--output', type=str, required=True)
parser.add_argument('-c', '--coverage', type=float, required=True)
args = parser.parse_args()

json_name = args.json

data = {}
with open(json_name) as f:
    data = json.load(f)


num = 0
new_json : dict = {}
for bmk in data.items():
    bmk_name, bmk_ckpts = bmk
    bmk_ckpts['points'] = sorted(bmk_ckpts['points'].items(), key=lambda x: float(x[1]), reverse=True)
    #print(bmk_name, bmk_ckpts)
    lst = []
    total = 0
    while total < args.coverage:
        point = bmk_ckpts['points'][0]
        total += float(point[1])
        bmk_ckpts['points'].remove(point)
        lst.append(point)
    #print(total)
    #lst = [bmk_name + '/' + i[0] + '/_' + i[0] + '_' + i[1] + '_.zstd' for i in lst]
    new_json[bmk_name] = {
        'insts' : bmk_ckpts['insts'],
        'points' : dict(lst)
    }
json.dump(new_json, open(args.output, 'w'), indent=4)
