from django.shortcuts import render, get_object_or_404
from .models import Professor, Alumne
from django.http import Http404

# Simulació d'una llista de professors (en absència d'una base de dades)
'''PROFESSORS = [
    {
        'id': 1,
        'nom': 'Roger',
        'cognom1': 'Sobrino',
        'cognom2': 'Smith',
        'correu': 'rogersobrino@example.com',
        'curs': 'DAW2',
        'tutor': True,
        'moduls_imparteix': 'Entorn servidor, Projecte',
    },
    {
        'id': 2,
        'nom': 'Montse',
        'cognom1': 'Calopa',
        'cognom2': 'Johnson',
        'correu': 'montsecalopa@example.com',
        'curs': 'DAM2',
        'tutor': False,
        'moduls_imparteix': 'Machine Learning, Entorn client',
    },
    {
        'id': 3,
        'nom': 'Juanma',
        'cognom1': 'Carter',
        'cognom2': '',
        'correu': 'juanmacarter@example.com',
        'curs': 'Intel·ligència artificial',
        'tutor': True,
        'moduls_imparteix': 'Desplegament de aplicacions, Machine Learning',
    },
    {
        'id': 4,
        'nom': 'Oriol',
        'cognom1': 'Brown',
        'cognom2': 'Taylor',
        'correu': 'oriolrown@example.com',
        'curs': 'DAW1',
        'tutor': False,
        'moduls_imparteix': 'Entorn client, Sistemes',
    },
]
ALUMNES = [
    {
        'id': 1,
        'nom': 'Iris',
        'cognom1': 'Vilaseca',
        'cognom2': 'Smith',
        'correu': 'iris@example.com',
        'curs': 'DAW2',
        'moduls_matriculats': 'Entorn servidor, Projecte',
    },
    {
        'id': 2,
        'nom': 'Milena',
        'cognom1': 'Rodriguez',
        'cognom2': 'Johnson',
        'correu': 'milena@example.com',
        'curs': 'DAM2',
        'moduls_matriculats': 'Machine Learning, Entorn client',
    },
    {
        'id': 3,
        'nom': 'Javi',
        'cognom1': 'Carter',
        'cognom2': '',
        'correu': 'javicarter@example.com',
        'curs': 'Intel·ligència artificial',
        'moduls_matriculats': 'Desplegament de aplicacions, Machine Learning',
    },
    {
        'id': 4,
        'nom': 'Dani',
        'cognom1': 'Brown',
        'cognom2': 'Taylor',
        'correu': 'dani@example.com',
        'curs': 'DAW1',
        'moduls_matriculats': 'Entorn client, Sistemes',
    },
]
'''
def get_professor_by_id(professors, id):
    # Filtra la llista per trobar el valor especificat
    filtered = filter(lambda prof: prof["id"] == id, professors)
    return next(filtered, None)  # Retorna el primer element coincident o none

def get_alumne_by_id(alumnes,id):
    filtered=filter(lambda alum: alum["id"]==id,alumnes)
    return next(filtered, None)


# Llistat de professors
def llistat_professors(request):
    #return render(request, 'teachers.html', {'professors': PROFESSORS})
    professors = Professor.objects.all()  # Recuperar tots els estudiants de la base de dades
    return render(request, 'teachers.html', {'professors': professors})

def detall_professor(request, id):
    '''professor = get_professor_by_id(PROFESSORS, id)
    if professor:
        return render(request, 'professor_detail.html', {'professor': professor})
    else:
        # Raise a 404 error if the professor is not found
        raise Http404(f"El professor amb ID {id} no existeix.")'''
    professor=get_object_or_404(Professor,id=id)
    return render(request,'professor_detail.html',{'professor':professor})
# Llistat d'alumnes
def llistat_alumnes(request):
    alumnes = Alumne.objects.all()
    return render(request, 'students.html', {'alumnes': alumnes})

# Detall d'un alumne
def detall_alumne(request, id):
    '''alumne = get_alumne_by_id(ALUMNES, id)
    if alumne:
        return render(request, 'alumne_detail.html', {'alumne': alumne})'''
    alumne=get_object_or_404(Alumne,id=id)
    return render(request,'alumne_detail.html',{'alumne':alumne})
