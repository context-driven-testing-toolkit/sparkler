import argparse, sys

print sys.argv

parser = argparse.ArgumentParser(description='sparkler: make simple graphical plots.')

parser.add_argument('values', metavar='N [label]', nargs='+',
                   help='an integer for the accumulator')

parser.add_argument(
    '-o, --output', 
    metavar='<file>',
    dest='output_file',
    help='name of the output file (default is ./my_graph.png)'
    )

args = parser.parse_args()

print args

