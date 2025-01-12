from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from models.user_model import login_user
from views.dashboard_view import DashboardWindow
from views.register_view import RegisterWindow  # Import RegisterWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 400)

        # Atur warna latar belakang
        self.setStyleSheet("background-color: #1e1e2f;")

        # Widget utama
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Spacer di atas
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Label judul
        title_label = QLabel("Login")
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

        # Tombol Login
        login_button = QPushButton("Login")
        login_button.setStyleSheet(
            """
            QPushButton {
                background-color: #0078D7;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            """
        )
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)

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
        register_button.clicked.connect(self.open_register)
        layout.addWidget(register_button, alignment=Qt.AlignCenter)

        # Spacer di bawah
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Atur layout ke widget utama
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_login(self):
        """Menangani login pengguna."""
        username = self.username_input.text()
        password = self.password_input.text()

        if login_user(username, password):
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
        else:
            error_label = QLabel("Username atau password salah.")
            error_label.setAlignment(Qt.AlignCenter)
            error_label.setStyleSheet("color: red;")
            self.centralWidget().layout().addWidget(error_label)

    def open_register(self):
        """Buka halaman register."""
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
