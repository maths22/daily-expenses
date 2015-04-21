from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Expense
from django.utils import timezone
from datetime import timedelta

class ExpenseViewTests(TestCase):
    def test_index_view_no_expenses(self):
        response = self.client.get(reverse('expenses:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No expenses have been recorded.")
        self.assertQuerysetEqual(response.context['expense_list'], [])
    def test_index_view_one_expense(self):
        Expense(item="food", price="7.89", date=timezone.now()).save()
        response = self.client.get(reverse('expenses:index'))
        self.assertQuerysetEqual(response.context['expense_list'], ['<Expense: food>'])
    def test_index_view_multiple_expenses(self):
        Expense(item="food1", price="7.89", date=timezone.now()).save()
        Expense(item="food2", price="7.89", date=timezone.now()-timedelta(days=2)).save()
        Expense(item="food3", price="7.89", date=timezone.now()-timedelta(days=1)).save()
        response = self.client.get(reverse('expenses:index'))
        self.assertQuerysetEqual(response.context['expense_list'], ['<Expense: food1>','<Expense: food3>','<Expense: food2>'])
