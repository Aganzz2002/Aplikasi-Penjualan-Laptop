from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtCore import Qt
from models.laptop_model import update_laptop

class EditLaptopDialog(QDialog):
    def __init__(self, parent=None, laptop_id=None, name=None, brand=None, specs=None, price=None, stock=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Laptop")
        self.setFixedSize(400, 300)

        # Set data awal
        self.laptop_id = laptop_id
        self.name = name
        self.brand = brand
        self.specs = specs
        self.price = price
        self.stock = stock

        # Set background color
        self.setStyleSheet("background-color: #1e1e2f; color: white;")

        # Layout utama
        layout = QVBoxLayout()

        # Input fields
        self.name_input = QLineEdit(self.name)
        self.name_input.setPlaceholderText("Nama Laptop")
        self.name_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.name_input)

        self.brand_input = QLineEdit(self.brand)
        self.brand_input.setPlaceholderText("Brand")
        self.brand_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.brand_input)

        self.specs_input = QLineEdit(self.specs)
        self.specs_input.setPlaceholderText("Specs")
        self.specs_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.specs_input)

        self.price_input = QLineEdit(str(self.price))
        self.price_input.setPlaceholderText("Harga")
        self.price_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.price_input)

        self.stock_input = QLineEdit(str(self.stock))
        self.stock_input.setPlaceholderText("Stok")
        self.stock_input.setStyleSheet("background-color: #2d2d44; color: white;")
        layout.addWidget(self.stock_input)

        # Spacer
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tombol Submit
        submit_button = QPushButton("Update Laptop")
        submit_butt
