import csv


def read_csv(filename) -> list:
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return data


def write_csv():
    pass
