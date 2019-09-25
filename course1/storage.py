import argparse
import json
import tempfile
import os


def remove_file(path):
	os.remove(path)

	
def key_print(path, key):
	try:
		with open(storage_path, 'r') as f:
			result = json.loads(f.read())
			print(", ".join(result[key]))
	except FileNotFoundError:
		print()

		
def file_write(path, key, value):
	try:
		with open(storage_path, 'r') as f:
			result = json.loads(f.read())
		with open(storage_path, 'w') as f:
			if key not in result.keys():
				result[key] = result.get(key, []) + [value]
				f.write(json.dumps(result))
			else:
				result[key] += [value]
				f.write(json.dumps(result))
	except FileNotFoundError:
		with open(storage_path, 'w') as f:
			result = json.dumps({key:[value]})
			f.write(result)

			
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="storage key")
parser.add_argument("--value", help="storage value")
parser.add_argument("--clear", help="remove the file")
args = parser.parse_args()
key = args.key
value = args.value
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.clear:
	remove_file(storage_path)
else:
	if key == None:
		print("Enter the key")
	elif value == None:
		key_print(storage_path, key)
	else:
		file_write(storage_path, key, value)
