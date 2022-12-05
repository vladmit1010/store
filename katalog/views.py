from django.shortcuts import render, redirect
from .models import Company, Puzzle, TypePuzzle, Order
from .forms import PuzzleForm
from katalog.forms import BuyerForm

cart = {}


def home(request):
    '''Головна сторінка'''
    form = PuzzleForm
    puzzles = Puzzle.objects.all().order_by('-counter')
    type_puzzle = TypePuzzle.objects.all().order_by('name')
    company_puzzle = Company.objects.all()
    is_admin = request.user.is_staff
    return render(request, 'katalog/index.html',
                  {'puzzles': puzzles, 'type_puzzle': type_puzzle, 'company_puzzle': company_puzzle, 'form': form,
                   'is_admin': is_admin})


def about(request):
    '''Про сайт'''
    return render(request, 'katalog/about.html')


def contact(request):
    '''Наші контактні номери'''
    return render(request, 'katalog/contact.html')


def about_puzzle(request, id_puzzle):
    '''Інформація про конкретниий товар'''
    puzzle = Puzzle.objects.get(id=id_puzzle)
    return render(request, 'katalog/about_puzzle.html', {'puzzle': puzzle})


def filter(request):
    '''Фільтр'''
    form = PuzzleForm
    puzzles = Puzzle.objects.all().order_by('-counter')
    type_puzzle = TypePuzzle.objects.all().order_by('name')
    company_puzzle = Company.objects.all()
    querydict = dict(request.GET)
    types = querydict.get('type')
    companes = querydict.get('company')
    price_from = querydict.get('price_from')[0]
    price_to = querydict.get('price_to')[0]
    puz_types = []
    puz_companes = []
    puz_price = list(puzzles)
    output_puzzles = []
    if types:
        for name in types:
            puz_types += puzzles.filter(type=TypePuzzle.objects.get(name=name))
        output_puzzles = set(output_puzzles).union(set(puz_types))
    if companes:
        for name in companes:
            puz_companes += puzzles.filter(company=Company.objects.get(name=name))
        output_puzzles = set(output_puzzles).union(set(puz_companes))
    if not output_puzzles:
        output_puzzles = puzzles
    if price_from:
        puz_price = puzzles.filter(price__gte=price_from)
    if price_to:
        puz_price = puzzles.filter(price__lte=price_to)
    output_puzzles = set(output_puzzles).intersection(set(puz_price))
    return render(request, 'katalog/index.html',
                  {'puzzles': output_puzzles, 'type_puzzle': type_puzzle, 'company_puzzle': company_puzzle,
                   'form': form})


def add_puzzle_to_cart(request, id_puzzle):
    '''Додавання до корзини нового товару'''
    if cart.get(request.user) is None:
        cart.update({request.user: []})
    for item in cart[request.user]:
        if Puzzle.objects.get(id=id_puzzle) in item:
            break
    else:
        cart[request.user].append([Puzzle.objects.get(id=id_puzzle), request.GET['quantity']])
    return redirect('katalog')


def my_basket(request):
    '''Корзина'''
    basket_users = cart.get(request.user)
    form = BuyerForm()
    total = 0
    if basket_users is None:
        return render(request, 'katalog/cart.html', {'cart': basket_users, 'total': total})
    for item in basket_users:
        total += item[0].price * int(item[1])
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            user_surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            address_post = form.cleaned_data['address_post']
            order = Order(
                user_name=user_name,
                user_surname=user_surname,
                email=email,
                address_post=address_post,
                total_price=total,
                order=';'.join(
                    [f'{basket_users[item][0]}: {basket_users[item][1]} ' for item in range(len(basket_users))])
            ).save()
        return redirect('katalog')
    return render(request, 'katalog/cart.html', {'cart': basket_users, 'total': total, 'form': form})


def remove_puzzle_in_basket(request, id_puzzle):
    '''Видалення товару з корзини'''
    basket_users = cart.get(request.user)
    for item in basket_users:
        if Puzzle.objects.get(id=id_puzzle) in item:
            basket_users.remove(item)
    return redirect('my_basket')
