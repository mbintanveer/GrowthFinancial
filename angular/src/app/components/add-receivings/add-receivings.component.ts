import { Component, OnInit } from '@angular/core';
import { Receiving } from 'src/app/models/receiving.model';
import { ReceivingService } from 'src/app/services/receiving.service';
import { Client} from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-receiving',
  templateUrl: './add-receivings.component.html',
  styleUrls: ['./add-receivings.component.css']
})

export class AddReceivingsComponent implements OnInit {
  receiving: Receiving = {
    receiving_id: '',
    receiving_description: '',
    receiving_amount: 0,
    date_created: '2020-01-01',
  
  };
  clients?: Client[];
  submitted = false;

  constructor (private receivingService: ReceivingService,
    private clientService: ClientService,
    private router: Router){ }

  ngOnInit(): void {
    this.retrieveClients();
  }

  retrieveClients(): void {
    this.clientService.getAll()
      .subscribe(
        data => {
          this.clients = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  saveReceiving(): void {
    const data = {
      receiving_id: this.receiving.receiving_id,
      receiving_description: this.receiving.receiving_description,
      receiving_amount:this.receiving.receiving_amount,
      date_created: this.receiving.date_created,
      receiving_client:this.receiving.receiving_client

    };
    

    this.receivingService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Receivings']);
        },
        error => {
          console.log(error);
        });
  }

  newReceiving(): void {
    this.submitted = false;
    this.receiving = {
      receiving_description: '',
      
    };
     
  }
}