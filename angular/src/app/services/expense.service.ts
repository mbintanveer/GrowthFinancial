import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Expense } from '../models/expense.model';

const baseUrl = 'http://localhost:8000/api/Expenses';

@Injectable({
  providedIn: 'root'
})

export class ExpenseService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Expense[]> {
    return this.http.get<Expense[]>(baseUrl);
  }

  get(id: any): Observable<Expense> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByTitle(title: any): Observable<Expense[]> {
    return this.http.get<Expense[]>(`${baseUrl}?title=${title}`);
  }

  findByExpenseType(expense_type: any): Observable<Expense[]> {
    return this.http.get<Expense[]>(`${baseUrl}?expense_type_keyword=${expense_type}`);
  }

}

