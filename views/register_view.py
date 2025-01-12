from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from models.user_model import register_user

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(100, 100, 400, 400)

        # Atur warna latar belakang
        self.setStyleSheet("background-color: #1e1e2f;")

        # Widget utama
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Spacer di atas
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label judul
        title_label = QLabel("Register")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            color: white;
            """
        )
        layout.addWidget(title_label)

        # Input Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #2d2d44;
                color: white;
                font-size: 14px;
                padding: 8px;
                border: 1px solid #3e3e5e;
                border-radius: 4px;
            }
            """
        )
        layout.addWidget(self.username_input)

        # Input Email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #2d2d44;
                color: white;
                font-size: 14px;
                padding: 8px;
                border: 1px solid #3e3e5e;
                border-radius: 4px;
            }
            """
        )
        layout.addWidget(self.email_input)

        # Input Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #2d2d44;
                color: white;
                font-size: 14px;
                padding: 8px;
                border: 1px solid #3e3e5e;
                border-radius: 4px;
            }
            """
        )
        layout.addWidget(self.password_input)

        # Tombol Register
        register_button = QPushButton("Register")
        register_button.setStyleSheet(
            """
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            """
        )
        register_button.clicked.connect(self.handle_register)
        layout.addWidget(register_button, alignment=Qt.AlignCenter)

        # Spacer di bawah
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Atur layout ke widget utama
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_register(self):
        """Menangani registrasi pengguna."""
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        if username and email and password:
            register_user(username, password, email)
            self.close()  # Kembali ke halaman login
        else:
            error_label = QLabel("Semua kolom harus diisi!")
            error_label.setAlignment(Qt.AlignCenter)
            error_label.setStyleSheet("color: red;")
            self.centralWidget().layout().addWidget(error_label)
