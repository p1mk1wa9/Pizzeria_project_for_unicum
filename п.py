import pandas
import numpy
import pandas as pd

chto_to = pd.read_csv("Test_file.csv", delimiter=";" , names=["id", "name", "age", "surname", "admin", "status"])
stolbec = input("Введите название столбца:")
stroka = int(input("Введите название строчки:"))
anything = input("Введите то, на что хотите заменить")
chto_to.at[stroka, stolbec] = anything
print(chto_to)