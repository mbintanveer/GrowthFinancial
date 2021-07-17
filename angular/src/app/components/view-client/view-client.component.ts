import { Component, OnInit } from '@angular/core';
import { ClientService } from 'src/app/services/client.service';
import { Client } from 'src/app/models/client.model';
import { ActivatedRoute, Router } from '@angular/router';

import { Receiving } from 'src/app/models/receiving.model';
import { ReceivingService } from 'src/app/services/receiving.service';

import { Invoice } from 'src/app/models/invoice.model';
import { InvoiceService } from 'src/app/services/invoice.service';


@Component({
  selector: 'app-view-client',
  templateUrl: './view-client.component.html',
  styleUrls: ['./view-client.component.css']
})

export class ViewClientComponent implements OnInit {
  page = 1;
  count = 0;
  tableSize = 5;
  tableSizesArr = [5];

  receivings?: any;
  currentReceiving: Receiving = {};

  invoices?: any;
  currentInvoice: Invoice = {};

  currentIndex = -1;
  currentClient: Client = {
    client_id: '',
    client_name: '',
  };

  constructor(private receivingService: ReceivingService,
    private invoiceService: InvoiceService,
    private clientService: ClientService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {

    this.getClient(this.route.snapshot.params.id);
    this.retrieveReceivings(this.route.snapshot.params.id);
    this.retrieveInvoices(this.route.snapshot.params.id);
  }
  
  getClient(id: string): void {
    this.clientService.get(id)
      .subscribe(
        data => {
          this.currentClient = data;
          console.log(this.currentClient);
        },
        error => {
          console.log(error);
        });
  }

// receiving_client_id: any
  retrieveReceivings(id: string): void {

    this.receivingService.findByClient(id)
      .subscribe(
        data => {
          this.receivings = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  retrieveInvoices(id: string): void {

    this.invoiceService.findByClient(id)
      .subscribe(
        data => {
          this.invoices = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveReceivings(this.currentClient.client_id);
    this.retrieveInvoices(this.currentClient.client_id);
    this.currentReceiving = {};
    this.currentInvoice = {};
    this.currentIndex = -1;
  }

  setActiveReceiving(receiving: Receiving, index: number): void {
    this.currentReceiving =receiving;
    this.currentIndex = index;
  }

  setActiveInvoice(invoice: Invoice, index: number): void {
    this.currentInvoice =invoice;
    this.currentIndex = index;
  }

  tabSize(event:any){
    this.page = event;
    this.retrieveReceivings(this.currentClient.client_id);
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrieveReceivings(this.currentClient.client_id);
  } 


  

}
