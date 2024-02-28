import sys
from PySide6 import QtCore, QtWidgets as QtW, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import calculations

gravitational_constance = 6.674e-11


class configWindow(QtW.QWidget):
    def __init__(self):
        super().__init__()

        self.input_Mass_Label = QtW.QLabel("Mass of your object:")
        self.input_Mass = QtW.QLineEdit()
        self.input_Mass.setPlaceholderText("Input mass in kg")

        self.input_Radius_Label = QtW.QLabel("Radius of your object:")
        self.input_Radius = QtW.QLineEdit()
        self.input_Radius.setPlaceholderText("Input radius in km")

        self.input_Velocity_Label = QtW.QLabel("Velocity of your object:")
        self.input_Velocity = QtW.QLineEdit()
        self.input_Velocity.setPlaceholderText("Input velocity")

        self.input_x_coordinate_Label = QtW.QLabel("X-coordinate of your object:")
        self.input_x_coordinate = QtW.QLineEdit()
        self.input_x_coordinate.setPlaceholderText("Input x coordinate")

        self.input_y_coordinate_Label = QtW.QLabel("Y-coordinate of your object:")
        self.input_y_coordinate = QtW.QLineEdit()
        self.input_y_coordinate.setPlaceholderText("Input y coordinate")

        self.settings_Window_Button = QtW.QPushButton("Change default settings")
        self.settings_Window_Button.clicked.connect(self.open_Settings_Window)

        self.save_Obj_config = QtW.QPushButton("Save current configuration")
        self.save_Obj_config.clicked.connect(self.create_Object)

        self.main_layout = QtW.QVBoxLayout(self)
        self.main_layout.addWidget(
            self.settings_Window_Button, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Mass_Label, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Mass, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Radius_Label, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Radius, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Velocity_Label, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_Velocity, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_x_coordinate_Label, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_x_coordinate, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_y_coordinate_Label, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.input_y_coordinate, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.save_Obj_config, alignment=QtCore.Qt.AlignmentFlag.AlignBottom
        )

    def open_Settings_Window(self):
        global gravitational_constance
        changeDefaultSettings.show(settingsWindow_widget)

    def create_Object(self):
        self.mass = float(str(self.input_Mass.text()))
        self.radius = float(str(self.input_Radius.text()))
        self.velocity = float(str(self.input_Velocity.text()))
        self.x_coordinate = float(str(self.input_x_coordinate.text()))
        self.y_coordinate = float(str(self.input_y_coordinate.text()))


class initObject(QtW.QWidget):
    def __init__(self):
        super().__init__()

        self.create_Object_button = QtW.QPushButton("Create a new Object")
        self.create_Object_button.clicked.connect(self.create_new_Object)

        self.main_layout = QtW.QVBoxLayout(self)
        self.row_layout = QtW.QHBoxLayout()
        self.column_layout = QtW.QVBoxLayout()

        self.main_layout.addLayout(self.row_layout)
        self.row_layout.addLayout(self.column_layout)
        self.main_layout.addWidget(
            self.create_Object_button, alignment=QtCore.Qt.AlignmentFlag.AlignBottom
        )

    def create_new_Object(self):
        configWindow.show(configWindow_widget)


class changeDefaultSettings(QtW.QWidget):
    global gravitational_constance

    def __init__(self):
        super().__init__()

        # self.gravViewLabel = QtW.QLabel(
        #     "Gravitational constance: " + str(gravitational_constance)
        # )

        self.InputNewGravConst = QtW.QLineEdit()
        self.InputNewGravConst.setPlaceholderText(
            "Current gravitational constance: " + str(gravitational_constance)
        )

        self.editGravConstButton = QtW.QPushButton("Change")
        self.editGravConstButton.clicked.connect(self.changeGravitationalConstance)

        ##//Layouts\\##
        self.main_layout = QtW.QVBoxLayout(self)
        self.columnlayout = QtW.QHBoxLayout()

        self.main_layout.addLayout(self.columnlayout)
        self.columnlayout.addWidget(self.InputNewGravConst)
        self.columnlayout.addWidget(self.InputNewGravConst)
        self.columnlayout.addWidget(self.editGravConstButton)

    def changeGravitationalConstance(self, new_gravitational_constance: float):
        global gravitational_constance
        new_gravitational_constance = float(self.InputNewGravConst.text())
        gravitational_constance = new_gravitational_constance
        print(f"Changed gravitational constance to: {gravitational_constance}")


if __name__ == "__main__":
    app = QtW.QApplication([])

    initObject_widget = initObject()
    initObject_widget.resize(800, 600)
    initObject_widget.setWindowTitle("initObject")
    initObject_widget.show()

    configWindow_widget = configWindow()
    configWindow_widget.resize(400, 500)
    configWindow_widget.setWindowTitle("configWindow")

    settingsWindow_widget = changeDefaultSettings()
    settingsWindow_widget.resize(400, 250)
    settingsWindow_widget.setWindowTitle("settingsWindow")
    sys.exit(app.exec())
