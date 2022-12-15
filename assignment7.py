import argparse
import sys

parser = argparse.ArgumentParser(description="our example parser.")
parser.add_argument("--filename", "-f", required=True)
parser.add_argument('--output', required=False)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument('--country', required=False)
parser.add_argument('--year', required=False)
parser.add_argument('--total', action="store_true", required=False)

args = parser.parse_args()

type_of_medal = ["Gold", "Silver", "Bronze"]
dictionary = dict()



if args.medals:
    output_file = None
    row = 0
    if args.output is not None:
        output_file = open(args.output, "w")
    with open(args.filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[7] == args.country and data[9] == args.year:
                if row < 10:
                    row += 1
                    out_line = f"{data[1]}, {data[-2]}, {data[-1]}\n"
                    print(out_line, end="")
                    if output_file is not None:
                        output_file.write(out_line)


if args.total:
    row = 0
    with open(args.filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[9] == args.year:
                if data[7] not in dictionary:
                    dictionary[data[7]] = [0, 0, 0]
                if data[-1] == "Gold":
                    dictionary[data[7]][0] += 1
                if data[-1] == "Silver":
                    dictionary[data[7]][1] += 1
                if data[-1] == "Bronze":
                    dictionary[data[7]][2] += 1
    for country, medals in dictionary.items():
        print(f"in {args.year} the {country} had won {medals[0]} gold medals, {medals[1]} silver medals, {medals[2]} bronze medals")


#args = parser.parse_args()
print(f"{args.filename=}")
print(f"{args.medals=}")
print(f"{args.year=}")
print(f"{args.country=}")

print(args)
