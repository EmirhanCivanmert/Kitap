from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import BookCreateForm, BookEditForm, UploadForm
from .models import Kitap, Category, Slider, UploadModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    kitaplar = Kitap.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()
    sliders = Slider.objects.filter(is_active=True)
    
    return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'books' : kitaplar,
        'sliders': sliders,
    })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_book(request):
    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/kitaplar")
    else:
            form = BookCreateForm()
    return render(request, "courses/create-book.html", {"form":form})

@login_required()
def book_list(request):
    kitaplar = Kitap.objects.all() #queryset
    return render(request, 'courses/book-list.html', {
        'books': kitaplar
    })

def book_edit(request, id):
    book = get_object_or_404(Kitap, pk=id)
    
    if request.method == "POST":
        form = BookEditForm(request.POST, request.FILES, instance=book)
        form.save()
        return redirect("book_list")
    else:
        form = BookEditForm(instance=book)
    
    return render(request, "courses/edit-book.html", { "form":form })

def book_delete(request, id):
    book = get_object_or_404(Kitap, pk=id)

    if request.method == "POST":
        book.delete() # Kitap.objects.get(pk=id).delete()
        return redirect("book_list")

    return render(request, "courses/book-delete.html", { "book":book })

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
        return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", { "form":form })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kitaplar = Kitap.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kitaplar")

    return render(request, 'courses/search.html', {
        'categories' : kategoriler,
        'books' : kitaplar,
    })

def details(request, slug):

    book = get_object_or_404(Kitap, slug=slug)

    context = {
        'book': book
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kitaplar = Kitap.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kitaplar, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories' : kategoriler,
        'page_obj' : page_obj,
        'seciliKategori': slug,
    })