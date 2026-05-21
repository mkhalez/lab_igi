import csv
import pickle
import os

"""
программа, определяющую, сколько учеников живет на улице, введенной с
клавиатуры, списки учеников, живущих в доме с номером, введенном с
клавиатуры
"""

class Student:
    def __init__(self, last_name, street, house, apartment):
        self.last_name = last_name
        self.street = street
        self.house = str(house)
        self.apartment = str(apartment)

    def __repr__(self):
        return f"{self.last_name} (ул. {self.street}, д. {self.house}, кв. {self.apartment})"

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "street": self.street,
            "house": self.house,
            "apartment": self.apartment
        }

class StudentRegistry:
    def __init__(self, students=None):
        self.students = students or []

    def add_student(self, student):
        self.students.append(student)

    def sort_by_name(self):
        self.students.sort(key=lambda x: x.last_name)

    def count_by_street(self, target_street):
        count = sum(1 for s in self.students if s.street.lower() == target_street.lower())
        return count

    def find_by_house(self, target_house):
        return [s for s in self.students if s.house == str(target_house)]

class CSVHandler:
    @staticmethod
    def save(filename, students):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["last_name", "street", "house", "apartment"])
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict())

    @staticmethod
    def load(filename):
        students = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    students.append(Student(
                                        row["last_name"],
                                        row["street"],
                                        row["house"],
                                        row["apartment"]
                                    ))
        return students

class PickleHandler:
    @staticmethod
    def save(filename, students):
        with open(filename, 'wb') as f:
            pickle.dump(students, f)

    @staticmethod
    def load(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return []

def main():
    initial_data = [
        {"last_name": "Иванов", "street": "Пушкина", "house": "10", "apartment": "5"},
        {"last_name": "Петров", "street": "Ленина", "house": "10", "apartment": "12"},
        {"last_name": "Сидоров", "street": "Пушкина", "house": "15", "apartment": "1"},
        {"last_name": "Козлов", "street": "Советская", "house": "10", "apartment": "44"}
    ]

    students_list = [Student(data["last_name"], data["street"], data["house"], data["apartment"]) for data in initial_data]
    registry = StudentRegistry(students_list)
    registry.sort_by_name()

    csv_file = "students.csv"
    CSVHandler.save(csv_file, registry.students)
    print(f"Данные сохранены в {csv_file}")
    
    loaded_csv = CSVHandler.load(csv_file)
    registry_csv = StudentRegistry(loaded_csv)

    pickle_file = "students.pkl"
    PickleHandler.save(pickle_file, registry.students)
    print(f"Данные сохранены в {pickle_file}\n")

    
    search_street = input("Введите название улицы для подсчета учеников: ")
    count = registry_csv.count_by_street(search_street)
    print(f"На улице {search_street} живет учеников: {count}")

    search_house = input("Введите номер дома для вывода списка: ")
    residents = registry_csv.find_by_house(search_house)
    if residents:
        print(f"В доме №{search_house} живут:")
        for r in residents:
            print(f" - {r.last_name}, кв. {r.apartment}")
    else:
        print("В этом доме ученики не найдены.")

if __name__ == "__main__":
    main()