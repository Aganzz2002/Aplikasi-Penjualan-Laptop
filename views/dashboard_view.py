from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from views.product_view import ProductView

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 800, 600)

        # Atur warna latar belakang
        self.setStyleSheet("background-color: #1e1e2f;")

        # Widget utama
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Spacer di atas label
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label Selamat Datang
        self.welcome_label = QLabel("Selamat datang di\nAganzz Laptop Store!")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            color: white;
            """
        )
        layout.addWidget(self.welcome_label, alignment=Qt.AlignCenter)

        # Spacer di antara label dan tombol
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tombol Manage Laptops
        self.manage_laptops_button = QPushButton("Manage Laptops")
        self.manage_laptops_button.setStyleSheet(
            """
            QPushButton {
                background-color: #0078D7;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            """
        )
        self.manage_laptops_button.clicked.connect(self.open_manage_laptops)
        layout.addWidget(self.manage_laptops_button, alignment=Qt.AlignCenter)

        # Spacer di bawah tombol
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tombol Logout
        self.logout_button = QPushButton("Logout")
        self.logout_button.setStyleSheet(
            """
            QPushButton {
                background-color: #d9534f;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
            """
        )
        self.logout_button.clicked.connect(self.handle_logout)
        layout.addWidget(self.logout_button, alignment=Qt.AlignCenter)

        # Spacer di bawah tombol Logout
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Atur layout ke widget utama
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_manage_laptops(self):
        """Membuka halaman Manage Laptops."""
        self.product_view = ProductView()
        self.product_view.show()

    def handle_logout(self):
        """Kembali ke halaman login."""
        self.close()  # Tutup dashboard
