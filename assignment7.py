def split_line(line):
    line_list = line.split()
    result = []
    index = 0
    paws_met = False # перевіряємо лапки
    for element in line_list:
        if element.startswith('"'):
            result[]

def checking_medals(medals, country, ):
    with open("Olympic Athletes - athlete_events.csv", "r") as file:
        head = None
        for line in file.readlines():
            if head is None:
                head = line.split(",")
                continue
            line.split()


p1 = ""
p2 = ""

while True:
    p1 = input()
    p2 = input()
    checking_medals(p1, p2)
