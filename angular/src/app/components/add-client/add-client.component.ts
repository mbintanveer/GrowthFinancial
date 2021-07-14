import { Component, OnInit } from '@angular/core';
import { Client } from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-add-client',
  templateUrl: './add-client.component.html',
  styleUrls: ['./add-client.component.css']
})

export class AddClientComponent implements OnInit {
  client: Client = {
    client_id: '',
    client_name: '',

  };
  submitted = false;

  constructor (private clientService: ClientService,
    private router: Router){ }

  ngOnInit(): void {
  }

  saveClient(): void {
    const data = {
      client_id: this.client.client_id,
      client_name: this.client.client_name
    };
    

    this.clientService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Clients']);
        },
        error => {
          console.log(error);
        });
  }

  newClient(): void {
    this.submitted = false;
    this.client = {
      client_name: '',
      
    };
     
  }
}