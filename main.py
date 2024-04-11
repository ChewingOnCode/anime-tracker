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


# Function to handle button click event
def on_button_click():
    print("Button clicked")


# Function to read data from a CSV file
def read_csv_data(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Get the header row
        for row in csvreader:
            data.append(row)
    return header, data


# Function to populate the table with data
def populate_table(header, data):
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)
    for row in data:
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, value in enumerate(row):
            table.setItem(rowPosition, col, QTableWidgetItem(value))
    return table


# Class for the edit entry dialog
class EditDialog(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Edit Entry")
        self.layout = QVBoxLayout()

        self.input_fields = []
        for col, value in enumerate(data):
            label = QLabel(f"Entry {col + 1}:")
            line_edit = QLineEdit()
            line_edit.setText(value)
            self.input_fields.append(line_edit)
            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

    # Function to get updated data from the dialog
    def get_updated_data(self):
        return [field.text() for field in self.input_fields]


# Class for the add entry dialog
class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Entry")
        self.layout = QVBoxLayout()

        self.input_fields = []
        for _ in range(2):  # Assuming 2 fields for "New Entry 1" and "New Entry 2"
            label = QLabel(f"New Entry {len(self.input_fields) + 1}:")
            line_edit = QLineEdit()
            self.input_fields.append(line_edit)
            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

    def get_new_data(self):
        return [field.text() for field in self.input_fields]


# Function to handle editing an entry
def edit_entry():
    selected_row = table.currentRow()
    if selected_row >= 0 and selected_row < table.rowCount():
        data = [
            table.item(selected_row, col).text()
            for col in range(table.columnCount())
            if table.item(selected_row, col) is not None
        ]

        dialog = EditDialog(data)
        if dialog.exec_():
            new_data = dialog.get_updated_data()
            for col, value in enumerate(new_data):
                if col < table.columnCount():
                    table.setItem(selected_row, col, QTableWidgetItem(value))
                else:
                    print(f"Column {col} is out of range.")
    else:
        print("Invalid selected row.")


# Function to handle deleting an entry
def delete_entry():
    selected_row = table.currentRow()
    if selected_row >= 0:
        reply = QMessageBox.question(
            window,
            "Delete Entry",
            "Are you sure you want to delete this entry?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            table.removeRow(selected_row)


# Function to add a new entry to the table
def add_entry_dialog():
    dialog = EditDialog([])
    if dialog.exec_():
        new_data = dialog.get_updated_data()
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, value in enumerate(new_data):
            if col < table.columnCount():
                table.setItem(rowPosition, col, QTableWidgetItem(value))
            else:
                print(f"Column {col} is out of range.")


# Function to add a new entry to the table
def add_entry():
    rowPosition = table.rowCount()
    table.insertRow(rowPosition)
    table.setItem(rowPosition, 0, QTableWidgetItem("New Entry 1"))
    table.setItem(rowPosition, 1, QTableWidgetItem("New Entry 2"))


if __name__ == "__main__":
    # Create the main application instance
    app = QApplication(sys.argv)

    # Create a main window
    window = QMainWindow()
    window.setWindowTitle("Anime Series Tracker App")
    window.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

    # Add a button to the main window
    button_add = QPushButton("Add Entry", window)
    button_add.setGeometry(100, 100, 200, 50)
    button_add.clicked.connect(add_entry_dialog)

    button_delete = QPushButton("Delete Entry", window)
    button_delete.setGeometry(100, 200, 200, 50)
    button_delete.clicked.connect(delete_entry)

    # Define the path to your CSV file
    csv_file_path = "animeData.csv"

    # Add a table to the main window
    table = QTableWidget()

    # Add the table to the layout
    layout = QVBoxLayout()

    # Read the CSV file
    header, data = read_csv_data(csv_file_path)
    table = populate_table(header, data)

    # Connect the edit_entry function to a signal (e.g., double click on a cell)
    table.cellDoubleClicked.connect(edit_entry)

    # Add the button and table to the layout
    layout.addWidget(button_add)
    layout.addWidget(button_delete)
    layout.addWidget(table)

    # Add the layout to the main window
    widget = QWidget()
    widget.setLayout(layout)

    window.setCentralWidget(widget)

    # Display the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
