import pymxs
import xlwt
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
        data_list = [get_dimensions(obj) for obj in scene_objects]

        data_list = [data for data in data_list if data is not None]

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Sheet1')

        headers = ['Name', 'Length', 'Width', 'Height']
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header)

        for row_num, data in enumerate(data_list, 1):
            for col_num, key in enumerate(headers):
                sheet.write(row_num, col_num, data[key])

        workbook.save('output_xlwt.xls')


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
            'Длина': length,
            'Ширина': width,
            'Высота': height
        }

        return dimensions


plugin = My3dsMaxPlugin()
plugin.show()
