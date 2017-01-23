from django.shortcuts import render, get_object_or_404
from .models import Fact
from .forms import FactForm
from django.shortcuts import redirect
# Create your views here.
def fact_show(request):
    facts = Fact.objects.all()
    return render(request, 'fact_bot_portal/fact_show.html', {'facts': facts})

def fact_new(request):
    if request.method == "POST":
        form = FactForm(request.POST)
        if form.is_valid():
            fact = form.save(commit=False)
            fact.save()
            return redirect('/')
    else:
        form = FactForm()
    return render(request, 'fact_bot_portal/fact_edit.html', {'form': form})

def fact_detail(request, pk):
    fact = get_object_or_404(Fact, pk=pk)
    return render(request, 'fact_bot_portal/fact_detail.html', {'fact': fact})

def fact_remove(request, pk):
    fact = get_object_or_404(Fact, pk=pk)
    fact.delete()
    return redirect('fact_show')
