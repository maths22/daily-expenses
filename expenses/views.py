from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils import timezone
from .models import Expense

def index(request):
    expense_list = Expense.objects.order_by('-date')
    context = {'expense_list': expense_list}
    return render(request, 'expenses/index.html', context)

def add(request):
    new_expense = Expense(item=request.POST['item'],price=request.POST['price'],date=timezone.now())
    new_expense.save()
    return HttpResponseRedirect(reverse('expenses:index'))
