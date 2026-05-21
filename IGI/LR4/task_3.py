import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def validate_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Некорректный ввод (float), попробуйте снова.")

def get_valid_x():
    while True:
        x = validate_float_input("Введите x (|x| < 1): ")
        if abs(x) < 1:
            return x
        print("Ошибка: число x должно быть |x| < 1")

class SeriesAnalyzer:
    def __init__(self, eps):
        self.eps = eps

    def get_series_terms(self, x):
        terms = []
        n = 0
        while n <= 500:
            current_term = x ** n
            terms.append(current_term)
            if abs(current_term) <= self.eps:
                break
            n += 1
        return terms

    def get_statistics(self, terms):
        if not terms:
            return None
        
        try:
            mode_val = statistics.mode(terms)
        except statistics.StatisticsError:
            mode_val = terms[0] 

        return {
            "mean": statistics.mean(terms),
            "median": statistics.median(terms),
            "mode": mode_val,
            "variance": statistics.variance(terms) if len(terms) > 1 else 0,
            "std_dev": statistics.stdev(terms) if len(terms) > 1 else 0
        }

    def plot_results(self, x_value):
        x_range = np.linspace(-0.95, 0.95, 400)
        
        y_math = [1 / (1 - val) for val in x_range]
        
        y_series = []
        for val in x_range:
            y_series.append(sum(self.get_series_terms(val)))

        plt.figure(figsize=(10, 6))
        plt.plot(x_range, y_math, label=r'Math $F(x) = \frac{1}{1-x}$', color='blue', linewidth=2)
        plt.plot(x_range, y_series, label=f'Ряд (eps={self.eps})', color='red', linestyle='--')

        current_y = sum(self.get_series_terms(x_value))
        plt.scatter([x_value], [current_y], color='green', zorder=5)
        plt.annotate(f'x={x_value}\nF(x)≈{current_y:.4f}', 
                     xy=(x_value, current_y), xytext=(x_value+0.1, current_y+1))

        plt.title('Сравнение функции и ее разложения в ряд')
        plt.xlabel('Аргумент x')
        plt.ylabel('Значение F(x)')
        plt.grid(True, which='both', linestyle=':', alpha=0.7)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.legend()
        plt.text(-0.9, 8, f"Анализ для x={x_value}", fontsize=10, bbox=dict(facecolor='orange'))

        filename = "task_3.png"
        plt.savefig(filename)
        print(f"\nГрафик успешно сохранен в файл: {filename}")
        plt.show()



def main():
    eps = validate_float_input("Введите точность eps: ")
    x = get_valid_x()

    analyzer = SeriesAnalyzer(eps)
    terms = analyzer.get_series_terms(x)
    stats = analyzer.get_statistics(terms)
    
    f_x_approx = sum(terms)
    f_x_math = (1 - x) ** (-1)


    header = ['Параметр', 'Значение']
    table_data = [
        ['x', x],
        ['n (членов)', len(terms)],
        ['F(x) (ряд)', f_x_approx],
        ['Math F(x)', f_x_math],
        ['Eps', eps],
        ['Среднее арифм.', stats['mean']],
        ['Медиана', stats['median']],
        ['Мода', stats['mode']],
        ['Дисперсия', stats['variance']],
        ['СКО (std dev)', stats['std_dev']]
    ]
    print(tabulate(table_data, headers=header, tablefmt='fancy_grid'))

    analyzer.plot_results(x)

if __name__ == "__main__":
    main()