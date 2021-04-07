import argparse
import json

js = {
  'message': 'foewijefwoiejfw'
}

parser = argparse.ArgumentParser()

parser.add_argument('file')

args = parser.parse_args()

fileName = args.file

with open(f'{fileName}.json', 'w') as jsFile:
  json.dump(js, jsFile)