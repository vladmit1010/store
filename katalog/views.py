from django.shortcuts import render
from .models import Company, Puzzle, TypePuzzle
from .forms import PuzzleForm


def home(request):
    form = PuzzleForm
    puzzles = Puzzle.objects.all()
    type_puzzle = TypePuzzle.objects.all().order_by('name')
    company_puzzle = Company.objects.all()
    return render(request, 'katalog/index.html',
                  {'puzzles': puzzles, 'type_puzzle': type_puzzle, 'company_puzzle': company_puzzle, 'form': form})


def about(request):
    return render(request, 'katalog/about.html')


def catalog(request):
    return render(request, 'katalog/contact.html')


def about_puzzle(request, id_puuzle):
    puzzle = Puzzle.objects.get(id=id_puuzle)
    return render(request, 'katalog/about_puzzle.html', {'puzzle': puzzle})


def filter(request):
    form = PuzzleForm
    puzzles = Puzzle.objects.all()
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
