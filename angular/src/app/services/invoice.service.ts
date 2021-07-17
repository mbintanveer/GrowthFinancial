import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Invoice } from '../models/invoice.model';

const baseUrl = 'http://localhost:8000/api/Invoices';

@Injectable({
  providedIn: 'root'
})

export class InvoiceService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(baseUrl);
  }

  get(id: any): Observable<Invoice> {
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

  findByTitle(title: any): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(`${baseUrl}?title=${title}`);
  }

  findByClient(invoice_client_id: any): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(`${baseUrl}?invoice_client_id=${invoice_client_id}`);
  }

}

