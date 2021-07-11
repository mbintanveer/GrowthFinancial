from rest_framework import serializers
from Expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('expense_id',
                'date_created',
                'expense_amount',
               # 'type_choices',
                'expense_type')
               

