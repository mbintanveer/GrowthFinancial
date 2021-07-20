import { Component, OnInit } from '@angular/core';
import { Client } from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.css']
})

 
export class ClientsListComponent implements OnInit {

  // clients?: Client[];
  currentClient: Client = {};
  currentIndex = -1;
  client_name = '';

  clients: any;
  page = 1;
  count = 0;
  tableSize = 10;
  // tableSizesArr = [1];

  constructor(private clientService: ClientService) { }

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
  
  tabSize(event:any){
    this.page = event;
    //this.retrieveClients();
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrieveClients();
  } 

  refreshList(): void {
    this.retrieveClients();
    this.currentClient = {};
    this.currentIndex = -1;
  }

  setActiveClient(client: Client, index: number): void {
    this.currentClient = client;
    this.currentIndex = index;
  }

  removeAllClients(): void {
    this.clientService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.refreshList();
        },
        error => {
          console.log(error);
        });
  }

  searchClient(): void {
    this.currentClient = {};
    this.currentIndex = -1;

    this.clientService.findByClientName(this.client_name)
      .subscribe(
        data => {
          this.clients = data;
          this.page=1
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
}


