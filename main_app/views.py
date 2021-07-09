from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hairpun, Visit

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hairpuns_index(request):
  hairpuns = Hairpun.objects.all()
  return render(request, 'hairpuns/index.html', {'hairpuns': hairpuns})

def hairpuns_details(request, pun_id):
  hairpun = Hairpun.objects.get(id=pun_id)
  return render(request, 'hairpuns/details.html', {'pun':hairpun})

class HairpunCreate(CreateView):
  model = Hairpun
  fields = '__all__'

class HairpunUpdate(UpdateView):
  model = Hairpun
  fields = '__all__'

class HairpunDelete(DeleteView):
  model = Hairpun
  success_url = '/hairpuns/'

def visit_create(request):
  data = request.POST.dict()
  del data['csrfmiddlewaretoken']
  Visit.objects.create(**data)
  return redirect('details', pun_id=data['hairpun_id'])
