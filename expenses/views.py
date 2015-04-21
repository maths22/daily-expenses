from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.db.models import Sum, Count
from django.utils import timezone
from .models import Expense
from .forms import ExpenseForm

def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            form = ExpenseForm()
    else:
        form = ExpenseForm()
        
    expense_list = Expense.objects.order_by('-date')
    expense_by_day = Expense.objects.values('date').annotate(Count('price'),Sum('price'))
    expense_totals = Expense.objects.aggregate(Count('price'),Sum('price'))
    
    context = {'form': form,'expense_list': expense_list,'expense_by_day': expense_by_day,'expense_totals': expense_totals}
    return render(request, 'expenses/index.html', context)
