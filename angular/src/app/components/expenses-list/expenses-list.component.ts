import { Component, OnInit } from '@angular/core';
import { Expense } from 'src/app/models/expense.model';
import { ExpenseService } from 'src/app/services/expense.service';


@Component({
  selector: 'app-expense-list',
  templateUrl: './expenses-list.component.html',
  styleUrls: ['./expenses-list.component.css']
})


export class ExpensesListComponent implements OnInit {

  expenses?: any;
  currentExpense: Expense = {};
  currentIndex = -1;
  title = '';
  page = 1;
  count = 0;
  tableSize = 10;

  constructor(private expenseService: ExpenseService) { }

  ngOnInit(): void {
    this.retrieveExpenses();
  }

  
  retrieveExpenses(): void {
    this.expenseService.getAll()
      .subscribe(
        data => {
          this.expenses = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
  
  refreshList(): void {
    this.retrieveExpenses();
    this.currentExpense = {};
    this.currentIndex = -1;
  }
    
  tabSize(event:any){
    this.page = event;
    //this.retrieveClients();
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrieveExpenses();
  } 

  setActiveExpense(expense: Expense, index: number): void {
    this.currentExpense =expense;
    this.currentIndex = index;
  }


  // searchTitle(): void {
  //   this.currentClient = {};
  //   this.currentIndex = -1;

  //   this.clientService.findByTitle(this.title)
  //     .subscribe(
  //       data => {
  //         this.clients = data;
  //         console.log(data);
  //       },
  //       error => {
  //         console.log(error);
  //       });
  // }
}


