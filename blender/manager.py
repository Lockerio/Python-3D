import bpy
import pandas as pd


class DataManager():
    @staticmethod
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

    @staticmethod
    def save_dict_to_excel(data, excel_filename):
        df = pd.DataFrame(data).T
        df.to_excel(excel_filename, index_label="Название объекта")