import pygame
import sys
from PySide6 import QtCore, QtWidgets as QtW, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import math

pygame.init()


class configWindow(QtW.QWidget):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.gravitationalConstance = 6.673 * 10**-11

        self.gravitational_force_label = QtW.QLabel()

        self.MassLabel = QtW.QLabel()
        self.MassLabel.setText("Mass in kg")

        self.MassInput = QtW.QLineEdit()
        self.MassInput.setPlaceholderText("Input planet mass")
        self.Mass = 0

        self.RadiusLabel = QtW.QLabel()
        self.RadiusLabel.setText("Radius in km")

        self.RadiusInput = QtW.QLineEdit()
        self.RadiusInput.setPlaceholderText("Input planet radius")
        self.Radius = 0

        self.Center = x, y

        self.createButton = QtW.QPushButton("Create model")
        self.createButton.clicked.connect(self.calculate_gravitational_force)

        self.layout = QtW.QVBoxLayout(self)
        self.layout.addWidget(self.MassLabel)
        self.layout.addWidget(self.MassInput)
        self.layout.addWidget(self.RadiusLabel)
        self.layout.addWidget(self.RadiusInput)
        self.layout.addWidget(self.createButton)
        self.layout.addWidget(self.gravitational_force_label)

    def calculate_gravitational_force(self):
        self.Mass = self.MassInput.text()
        self.Radius = self.RadiusInput.text()
        self.gravitational_force = self.gravitationalConstance * (
            (float(self.Mass)) / (float(self.Radius) ** 2)
        )
        self.gravitational_force_label.setText(str(self.gravitational_force))


if __name__ == "__main__":
    app = QtW.QApplication([])

    widget = configWindow(x=400, y=300)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


class planet:
    def __init__(self):
        self.Mass: float = 0
        self.Radius: float = 0
        self.isInSolarSystem: bool = False


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            key = pygame.mouse.get_pos()
            player.center = key

    pygame.display.update()

pygame.quit()
