import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from ui_components import MainApplicationWindow
from dialogs import EntryDialog
from data_manager import (
    read_csv_data,
    write_csv_data,
    filter_data_by_genre,
    get_page_data,
)


def populate_table(window, data, header, page=1, items_per_page=10):
    window.table.clear()  # Clears the entire table including headers
    window.table.setRowCount(0)  # Ensures no rows are left over
    window.table.setColumnCount(len(header))
    window.table.setHorizontalHeaderLabels(header)
    page_data = get_page_data(data, page, items_per_page)
    for row_data in page_data:
        rowPosition = window.table.rowCount()
        window.table.insertRow(rowPosition)
        for col, value in enumerate(row_data):
            window.table.setItem(rowPosition, col, QTableWidgetItem(value))
    update_page_info(window.page_info_label, page, len(data) // items_per_page + 1)


def update_page_info(label, current_page, total_pages):
    label.setText(f"Page {current_page} of {total_pages}")


def main():
    app = QApplication(sys.argv)
    window = MainApplicationWindow()
    csv_file_path = "animeData.csv"
    header, data = read_csv_data(csv_file_path)

    populate_table(window, data, header)

    window.genre_dropdown.currentIndexChanged.connect(
        lambda: filter_and_update_table(window, header, data)
    )

    window.button_prev.clicked.connect(lambda: change_page(window, -1, header, data))
    window.button_next.clicked.connect(lambda: change_page(window, 1, header, data))

    window.button_add.clicked.connect(
        lambda: add_entry(window, header, data, csv_file_path)
    )

    window.button_delete.clicked.connect(
        lambda: delete_entry(window, data, csv_file_path)
    )

    window.show()
    sys.exit(app.exec_())


def filter_and_update_table(window, header, data):
    genre = window.genre_dropdown.currentText()
    filtered_data = filter_data_by_genre(data, genre, header)
    populate_table(
        window, filtered_data, header
    )  # This will clear and repopulate the table


def change_page(window, step, header, data):
    current_page = int(window.page_info_label.text().split()[1])
    new_page = current_page + step
    total_pages = len(data) // window.table.rowCount() + 1
    if 1 <= new_page <= total_pages:
        populate_table(window, data, header, new_page)


def add_entry(window, header, data, file_path):
    dialog = EntryDialog(header)
    if dialog.exec_() == QDialog.Accepted:
        new_data = dialog.get_data()
        data.append([new_data[head] for head in header])
        write_csv_data(file_path, header, data)
        populate_table(window, data, header)


def delete_entry(window, data, file_path):
    selected_row = window.table.currentRow()
    if selected_row >= 0:
        data.pop(selected_row)
        window.table.removeRow(selected_row)
        write_csv_data(file_path, header, data)


if __name__ == "__main__":
    main()
