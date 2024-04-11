from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
)
from csv_operations import read_csv, write_csv


class CSVApplication(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.btn_read_csv = QPushButton("Read CSV")
        self.btn_write_csv = QPushButton("Write CSV")
        self.btn_read_csv.clicked.connect(self.read_csv_button_clicked)
        self.btn_write_csv.clicked.connect(self.write_csv_button_clicked)
        layout.addWidget(self.btn_read_csv)
        layout.addWidget(self.btn_write_csv)
        self.setLayout(layout)

    def read_csv_button_clicked(self):
        data = read_csv("data.csv")
        # Display or process the data as needed

    def write_csv_button_clicked(self):
        data = [["entry1", "value1"], ["entry2", "value2"]]  # Sample data
        write_csv("data.csv", data)


if __name__ == "__main__":
    app = QApplication([])
    window = CSVApplication()
    window.show()
    app.exec_()
