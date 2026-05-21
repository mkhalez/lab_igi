import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class ShapeColor:
    def __init__(self, color="white"):
        self._color = color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value

class GeometricFigure(ABC):
    @abstractmethod
    def calc_area(self):
        pass

class Parallelogram(GeometricFigure):
    name = "Параллелограмм"
    def __init__(self, a, b, angle_deg, color_name):
        self.a = a
        self.b = b
        self.angle = angle_deg
        self.shape_color = ShapeColor(color_name)
    def get_name(self):
        return self.name
    def calc_area(self):
        return self.a * self.b * math.sin(math.radians(self.angle))
    def get_info(self):
        info = "Фигура: {0}\nСтороны: a={1}, b={2}\nУгол: {3}°\nЦвет: {4}\nПлощадь: {5:.2f}".format(
            self.get_name(), self.a, self.b, self.angle, self.shape_color.color, self.calc_area()
        )
        return info

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("Ошибка: введите положительное число.")

class Drawer():
    def draw_parallelogram(self, fig_obj, label_text):
        rad = math.radians(fig_obj.angle)
        
        x_coords = [0, fig_obj.a, fig_obj.a + fig_obj.b * math.cos(rad), fig_obj.b * math.cos(rad)]
        y_coords = [0, 0, fig_obj.b * math.sin(rad), fig_obj.b * math.sin(rad)]
        vertices = list(zip(x_coords, y_coords))
        
        fig, ax = plt.subplots()
        polygon = patches.Polygon(vertices, closed=True, 
                                linewidth=2, edgecolor='black', 
                                facecolor=fig_obj.shape_color.color)
        
        ax.add_patch(polygon)
        
        max_y = max(y_coords)
        text_y_position = max_y + (max_y * 0.1 if max_y > 0 else 0.5)
        
        plt.text(0, text_y_position, label_text, 
                fontsize=12, fontweight='bold', color='black', 
                ha='left', va='bottom')
        
        plt.xlim(min(x_coords) - 1, max(x_coords) + 1)
        plt.ylim(-1, text_y_position + 1)
        
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(f"{fig_obj.get_name()} ({fig_obj.shape_color.color})", pad=20)
        
        plt.savefig("parallelogram.png")
        print("\nИзображение сохранено в файл 'parallelogram.png'")
        plt.show()

def main():
    print("--- Построение параллелограмма ---")
    
    side_a = get_positive_float("Введите длину стороны a: ")
    side_b = get_positive_float("Введите длину стороны b: ")
    
    while True:
        angle = get_positive_float("Введите угол A между сторонами (в градусах, < 180): ")
        if angle < 180:
            break
        print("Ошибка: угол должен быть меньше 180 градусов.")
    
    color = input("Введите цвет фигуры (например, 'blue', 'red', 'green'): ")
    label = input("Введите текст для подписи фигуры: ")
    
    p_fig = Parallelogram(side_a, side_b, angle, color)
    print("\n" + "="*20)
    print(p_fig.get_info())
    print("="*20)
    
    drawer = Drawer()
    drawer.draw_parallelogram(p_fig, label)

if __name__ == "__main__":
    main()