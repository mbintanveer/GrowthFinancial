import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Payment } from '../models/payment.model';

const baseUrl = 'http://localhost:8000/api/Payments';

@Injectable({
  providedIn: 'root'
})

export class PaymentService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Payment[]> {
    return this.http.get<Payment[]>(baseUrl);
  }

  get(id: any): Observable<Payment> {
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

  findByTitle(title: any): Observable<Payment[]> {
    return this.http.get<Payment[]>(`${baseUrl}?title=${title}`);
  }

  findByVendor(payment_vendor_id: any): Observable<Payment[]> {
    return this.http.get<Payment[]>(`${baseUrl}?payment_vendor_id=${payment_vendor_id}`);
  }

}

