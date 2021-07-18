import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Bill } from '../models/bill.model';

const baseUrl = 'http://localhost:8000/api/Bills';

@Injectable({
  providedIn: 'root'
})

export class BillService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Bill[]> {
    return this.http.get<Bill[]>(baseUrl);
  }

  get(id: any): Observable<Bill> {
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

  findByTitle(title: any): Observable<Bill[]> {
    return this.http.get<Bill[]>(`${baseUrl}?title=${title}`);
  }

  findByVendor(bill_vendor_id: any): Observable<Bill[]> {
    return this.http.get<Bill[]>(`${baseUrl}?bill_vendor_id=${bill_vendor_id}`);
  }

}

