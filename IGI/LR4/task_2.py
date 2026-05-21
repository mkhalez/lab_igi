import re
import zipfile
import os

"""
Получить список дат (формат 2007)
Из заданной строки получить список слов, у которых третья с конца буква согласная, а
предпоследняя – гласная.
определить количество слов в строке;
найти самое длинное слово и его порядковый номер;
вывести каждое нечетное слово
"""

class FileArchiveMixin:
    def save_to_file(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"Результаты сохранены в {filename}")

    def create_zip(self, zip_name, target_file):
        with zipfile.ZipFile(zip_name, 'w') as zf:
            zf.write(target_file)
            info = zf.getinfo(target_file)
            return f"Архив {zip_name} создан. Файл: {info.filename}, Размер: {info.file_size} байт"

class BaseTextAnalyzer:
    def __init__(self, text):
        self._text = text
        self.stats = {}

    def get_words(self):
        return re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', self._text)

    def analyze(self):
        words = self.get_words()
        self.word_count = len(words)
        self.stats['total_words'] = self.word_count
        return self.stats

class AdvancedTextAnalyzer(BaseTextAnalyzer, FileArchiveMixin):
    def __init__(self, text):
        super().__init__(text)
        self._output_file = "result.txt"

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self, value):
        if value.endswith('.txt'):
            self._output_file = value

    def analyze(self):
        super().analyze()
        
        decl = len(re.findall(r'[^\.!\?]+\.', self._text))
        interrog = len(re.findall(r'[^\.!\?]+\?', self._text))
        imperative = len(re.findall(r'[^\.!\?]+!', self._text))
        
        smileys = re.findall(r'[;:][\-]*(\(+|\)+|\[+|\]+)', self._text)
        
        dates = re.findall(r'\b\d{4}\b', self._text)
        

        spec_words_pattern = r'\b\w*[бвгджзйклмнпрстфхцчшщ][аеёиоуыэюя]\w\b'
        spec_words = re.findall(spec_words_pattern, self._text, re.IGNORECASE)
        
        words = self.get_words()
        longest_word = max(words, key=len) if words else ""
        longest_index = words.index(longest_word) + 1 if words else 0
        
        avg_word_len = sum(len(w) for w in words) / len(words) if words else 0

        sentences = re.findall(r'[^.!?]+[.!?]', self._text)
        avg_sent_len = sum(len(re.findall(r'\b\w+\b', s)) for s in sentences) / len(sentences)
        
        res = [
            f"Общее кол-во предложений: {decl + interrog + imperative}",
            f"Повествовательные: {decl}, Вопросительные: {interrog}, Побудительные: {imperative}",
            f"Кол-во смайликов: {len(smileys)}",
            f"Список дат: {', '.join(dates)}",
            f"Специфические слова: {', '.join(spec_words)}",
            f"Всего слов: {len(words)}",
            f"Самое длинное слово: '{longest_word}' (№{longest_index})",
            f"Средняя длина слова: {avg_word_len:.2f}",
            f"Нечетные слова: {' '.join(words[::2])}",
            f"Средняя длина предложения: {avg_sent_len}"
        ]
        
        output_data = "\n".join(res)
        self.save_to_file(self.output_file, output_data)
        return output_data


def main():
    input_content = """
    Привет! Как дела в 2007 году? Сегодня отличная погода. 
    Студент сидит в тишине. Книга лежит на столе. 
    Вот смайлики: :-))) ;----[[[[ :[ .
    """
    with open("task_2.txt", "w", encoding="utf-8") as f:
        f.write(input_content)

    with open("task_2.txt", "r", encoding="utf-8") as f:
        content = f.read()

    analyzer = AdvancedTextAnalyzer(content)
    result_text = analyzer.analyze()
    
    print("\n--- РЕЗУЛЬТАТЫ АНАЛИЗА ---")
    print(result_text)

    zip_info = analyzer.create_zip("results_archive.zip", analyzer.output_file)
    print(f"\n{zip_info}")


if __name__ == "__main__":
    main()