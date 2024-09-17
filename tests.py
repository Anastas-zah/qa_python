from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_lenght_name_more_41(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в Стране Чудес, Или Странствие в Странную Страну по страницам престранной пространной истории')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.set_book_genre('Гарри Поттер и Кубок огня', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и Кубок огня') == 'Фантастика'

    def test_added_books_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Тайная комната')
        assert collector.get_book_genre('Гарри Поттер и Тайная комната') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        detectives_books = collector.get_books_with_specific_genre('Детективы')
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert detectives_books == ['Приключения Шерлока Холмса']
        assert horror_books == ['Сияние']

    def test_get_books_for_chilgren(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.set_book_genre('Гарри Поттер и Философский камень', 'Фантастика')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert children_books == ['Гарри Поттер и Философский камень']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        assert 'Гарри Поттер и Узник Азкабана' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.delete_book_from_favorites('Гарри Поттер и Узник Азкабана')
        assert 'Гарри Поттер и Узник Азкабана' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и Узник Азкабана']

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Идеальный муж')
        collector.set_book_genre('Идеальный муж', 'Комедии')
        assert collector.get_book_genre('Идеальный муж') == 'Комедии'