import argparse

parser = argparse.ArgumentParser(description="our example parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument('--output', required=False)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument('--country', required=False)
parser.add_argument('--year', required=False)

args = parser.parse_args()

import sys


if args.medals:
    output_file = None
    row = 0
    if args.output is not None:
        output_file = open(args.output, "w")
    with open(args.filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[7] == args.country and data[9] == args.year:
                if output_file is not None and row < 10:
                    row += 1
                    output_file.write(f"{data[1]}, {data[-2]}, {data[-1]}\n")




#args = parser.parse_args()
print(f"{args.filename=}")
print(f"{args.medals=}")
print(f"{args.year=}")
print(f"{args.country=}")

print(args)
