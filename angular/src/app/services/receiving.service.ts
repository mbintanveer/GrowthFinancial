import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Receiving } from '../models/receiving.model';

const baseUrl = 'http://localhost:8000/api/Receivings';

@Injectable({
  providedIn: 'root'
})

export class ReceivingService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Receiving[]> {
    return this.http.get<Receiving[]>(baseUrl);
  }

  get(id: any): Observable<Receiving> {
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

  findByTitle(title: any): Observable<Receiving[]> {
    return this.http.get<Receiving[]>(`${baseUrl}?title=${title}`);
  }
}

