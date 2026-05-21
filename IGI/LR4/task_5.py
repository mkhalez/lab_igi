import numpy as np

def calculate_median_manual(row):
    sorted_row = np.sort(row)
    n = len(sorted_row)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_row[mid - 1] + sorted_row[mid]) / 2
    else:
        return sorted_row[mid]

def main():
    n, m = 4, 5 

    A = np.random.randint(1, 100, size=(n, m))
    
    print("Исходная матрица A:")
    print(A)
    print("-" * 30)

    last_row = A[-1, :]
    print(f"Последняя строка до сортировки: {last_row}")

    sorted_last_row = np.sort(last_row)
    print(f"Последняя строка после сортировки: {sorted_last_row}")

    median_np = np.median(sorted_last_row)
    
    median_manual = calculate_median_manual(sorted_last_row)

    print("-" * 30)
    print(f"Медиана (через np.median()): {median_np}")
    print(f"Медиана (через формулу):    {median_manual}")

    print("-" * 30)
    print(f"Среднее арифметическое (mean) всей матрицы: {np.mean(A):.2f}")
    print(f"Дисперсия (var) последней строки:          {np.var(sorted_last_row):.2f}")
    print(f"Стандартное отклонение (std) матрицы:     {np.std(A):.2f}")
    
    if n > 1:
        corr = np.corrcoef(A[0, :], A[-1, :])[0, 1]
        print(f"Корреляция между 1-й и {n}-й строками:   {corr:.2f}")

if __name__ == "__main__":
    main()