from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


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
