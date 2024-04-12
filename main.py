import sys
import csv
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
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
            header = next(
                csvreader, ["Title", "Genre", "Rating"]
            )  # Default headers if CSV is empty
            data = [row for row in csvreader]
    except FileNotFoundError:
        header = ["Title", "Genre", "Rating"]  # Default headers
        data = []  # Initialize an empty list for data
    return header, data


# Function to populate the table with data
def populate_table(table, header, data):
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)
    for row_data in data:
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, value in enumerate(row_data):
            table.setItem(rowPosition, col, QTableWidgetItem(value))


def filter_by_genre(table, genre, data, header):
    """
    Filters the table by genre and updates the table with the filtered data.

    Args:
        table (QTableWidget): The table widget to be filtered.
        genre (str): The genre to filter by. Use "All" to show all entries.
        data (list): The data to filter.
        header (list): The header of the table.

    Returns:
        None
    """
    # Assuming the second column in your CSV is the 'Genre' column
    genre_index = header.index("Genre")  # Adjust column index as necessary

    if genre == "All":
        populate_table(table, header, data)
    else:
        # Ensure comparison is case-insensitive and handles any leading/trailing whitespace
        filtered_data = [
            row
            for row in data
            if genre.strip().lower() == row[genre_index].strip().lower()
        ]
        populate_table(table, header, filtered_data)


def multi_column_sort(data, sort_criteria):
    """
    Sorts the data based on multiple columns.

    :param data: The data to sort, a list of lists.
    :param sort_criteria: A list of tuples specifying the sorting criteria.
                          Each tuple is (column_index, sort_order),
                          where sort_order is 'asc' for ascending or 'desc' for descending.
    """
    for column_index, sort_order in reversed(sort_criteria):
        data.sort(key=lambda row: row[column_index], reverse=(sort_order == "desc"))


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


# Function to handle adding a new entry to the table
def add_entry(table, header, data, file_path):
    dialog = EntryDialog(header)
    if dialog.exec_() == QDialog.Accepted:
        new_data = dialog.get_data()
        data.append([new_data[head] for head in header])

        # Write the updated data to the CSV file
        with open(file_path, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)  # Write the header
            csvwriter.writerows(data)  # Write the updated data

        populate_table(table, header, data)


# Function to handle editing an entry
def edit_entry(table, row, header):
    data = {}
    for col in range(table.columnCount()):
        cell_item = table.item(row, col)
        column_name = header[col]  # Get the column name using the column index
        data[column_name] = (
            cell_item.text() if cell_item else ""
        )  # Get the cell text or set to empty string if None

    # Now you can use 'data' for editing operations
    # print(data)

    # he data is directly edited and needs to be updated in the table
    for col, column_name in enumerate(header):
        if column_name in data:
            table.setItem(row, col, QTableWidgetItem(data[column_name]))


# Function to handle deleting an entry
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Anime Series Tracker App")
    window.setGeometry(100, 100, 800, 600)

    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)  # Create a layout for the central widget

    genre_dropdown = QComboBox()
    genre_dropdown.addItems(["All", "Action", "Comedy", "Drama", "Fantasy", "Horror"])
    layout.addWidget(genre_dropdown)  # Add the genre dropdown to the layout

    table = QTableWidget()
    csv_file_path = "animeData.csv"
    header, data = read_csv_data(csv_file_path)
    populate_table(table, header, data)

    genre_dropdown.currentIndexChanged.connect(
        lambda: filter_by_genre(table, genre_dropdown.currentText(), data, header)
    )

    button_add = QPushButton("Add Entry")
    button_add.clicked.connect(lambda: add_entry(table, header, data, csv_file_path))
    layout.addWidget(button_add)  # Add the add button to the layout

    button_delete = QPushButton("Delete Entry")
    button_delete.clicked.connect(lambda: delete_entry(table))
    layout.addWidget(button_delete)  # Add the delete button to the layout

    layout.addWidget(table)  # Add the table to the layout

    central_widget.setLayout(layout)  # Set the layout for the central widget
    window.setCentralWidget(central_widget)  # Set the central widget of the window

    window.show()
    sys.exit(app.exec_())
