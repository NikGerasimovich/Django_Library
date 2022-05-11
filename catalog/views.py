from django.http import Http404
from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Книги содержащие в себе слово 80
    num_book_part = Book.objects.all().filter(title__icontains='80')
    num_count_part = num_book_part.count()

    # Книги с одинаковым жанром(Детектив)
    num_book_insane_part = Book.objects.filter(genre__name__icontains='Фантастика')
    num_count_insane_part = num_book_insane_part.count()

    # Получение числа визитов на главную страницу
    num_authors = Author.objects.count()
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_book_part': num_book_part,
                 'num_count_part': num_count_part,
                 'num_book_insane_part': num_book_insane_part,
                 'num_count_insane_part': num_count_insane_part,
                 'num_visit': num_visit,
                 },
    )


class BookListViews(generic.ListView):
    model = Book
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListViews, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class BookDetailViews(generic.DetailView):
    model = Book

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        return render(
            request,
            'catalog/book_detail.html',
            context={'book': book_id, }
        )


class AuthorListViews(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AuthorListViews, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailViews(generic.DetailView):
    model = Author

    def author_detail_view(request, pk):

        author_id = Author.objects.get(pk=pk)
        return render(
            request,
            'catalog/author_detail.html',
            context={'author': author_id, }
        )