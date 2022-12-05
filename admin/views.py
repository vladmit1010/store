from django.shortcuts import render, redirect
from .forms import PuzzleForms, CompanyForms, TypeForms, OrderForms

from katalog.models import Puzzle, Company, TypePuzzle, Order


def show_puzzles(request):
    '''Відображання таблиці з товарами'''
    puzzles = Puzzle.objects.all()
    return render(request, 'katalog/show_puzzles.html', {'puzzles': puzzles})


def add_puzzle(request):
    '''додавання нового товару'''
    form = PuzzleForms()
    if request.method == 'GET':
        return render(request, 'katalog/add.html', {'form': form})
    elif request.method == 'POST':
        form = PuzzleForms(request.POST, request.FILES)
        if int(form['price'].data) > 0:
            post = form.save(commit=False)
            post.save()
            return redirect('show_puzzles')
        return render(request, 'katalog/add.html', {'form': form})


def delete_puzzle(request, id):
    '''Видалення товару'''
    Puzzle.objects.get(id=id).delete()
    return redirect('show_puzzles')


def edit_puzzle(request, id):
    '''Редагувааня товару'''
    form = PuzzleForms(instance=Puzzle.objects.get(id=id))
    if request.method == 'POST':
        form = PuzzleForms(request.POST, request.FILES, instance=Puzzle.objects.get(id=id))
        if int(form['price'].data) > 0:
            form.save()
        return redirect('show_puzzles')
    return render(request, 'katalog/edit.html', {'form': form})


def show_companies(request):
    '''Відображення всіх компаній'''
    company = Company.objects.all()
    return render(request, 'katalog/show_companies.html', {'company': company})


def add_company(request):
    '''Додавання нової компанії'''
    form = CompanyForms()
    if request.method == 'GET':
        return render(request, 'katalog/add.html', {'form': form})
    elif request.method == 'POST':
        form = CompanyForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('show_puzzles')


def delete_company(request, id):
    '''Видалення компанії'''
    Company.objects.get(id=id).delete()
    return redirect('show_companies')


def edit_company(request, id):
    '''Редагування компанії'''
    form = CompanyForms(instance=Company.objects.get(id=id))
    if request.method == 'POST':
        form = CompanyForms(request.POST, request.FILES, instance=Company.objects.get(id=id))
        form.save()
        return redirect('show_companies')
    return render(request, 'katalog/edit.html', {'form': form})


def show_types(request):
    '''Відображення всіх типів'''
    type_puz = TypePuzzle.objects.all()
    return render(request, 'katalog/show_types.html', {'types': type_puz})


def add_type(request):
    '''Додавання нового типу'''
    form = TypeForms()
    if request.method == 'GET':
        return render(request, 'katalog/add.html', {'form': form})
    elif request.method == 'POST':
        form = TypeForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('show_types')


def delete_type(request, id):
    '''Видлення нового типу'''
    TypePuzzle.objects.get(id=id).delete()
    return redirect('show_types')


def edit_type(request, id):
    '''Редагування нового типу'''
    form = TypeForms(instance=TypePuzzle.objects.get(id=id))
    if request.method == 'POST':
        form = TypeForms(request.POST, request.FILES, instance=TypePuzzle.objects.get(id=id))
        form.save()
        return redirect('show_types')
    return render(request, 'katalog/edit.html', {'form': form})


def show_orders(request):
    '''Відображення всії заказів'''
    order = Order.objects.all().order_by('is_made')
    return render(request, 'katalog/show_orders.html', {'orders': order})


def delete_order(request, id):
    '''Видалення заказу'''
    Order.objects.get(id=id).delete()
    return redirect('show_orders')


def edit_order(request, id):
    '''Редагування заказу'''
    form = OrderForms(instance=Order.objects.get(id=id))
    if request.method == 'POST':
        form = OrderForms(request.POST, request.FILES, instance=Order.objects.get(id=id))
        form.save()
        return redirect('show_orders')
    return render(request, 'katalog/edit.html', {'form': form})
