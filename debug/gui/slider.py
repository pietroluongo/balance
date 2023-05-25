# from PyQt5.QtWidgets import QWidget, QLabel, QSlider
# from PyQt5.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QSlider
from PySide6.QtCore import Qt
from .constants import WIDTH, HEIGHT

LABEL_MARGIN = WIDTH // 25
LABEL_CENTERING_OFFSET = HEIGHT // 100


class Slider(object):
    def __init__(self, label: str, parent: QWidget, pos_x: int, pos_y: int):
        self._x = pos_x
        self._y = pos_y
        self._value: float = 0.0
        self._update_callback = None
        self._mouseup_callback = None

        self._init_label(label, parent, pos_x, pos_y + LABEL_CENTERING_OFFSET)
        self._init_slider(parent, pos_x + LABEL_MARGIN, pos_y)
        self._init_value_label(
            parent, WIDTH - WIDTH // 10, pos_y + LABEL_CENTERING_OFFSET
        )

    def _init_slider(self, parent: QWidget, pos_x: int, pos_y: int):
        slider = QSlider(Qt.Orientation.Horizontal, parent)
        slider.setGeometry(pos_x, pos_y, WIDTH - WIDTH // 3, 30)
        slider.setRange(0, 100)
        slider.show()
        slider.valueChanged.connect(lambda: self._update_value(self._slider.value()))
        self._slider = slider

    def _init_label(self, text: str, parent: QWidget, pos_x: int, pos_y: int):
        label = QLabel(parent)
        label.setText(text)
        label.move(pos_x, pos_y)
        label.show()
        self._text_label = label

    def _init_value_label(self, parent: QWidget, pos_x: int, pos_y: int):
        label = QLabel(parent)
        label.setText("0.0")
        label.move(pos_x, pos_y)
        label.show()
        self._value_label = label

    def _update_value(self, value: float):
        self._value = value
        self._value_label.setText(str(self.value))
        if self._update_callback is not None:
            self._update_callback(value)

    def register_update_callback(self, func):
        self._update_callback = func

    def register_mouseup_callback(self, func):
        self._slider.sliderReleased.connect(lambda: func(self._slider.value()))

    @property
    def value(self) -> float:
        return self._value / 10
