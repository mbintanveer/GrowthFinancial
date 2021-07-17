import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Client } from '../models/client.model';

const baseUrl = 'http://localhost:8000/api/Clients';

@Injectable({
  providedIn: 'root'
})

export class ClientService {
  constructor(private http: HttpClient) { }

  getAll(): Observable<Client[]> {
    return this.http.get<Client[]>(baseUrl);
  }

  get(id: any): Observable<Client> {
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

  findByClientName(client_name: any): Observable<Client[]> {
    return this.http.get<Client[]>(`${baseUrl}?client_name_keyword=${client_name}`);
  }
}

