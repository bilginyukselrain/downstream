import argparse

def write(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

parser = argparse.ArgumentParser(description='Update values in a CSV file.')
parser.add_argument('-e', '--env', help='Helm environment', required=True)
parser.add_argument('-r', '--regions', help='Helm regions separated by space', required=True)
parser.add_argument('-t', '--tag', help='Image tag to replace', required=True)

args = parser.parse_args()

regions = args.regions.split(' ')
for region in regions:
    print('Updating values file: values-{}-{}.yml'.format(args.env, region))
    filename = 'values-{}-{}.yml'.format(args.env, region)
    write(filename, args.tag)

