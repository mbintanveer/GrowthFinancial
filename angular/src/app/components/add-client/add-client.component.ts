import { Component, OnInit } from '@angular/core';
import { Client } from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';

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

  constructor (private clientService: ClientService){ }

  ngOnInit(): void {
  }

  saveClient(): void {
    const data = {
      id: this.client.client_id,
      name: this.client.client_name
    };

    this.clientService.create(data)
      .subscribe(
        response => {
          console.log(response);
        },
        error => {
          console.log(error);
        });
  }

  newClient(): void {

    this.client = {
      client_id: '',
      client_name: '',
      
    };
  }


}
