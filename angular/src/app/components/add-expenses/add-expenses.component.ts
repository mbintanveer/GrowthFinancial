import { Component, OnInit } from '@angular/core';
import { Expense } from 'src/app/models/expense.model';
import { ExpenseService } from 'src/app/services/expense.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-expense',
  templateUrl: './add-expenses.component.html',
  styleUrls: ['./add-expenses.component.css']
})

export class AddExpensesComponent implements OnInit {
  expense: Expense = {
    expense_id: '',
    expense_type: '',

  };
  submitted = false;

  constructor (private expenseService: ExpenseService,
    private router: Router){ }

  ngOnInit(): void {
  }

  saveExpense(): void {
    const data = {
      expense_id: this.expense.expense_id,
      expense_name: this.expense.expense_type
    };
    

    this.expenseService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Expenses']);
        },
        error => {
          console.log(error);
        });
  }

  newExpense(): void {
    this.submitted = false;
    this.expense = {
      expense_type: '',
      
    };
     
  }
}