from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QLabel,
    QComboBox,
)


class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Series Tracker App")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.configure_ui()

    def configure_ui(self):
        # Setup the main window layout and primary widgets
        self.setup_genre_dropdown()
        self.setup_table()
        self.setup_pagination_controls()
        self.setup_entry_buttons()

    def setup_genre_dropdown(self):
        self.genre_dropdown = QComboBox()
        self.genre_dropdown.addItems(
            ["All", "Action", "Comedy", "Drama", "Fantasy", "Horror"]
        )
        self.layout.addWidget(self.genre_dropdown)

    def setup_table(self):
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def setup_pagination_controls(self):
        self.button_prev = QPushButton("Previous Page")
        self.button_next = QPushButton("Next Page")
        self.page_info_label = QLabel()
        pagination_layout = QHBoxLayout()
        pagination_layout.addWidget(self.button_prev)
        pagination_layout.addWidget(self.page_info_label)
        pagination_layout.addWidget(self.button_next)
        self.layout.addLayout(pagination_layout)

    def setup_entry_buttons(self):
        self.button_add = QPushButton("Add Entry")
        self.button_delete = QPushButton("Delete Entry")
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.button_delete)
