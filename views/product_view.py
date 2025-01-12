from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem, QMessageBox
from PySide6.QtCore import Qt

class ProductView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Laptops")
        self.setGeometry(100, 100, 800, 600)

        # Atur warna latar belakang
        self.setStyleSheet("background-color: #1e1e2f; color: white;")

        # Widget utama
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Tabel Laptop
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Nama", "Brand", "Specs", "Harga", "Stok"])
        main_layout.addWidget(self.table)

        # Tombol CRUD
        button_layout = QHBoxLayout()

        # Spacer di kiri tombol
        button_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Tombol Add
        self.add_button = QPushButton("Add Laptop")
        self.add_button.setFixedWidth(120)
        self.add_button.setStyleSheet("background-color: #0078D7; color: white;")
        button_layout.addWidget(self.add_button)

        # Tombol Edit
        self.edit_button = QPushButton("Edit Selected")
        self.edit_button.setFixedWidth(120)
        self.edit_button.setStyleSheet("background-color: #0078D7; color: white;")
        button_layout.addWidget(self.edit_button)

        # Tombol Delete
        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.setFixedWidth(120)
        self.delete_button.setStyleSheet("background-color: #0078D7; color: white;")
        button_layout.addWidget(self.delete_button)

        # Tombol Cetak
        self.print_button = QPushButton("Cetak Laporan")
        self.print_button.setFixedWidth(120)
        self.print_button.setStyleSheet("background-color: #0078D7; color: white;")
        button_layout.addWidget(self.print_button)

        # Spacer di kanan tombol
        button_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Tambahkan layout tombol ke layout utama
        main_layout.addLayout(button_layout)

        # Atur layout utama
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
