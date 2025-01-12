from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtCore import Qt
from models.laptop_model import create_laptop

class AddLaptopDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Laptop")
        self.setFixedSize(400, 300)

        # Set background color
        self.setStyleSheet("background-color: #1e1e2f; color: white;")

        # Layout utama
        layout = QVBoxLayout()

        # Input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama Laptop")
        self.name_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.name_input)

        self.brand_input = QLineEdit()
        self.brand_input.setPlaceholderText("Brand")
        self.brand_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.brand_input)

        self.specs_input = QLineEdit()
        self.specs_input.setPlaceholderText("Specs")
        self.specs_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.specs_input)

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Harga")
        self.price_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.price_input)

        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText("Stok")
        self.stock_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.stock_input)

        # Spacer
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tombol Submit
        submit_button = QPushButton("Add Laptop")
        submit_button.setStyleSheet(
            "background-color: #0078D7; color: white; padding: 10px; border-radius: 6px;"
        )
        submit_button.clicked.connect(self.handle_submit)
        layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        # Set layout ke dialog
        self.setLayout(layout)

    def handle_submit(self):
        """Handle submit data laptop."""
        name = self.name_input.text()
        brand = self.brand_input.text()
        specs = self.specs_input.text()
        try:
            price = float(self.price_input.text())
            stock = int(self.stock_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga dan Stok harus berupa angka!")
            return

        if name and brand and specs and price and stock:
            create_laptop(name, brand, specs, price, stock)
            QMessageBox.information(self, "Success", "Laptop berhasil ditambahkan!")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
