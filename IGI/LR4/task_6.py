import pandas as pd

def a_point(df):
    
    unique_levels = df['Level'].unique()

    difficulty_levels = pd.Series(
        unique_levels, 
        index=[f'diff_{i+1}' for i in range(len(unique_levels))]
    )

    print("--- Объект Series: difficulty_levels ---")
    print(difficulty_levels)

    print(f"\nДоступ через .loc['diff_1']: {difficulty_levels.loc['diff_1']}")
    print(f"Доступ через .iloc[0]: {difficulty_levels.iloc[0]}")

def b_point(df):
    avg_rating_max = df[df['Level'] == 'Expert']['Rating'].mean()

    avg_rating_min = df[df['Level'] == 'Beginner']['Rating'].mean()

    ratio = avg_rating_max / avg_rating_min

    print(f"Средний рейтинг Expert: {avg_rating_max:.2f}")
    print(f"Средний рейтинг Beginner: {avg_rating_min:.2f}")
    print(f"Отношение: {ratio:.2f}")

def main():
    df = pd.read_csv('megaGymDataset.csv')
    a_point(df)
    print("=====================")
    b_point(df)

if __name__ == "__main__":
    main()