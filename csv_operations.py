import csv


def read_csv(file_path):
    data = []
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


def write_csv(file_path, data):
    with open(file_path, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
