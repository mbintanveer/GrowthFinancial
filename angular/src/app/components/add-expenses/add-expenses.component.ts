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
    expense_amount: 0,
    date_created: '2020-01-01',
    

  };
  submitted = false;

  constructor (private expenseService: ExpenseService,
    private router: Router){ }

  ngOnInit(): void {
  }

  saveExpense(): void {
    const data = {
      expense_id: this.expense.expense_id,
      expense_type: this.expense.expense_type,
      expense_amount:this.expense.expense_amount,
      date_created: this.expense.date_created,


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