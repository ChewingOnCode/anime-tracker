import sys
import csv
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTableWidgetItem,
    QDialog,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QMessageBox,
    QComboBox,
)

# Global Variables for Pagination
current_page = 1
items_per_page = 10
total_pages = 1


# Function to read data from a CSV file
def read_csv_data(file_path):
    try:
        with open(file_path, newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader, ["Title", "Genre", "Rating", "Tags"])
            data = [row for row in csvreader]
    except FileNotFoundError:
        header = ["Title", "Genre", "Rating", "Tags"]
        data = []
    global total_pages
    total_pages = (len(data) + items_per_page - 1) // items_per_page
    return header, data


# Function to populate the table with data
def populate_table(table, header, data):
    table.setRowCount(0)
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)
    start_index = (current_page - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(data))
    for row_data in data[start_index:end_index]:
        row_position = table.rowCount()
        table.insertRow(row_position)
        for col, value in enumerate(row_data):
            table.setItem(row_position, col, QTableWidgetItem(value))


class EntryDialog(QDialog):
    def __init__(self, headers, data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Entry")
        layout = QVBoxLayout(self)
        self.input_fields = {}
        for header in headers:
            label = QLabel(f"{header}:")
            line_edit = QLineEdit(self)
            if data and header in data:
                line_edit.setText(data[header])
            self.input_fields[header] = line_edit
            layout.addWidget(label)
            layout.addWidget(line_edit)

        # Tags input field
        self.tags_field = QLineEdit(self)
        if data and "Tags" in data:
            self.tags_field.setText(data["Tags"])
        layout.addWidget(QLabel("Tags (comma-separated):"))
        layout.addWidget(self.tags_field)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_data(self):
        data = {
            header: field.text().strip() for header, field in self.input_fields.items()
        }
        data["Tags"] = self.tags_field.text().strip()
        return data


def add_entry(table, header, data, file_path):
    dialog = EntryDialog(header)
    if dialog.exec_() == QDialog.Accepted:
        new_data = dialog.get_data()
        data.append([new_data[head] for head in header])
        with open(file_path, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            csvwriter.writerows(data)
        populate_table(table, header, data)


def update_page_info(page_info_label):
    page_info_label.setText(f"Page {current_page} of {total_pages}")


def change_page(step, table, header, data, page_info_label):
    global current_page
    new_page = current_page + step
    if 1 <= new_page <= total_pages:
        current_page = new_page
        populate_table(table, header, data)
        update_page_info(page_info_label)


def filter_by_genre_and_tags(
    table, genre, tags, data, header, page=1, items_per_page=10
):
    genre_index = header.index("Genre")
    tags_index = header.index("Tags")

    filtered_data = [
        row
        for row in data
        if (genre == "All" or row[genre_index].strip().lower() == genre.strip().lower())
    ]

    if tags:
        tag_list = [tag.strip().lower() for tag in tags.split(",")]
        filtered_data = [
            row
            for row in filtered_data
            if any(tag in row[tags_index].lower().split(",") for tag in tag_list)
        ]

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    page_data = filtered_data[start_index:end_index]

    populate_table(table, header, page_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Anime Series Tracker App")
    window.setGeometry(100, 100, 800, 600)

    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)

    genre_dropdown = QComboBox()
    genre_dropdown.addItems(["All", "Action", "Comedy", "Drama", "Fantasy", "Horror"])
    layout.addWidget(genre_dropdown)

    table = QTableWidget()
    csv_file_path = "animeData.csv"
    header, data = read_csv_data(csv_file_path)

    button_prev = QPushButton("Previous Page")
    button_next = QPushButton("Next Page")
    page_info_label = QLabel()
    pagination_layout = QHBoxLayout()
    pagination_layout.addWidget(button_prev)
    pagination_layout.addWidget(page_info_label)
    pagination_layout.addWidget(button_next)
    layout.addLayout(pagination_layout)

    button_prev.clicked.connect(
        lambda: change_page(-1, table, header, data, page_info_label)
    )
    button_next.clicked.connect(
        lambda: change_page(1, table, header, data, page_info_label)
    )
    update_page_info(page_info_label)

    populate_table(table, header, data)

    button_add = QPushButton("Add Entry")
    button_add.clicked.connect(lambda: add_entry(table, header, data, csv_file_path))
    layout.addWidget(button_add)

    button_delete = QPushButton("Delete Entry")
    button_delete.clicked.connect(lambda: delete_entry(table))
    layout.addWidget(button_delete)

    layout.addWidget(table)

    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    window.show()
    sys.exit(app.exec_())
