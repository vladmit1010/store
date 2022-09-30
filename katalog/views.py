from django.shortcuts import render, redirect
from .models import Company, Puzzle, TypePuzzle
from .forms import PuzzleForm
from auth.forms import BuyerForm
cart = {}


def home(request):
    form = PuzzleForm
    puzzles = Puzzle.objects.all().order_by('-counter')
    type_puzzle = TypePuzzle.objects.all().order_by('name')
    company_puzzle = Company.objects.all()
    return render(request, 'katalog/index.html',
                  {'puzzles': puzzles, 'type_puzzle': type_puzzle, 'company_puzzle': company_puzzle, 'form': form})


def about(request):
    return render(request, 'katalog/about.html')


def catalog(request):
    return render(request, 'katalog/contact.html')


def about_puzzle(request, id_puzzle):
    puzzle = Puzzle.objects.get(id=id_puzzle)
    return render(request, 'katalog/about_puzzle.html', {'puzzle': puzzle})


def filter(request):
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
    if cart.get(request.user) is None:
        cart.update({request.user: []})
    for item in cart[request.user]:
        if Puzzle.objects.get(id=id_puzzle) in item:
            break
    else:
        cart[request.user].append([Puzzle.objects.get(id=id_puzzle), request.GET['quantity']])
    return redirect('/katalog')


def my_basket(request):
    basket_users = cart.get(request.user)
    form = BuyerForm()
    total = 0
    if basket_users is None:
        return render(request, 'katalog/cart.html', {'cart': basket_users, 'total': total})
    for item in basket_users:
        total += item[0].price * int(item[1])
    return render(request, 'katalog/cart.html', {'cart': basket_users, 'total': total,'form':form})


def remove_puzzle_in_basket(request, id_puzzle):
    basket_users = cart.get(request.user)
    for item in basket_users:
        if Puzzle.objects.get(id=id_puzzle) in item:
            basket_users.remove(item)
    return redirect('/katalog/my_basket/')
