import argparse
import json
import tempfile
import os


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="storage key")
parser.add_argument("--value", help="storage value")
args = parser.parse_args()
if args.key == None:
	print("KeyError")
elif args.value == None:
	pass
else:
	pass

#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#with open(storage_path, 'w') as f: