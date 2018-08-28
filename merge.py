import glob
import json

if __name__ == '__main__':
    data = []
    files = glob.glob('data/ACL-*-labeled.json')
    for file in files:
        with open(file, 'r') as f:
            d = json.load(f)
            data.extend(d)

    with open('data/acl-labeled.json', 'w') as f:
        json.dump(data, f, indent=4)
