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


# Function to read data from a CSV file
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


# Function to populate the table with data
def populate_table(table, header, data, page=1, items_per_page=10):
    table.clear()
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    for row_data in data[start_index:end_index]:
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, value in enumerate(row_data):
            table.setItem(rowPosition, col, QTableWidgetItem(value))


def filter_by_genre(table, genre, data, header):
    genre_index = header.index("Genre")
    if genre == "All":
        populate_table(table, header, data)
    else:
        filtered_data = [
            row
            for row in data
            if genre.strip().lower() == row[genre_index].strip().lower()
        ]
        populate_table(table, header, filtered_data)


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
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_data(self):
        return {header: field.text() for header, field in self.input_fields.items()}


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


def edit_entry(table, row, header):
    data = {}
    for col in range(table.columnCount()):
        cell_item = table.item(row, col)
        data[header[col]] = cell_item.text() if cell_item else ""
    for col, column_name in enumerate(header):
        if column_name in data:
            table.setItem(row, col, QTableWidgetItem(data[column_name]))


def delete_entry(table):
    selected_row = table.currentRow()
    if selected_row >= 0:
        entry_name = table.item(selected_row, 0).text()
        reply = QMessageBox.question(
            None,
            "Delete Entry",
            f"Are you sure you want to delete '{entry_name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            table.removeRow(selected_row)


def update_page_info(page_info_label, current_page, total_pages):
    page_info_label.setText(f"Page {current_page} of {total_pages}")


def change_page(
    step,
    table,
    header,
    data,
    page_info_label,
    current_page,
    total_pages,
    items_per_page,
):
    new_page = current_page + step
    if 1 <= new_page <= total_pages:
        current_page = new_page
        populate_table(table, header, data, current_page, items_per_page)
        update_page_info(page_info_label, current_page, total_pages)
    return current_page


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

    # Pagination setup
    current_page = 1
    items_per_page = 10
    total_pages = (len(data) + items_per_page - 1) // items_per_page

    button_prev = QPushButton("Previous Page")
    button_next = QPushButton("Next Page")
    page_info_label = QLabel()
    pagination_layout = QHBoxLayout()
    pagination_layout.addWidget(button_prev)
    pagination_layout.addWidget(page_info_label)
    pagination_layout.addWidget(button_next)
    layout.addLayout(pagination_layout)

    button_prev.clicked.connect(
        lambda: change_page(
            -1,
            table,
            header,
            data,
            page_info_label,
            current_page,
            total_pages,
            items_per_page,
        )
    )
    button_next.clicked.connect(
        lambda: change_page(
            1,
            table,
            header,
            data,
            page_info_label,
            current_page,
            total_pages,
            items_per_page,
        )
    )
    update_page_info(page_info_label, current_page, total_pages)

    populate_table(table, header, data, current_page, items_per_page)
    genre_dropdown.currentIndexChanged.connect(
        lambda: filter_by_genre(table, genre_dropdown.currentText(), data, header)
    )

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
