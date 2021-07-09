from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hairpun, Visit, Category

# Static pages 
# ------------
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Hairpuns 
# ------------
def hairpuns_index(request):
  hairpuns = Hairpun.objects.all()
  return render(request, 'hairpuns/index.html', {'hairpuns': hairpuns})

def hairpuns_details(request, pun_id):
  hairpun = Hairpun.objects.get(id=pun_id)
  categories_in = hairpun.categories.all()
  categories_not_in = list(filter(lambda cat: not cat in categories_in, Category.objects.all()))
  print('categories_in: ', categories_in, 'categories not in', categories_not_in)
  return render(request, 'hairpuns/details.html', {'pun':hairpun, 'categories_in':categories_in, 'categories_not_in':categories_not_in})

class HairpunCreate(CreateView):
  model = Hairpun
  fields = '__all__'

class HairpunUpdate(UpdateView):
  model = Hairpun
  fields = '__all__'

class HairpunDelete(DeleteView):
  model = Hairpun
  success_url = '/hairpuns/'

def assoc_category(request, pun_id, category_id):
  Hairpun.objects.get(id=pun_id).categories.add(category_id)
  return redirect('details', pun_id=pun_id)

def un_assoc_category(request, pun_id, category_id):
  Hairpun.objects.get(id=pun_id).categories.remove(category_id)
  return redirect('details', pun_id=pun_id)

# Add a visit POST 
# ------------
def visit_create(request):
  data = request.POST.dict()
  del data['csrfmiddlewaretoken']
  Visit.objects.create(**data)
  return redirect('details', pun_id=data['hairpun_id'])

# Categories 
# ------------
def categories_index(request):
  categories = Category.objects.all()
  return render(request, 'category/index.html', {'categories': categories})


def category_details(request, category_id):
  category = Category.objects.get(id=category_id)
  return render(request, 'category/details.html', {'category':category})

class CategoryCreate(CreateView):
  model = Category
  fields = '__all__'

class CategoryUpdate(UpdateView):
  model = Category
  fields = '__all__'

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/category/deleted'

def category_deleted(request):
  return render(request, 'generic_page.html', {'title':"Poof!", 'message':
  "You've deleted that category."})