from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from .models import Book
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout

""" books = Book.objects.bulk_create([
Book(name='Гарри Поттер и философский камень', author='Джоан Роулинг', price=700, genre='Фэнтези'),
Book(name='Война и мир', author='Толстой Л.Н.', price=1000, genre='Роман'),
Book(name='Мастер и Маргарита', author='Булгаков М.А.', price=600, genre='Роман'),
Book(name='Маленький принц', author='Антуан де Сент-Экзюпери', price=400, genre='Сказка'),
Book(name='Алиса в Стране чудес', author='Льюис Кэрролл', price=300, genre='Сказка'),
Book(name='Преступление и наказание', author='Федор Достоевский', price=500, genre='Роман'),
Book(name='Голодные игры', author='Сьюзен Коллинз', price=600, genre='Антиутопия'),
]) """


# Create your views here.

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    can_add = request.user.is_authenticated 
    can_edit_delete = request.user.is_staff

    return render(request, 'book_list.html', {'page_obj': page_obj, 'can_add': can_add, 'can_edit_delete': can_edit_delete})


@login_required
def book_new(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        genre = request.POST.get('genre')
        Book.objects.create(
            name=name,
            author=author,
            price=price,
            genre=genre
        )
        return redirect('book_list')
    return render(request, 'book_new.html')

@login_required
@permission_required('main.change_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.genre = request.POST.get('genre')
        book.save()
        return redirect('book_list')
    return render(request, 'book_edit.html', {'book': book})

@login_required
@permission_required('main.delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('book_list')