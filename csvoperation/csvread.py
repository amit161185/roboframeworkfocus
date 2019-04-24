import csv
from pathlib import Path

data_folder = Path('C:/githubPythonProjectClone/data')
print("your data folder path is this:", data_folder)


class CsvReadfile:

    def csvreadmethod(self):
        file_to_open = data_folder / "inputcsvread.csv"
        print("your file name:", file_to_open)
        with open(file_to_open, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for values in reader:
              print(values)

        name = csvFile.name
        print(name)
        #print(csvFile.read())
        #csvFile.truncate(1)
