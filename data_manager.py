import csv


def read_csv_data(file_path):
    try:
        with open(file_path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader, ["Title", "Genre", "Rating"])
            data = [row for row in csvreader]
    except FileNotFoundError:
        header = ["Title", "Genre", "Rating"]
        data = []
    return header, data


# Function to write data to a CSV file
def write_csv_data(file_path, header, data):
    with open(file_path, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(data)


# Function to filter data by genre
def filter_data_by_genre(data, genre, header):
    genre_index = header.index("Genre")
    if genre == "All":
        return data
    else:
        return [
            row
            for row in data
            if genre.strip().lower() == row[genre_index].strip().lower()
        ]


# Pagination functions (assume these are used to manage paging through data)
def get_page_data(data, page=1, items_per_page=10):
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    return data[start_index:end_index]
