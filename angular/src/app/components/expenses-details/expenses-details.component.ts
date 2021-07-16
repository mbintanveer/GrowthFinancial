import { Component, OnInit } from '@angular/core';
import { ExpenseService } from 'src/app/services/expense.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Expense } from 'src/app/models/expense.model';

@Component({
  selector: 'app-expense-details',
  templateUrl: './expenses-details.component.html',
  styleUrls: ['./expenses-details.component.css']
})

export class ExpensesDetailsComponent implements OnInit {
  currentExpense: Expense = {
    expense_id: '',
    expense_type: '',
    expense_amount: 0,
    date_created:'',
    
  };
  message = '';

  constructor(
    private expenseService: ExpenseService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getExpense(this.route.snapshot.params.id);
      console.log('hi')
    }
  
    getExpense(id: string): void {
      this.expenseService.get(id)
        .subscribe(
          data => {
            this.currentExpense = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        expense_id: this.currentExpense.expense_id,
        expense_type: this.currentExpense.expense_type,
        expense_amount: 0,
        date_created:'',
      };
  
      this.message = '';
  
      this.expenseService.update(this.currentExpense.expense_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateExpense(): void {
  
      this.expenseService.update(this.currentExpense.expense_id, this.currentExpense)
        .subscribe(
            
          error => {
            console.log(error);
          });
        this.router.navigate(['/Expenses']);
          
    }
  
    deleteExpense(): void {
      this.expenseService.delete(this.currentExpense.expense_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This expense was deleted successfully!';
            this.router.navigate(['/Expenses']);
          },
          error => {
            console.log(error);
          });
    }
  }

