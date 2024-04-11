import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QVBoxLayout, QWidget

def on_button_click():
    print("Button clicked")

def read_csv_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Get the header row
        for row in csvreader:
            data.append(row)
    return header, data

def populate_table(header, data):
    table.setColumnCount(len(header))
    table.setHorizontalHeaderLabels(header)
    for row in data:
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        for col, value in enumerate(row):
            table.setItem(rowPosition, col, QTableWidgetItem(value))



# Create the main application instance
app = QApplication(sys.argv)

# Create a main window
window = QMainWindow()
window.setWindowTitle('Anime Series Tracker App')
window.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

# Add a button to the main window
button = QPushButton('Add Entry', window)
button.setGeometry(100, 100, 200, 50)
button.clicked.connect(on_button_click)

# Define the path to your CSV file
csv_file_path = 'animeData.csv'

# Read the CSV file
header, data = read_csv_data(csv_file_path)
populate_table(header, data)

# Add a table to the main window
table = QTableWidget()

# Add the table to the layout
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(table)

# Add the layout to the main window
widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

# Display the main window
window.show()

# Start the application event loop
sys.exit(app.exec_())