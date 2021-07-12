import { Component, OnInit } from '@angular/core';
import { ClientService } from 'src/app/services/client.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Client } from 'src/app/models/client.model';

@Component({
  selector: 'app-client-details',
  templateUrl: './client-details.component.html',
  styleUrls: ['./client-details.component.css']
})

export class ClientDetailsComponent implements OnInit {
  currentClient: Client = {
    client_id: '',
    client_name: '',
  };
  message = '';

  constructor(
    private clientService: ClientService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getClient(this.route.snapshot.params.id);
    }
  
    getClient(id: string): void {
      this.clientService.get(id)
        .subscribe(
          data => {
            this.currentClient = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        client_id: this.currentClient.client_id,
        client_name: this.currentClient.client_name
      };
  
      this.message = '';
  
      this.clientService.update(this.currentClient.client_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateClient(): void {
      this.message = '';
  
      this.clientService.update(this.currentClient.client_id, this.currentClient)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'This client was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    deleteClient(): void {
      this.clientService.delete(this.currentClient.client_id)
        .subscribe(
          response => {
            console.log(response);
            this.router.navigate(['/clients']);
          },
          error => {
            console.log(error);
          });
    }
  }

