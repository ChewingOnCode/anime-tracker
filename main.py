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
)


# Function to read data from a CSV file
def read_csv_data(file_path):
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Get the header row
        data = [row for row in csvreader]
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
def add_entry(table, header):
    dialog = EntryDialog(header)
    if dialog.exec_() == QDialog.Accepted:
        new_data = dialog.get_data()
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, head in enumerate(header):
            table.setItem(rowPosition, col, QTableWidgetItem(new_data.get(head, "")))


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

    table = QTableWidget(window)
    csv_file_path = "animeData.csv"
    header, data = read_csv_data(csv_file_path)
    populate_table(table, header, data)

    button_add = QPushButton("Add Entry", window)
    button_add.clicked.connect(lambda: add_entry(table, header))

    button_delete = QPushButton("Delete Entry", window)
    button_delete.clicked.connect(lambda: delete_entry(table))

    table.cellDoubleClicked.connect(lambda row, column: edit_entry(table, row, header))

    layout = QVBoxLayout()
    layout.addWidget(button_add)
    layout.addWidget(button_delete)
    layout.addWidget(table)

    widget = QWidget()
    widget.setLayout(layout)
    window.setCentralWidget(widget)

    window.show()
    sys.exit(app.exec_())
