import pymxs
import pandas as pd
from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Slot
from pymxs import runtime as rt

class My3dsMaxPlugin(QMainWindow):
    def __init__(self):
        super(My3dsMaxPlugin, self).__init__()

        self.setWindowTitle("Get Bbox sizes")
        self.setGeometry(100, 100, 200, 100)

        widget = QWidget(self)
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        button = QPushButton("Get sizes", self)
        layout.addWidget(button)

        button.clicked.connect(self.on_button_clicked)

    @Slot()
    def on_button_clicked(self):
        scene_objects = rt.objects
        data= {get_dimensions(obj) for obj in scene_objects}

        df = pd.DataFrame(data)
        df.to_excel("output.xlsx", index_label="Название объекта")


def get_dimensions(obj):
    obj = rt.getNodeByName(obj.name)
    if obj is not None:
        try:
            bounding_box = obj.max
        except AttributeError:
            print(f"Объект '{obj.name}' не имеет атрибута 'max'.")
            return None

        length = abs(bounding_box.x)
        width = abs(bounding_box.y)
        height = abs(bounding_box.z)

        dimensions = {
            obj.name: {
                'Длина': length,
                'Ширина': width,
                'Высота': height
            }
        }

        return dimensions
    
def format_dict(input_dict):
        transformed_dict = {}

        for key, value in input_dict.items():
            cost = key.split(".")[0]

            dimensions = f" {value['Длина']} x {value['Ширина']} x {value['Высота']}"
            title = cost + dimensions

            if title in transformed_dict:
                transformed_dict[title]['Количество'] += 1
            else:
                transformed_dict[title] = {
                    "Длина": value["Длина"],
                    "Ширина": value["Ширина"],
                    "Высота": value["Высота"],
                    "Цена": cost,
                    "Количество": 1
                }
        return transformed_dict


plugin = My3dsMaxPlugin()
plugin.show()
