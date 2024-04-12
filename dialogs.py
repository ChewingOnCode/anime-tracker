from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QMessageBox,
)


class EntryDialog(QDialog):
    def __init__(self, headers, data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Entry")
        layout = QVBoxLayout(self)
        self.input_fields = {}
        for header in headers:
            label = QLabel(f"{header}:")
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(f"Enter {header.lower()}")
            if data and header in data:
                line_edit.setText(data[header])
            self.input_fields[header] = line_edit
            layout.addWidget(label)
            layout.addWidget(line_edit)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.on_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_data(self):
        return {
            header: field.text().strip() for header, field in self.input_fields.items()
        }

    def on_accept(self):
        if all(field.text().strip() for field in self.input_fields.values()):
            self.accept()
        else:
            QMessageBox.warning(
                self, "Incomplete Data", "Please complete all fields.", QMessageBox.Ok
            )


def confirm_deletion(parent, entry_name):
    message_box = QMessageBox(parent)
    message_box.setWindowTitle("Confirm Deletion")
    message_box.setText(f"Are you sure you want to delete '{entry_name}'?")
    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    message_box.setDefaultButton(QMessageBox.No)
    return message_box.exec_() == QMessageBox.Yes


# Settings Dialog
class SettingsDialog(QDialog):
    def __init__(self, current_settings, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        layout = QFormLayout()

        # Example setting: Theme selection
        self.theme_selector = QComboBox()
        self.theme_selector.addItems(["Light", "Dark", "System Default"])
        self.theme_selector.setCurrentText(
            current_settings.get("theme", "System Default")
        )
        layout.addRow("Theme:", self.theme_selector)

        # Save and Cancel Buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.setLayout(layout)
        layout.addWidget(self.buttons)

    def get_settings(self):
        return {"theme": self.theme_selector.currentText()}
