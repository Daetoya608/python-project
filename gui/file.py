from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
import sys


class ClickableLabel(QLabel):
    # Определяем кастомный сигнал
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        # Отправляем сигнал при нажатии
        self.clicked.emit()
        super().mousePressEvent(event)


class ProductCard(QWidget):
    def __init__(self, image_text, name, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(400, 150)  # Размер каждой карточки

        layout = QVBoxLayout(self)

        # Создание и настройка виджетов для фото, названия и цены
        self.image_label = QLabel(image_text)
        self.name_label = QLabel(name)
        self.price_label = QLabel(price)

        # Добавляем виджеты в компоновку карточки
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)

        # Настраиваем шрифты и выравнивание
        self.image_label.setAlignment(Qt.AlignCenter)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.price_label.setAlignment(Qt.AlignCenter)
        self.name_label.setStyleSheet("font-size: 18px;")
        self.price_label.setStyleSheet("font-size: 16px; color: green;")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка основного окна
        self.setWindowTitle("Mini Marketplace")
        self.setGeometry(100, 100, 450, 750)  # Устанавливаем размер окна

        # Верхняя фиксированная область
        self.top_frame = QFrame(self)
        self.top_frame.setFixedHeight(50)
        self.top_frame.setStyleSheet("background-color: lightgray;")

        # Компоновка для верхнего фрейма
        top_layout = QHBoxLayout(self.top_frame)

        # Добавляем заголовок слева
        title_label = QLabel("Добро пожаловать в маркетплейс")
        title_label.setStyleSheet("font-size: 16px;")

        # Создаем виджет для изображения с возможностью отслеживания клика
        self.image_label = ClickableLabel()
        pixmap = QPixmap("your_image.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

        # Подключаем сигнал клика к методу для переключения окна
        self.image_label.clicked.connect(self.switch_to_cart_view)

        # Добавляем заголовок и картинку в компоновку
        top_layout.addWidget(title_label)
        top_layout.addStretch()  # Отступ для выравнивания
        top_layout.addWidget(self.image_label)  # Картинка справа

        # Нижняя фиксированная область
        self.bottom_frame = QFrame(self)
        self.bottom_frame.setFixedHeight(50)
        self.bottom_frame.setStyleSheet("background-color: lightgray;")

        # Создаем прокручиваемую область для карточек товаров
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Основной контейнер для карточек товаров
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)

        # Добавляем несколько карточек товаров
        for i in range(10):
            card = ProductCard(f"Фото {i + 1}", f"Товар {i + 1}", f"{(i + 1) * 100} руб")
            self.content_layout.addWidget(card)

        self.scroll_area.setWidget(self.content_widget)

        # Главная вертикальная компоновка для всего окна
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addWidget(self.bottom_frame)

        # Создаем центральный виджет для компоновки main_layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def switch_to_cart_view(self):
        # Очищаем текущий виджет и добавляем новый контент для корзины
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавляем виджет с сообщением о корзине
        cart_label = QLabel("Корзина: пока пусто")
        cart_label.setStyleSheet("font-size: 24px; color: blue;")
        cart_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(cart_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
