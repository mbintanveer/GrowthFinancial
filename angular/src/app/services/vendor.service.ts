import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vendor } from '../models/vendor.model';

const baseUrl = 'http://localhost:8000/api/Vendors';
const summaryUrl = 'http://localhost:8000/api/Vendors_Summary'
const all_summary_Url='http://localhost:8000/api/All_Vendors_Summary'

@Injectable({
  providedIn: 'root'
})

export class VendorService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Vendor[]> {
    return this.http.get<Vendor[]>(baseUrl);
  }

  get(id: any): Observable<Vendor> {
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

  findByTitle(title: any): Observable<Vendor[]> {
    return this.http.get<Vendor[]>(`${baseUrl}?title=${title}`);
  }

  get_Vendor_Summary(id: any): Observable<Vendor> {
    return this.http.get(`${summaryUrl}/${id}`);
  }

  get_all_vendor_summaries(): Observable<any> {
    return this.http.get(all_summary_Url);
  }

  

  findByVendorName(vendor_name: any): Observable<Vendor[]> {
    return this.http.get<Vendor[]>(`${baseUrl}?vendor_name_keyword=${vendor_name}`);
  }

}

