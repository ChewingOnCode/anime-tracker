import sys
import csv
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
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


if __name__ == "__main__":
    # Create the main application instance
    app = QApplication(sys.argv)

    # Create a main window
    window = QMainWindow()
    window.setWindowTitle("Anime Series Tracker App")
    window.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

    # Create a button widget
    button = QPushButton("Add Entry", window)
    button.setGeometry(100, 100, 200, 50)
    button.clicked.connect(on_button_click)

    # Create a table widget
    table = QTableWidget(window)
    table.setGeometry(100, 200, 600, 400)

    # Read the CSV file
    csv_file_path = "animeData.csv"
    header, data = read_csv_data(csv_file_path)

    # Set the number of rows and columns in the table
    table.setRowCount(len(data))
    table.setColumnCount(len(header))

    # Set the table headers
    table.setHorizontalHeaderLabels(header)

    # Populate the table with data
    for row, entry in enumerate(data):
        for col, value in enumerate(entry):
            table.setItem(row, col, QTableWidgetItem(value))

    # Set the layout for the main window
    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(table)

    # Create a central widget and set the layout
    central_widget = QWidget()
    central_widget.setLayout(layout)

    # Set the central widget for the main window
    window.setCentralWidget(central_widget)

    # Display the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
