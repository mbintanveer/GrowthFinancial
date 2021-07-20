import { Component, OnInit } from '@angular/core';
import { ClientService } from 'src/app/services/client.service';
import { Client } from 'src/app/models/client.model';
import { Client_Summary } from 'src/app/models/client.model';
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
  invoice_page = 1;
  receiving_page = 1;

  count = 0;
  tableSize = 10;
  tableSizesArr = [10];

  receivings?: any;
  currentReceiving: Receiving = {};

  invoices?: any;
  currentInvoice: Invoice = {};

  currentIndex = -1;
  currentClient: Client = {
    client_id: '',
    client_name: '',}

  getClientSummary:Client_Summary ={
    client_name:'',
    get_one_month: 0,
    get_two_month: 0,
    get_three_month: 0,
    get_four_month: 0,
    get_total: 0,
  }
 


  constructor(private receivingService: ReceivingService,
    private invoiceService: InvoiceService,
    private clientService: ClientService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {

    this.getClient(this.route.snapshot.params.id);
    this.retrieveReceivings(this.route.snapshot.params.id);
    this.retrieveInvoices(this.route.snapshot.params.id);
    this.get_Client_Summary(this.route.snapshot.params.id);
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

  get_Client_Summary(id: string): void {
    this.clientService.get_Client_Summary(id)
      .subscribe(
        data => {
          this.getClientSummary = data;
          console.log(this.currentClient);
        },
        error => {
          console.log(error);
        });
  }

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
  
  invoices_tabSize(event:any){
    this.invoice_page = event;
    this.retrieveInvoices(this.currentClient.client_id)
  }  

  receivings_tabSize(event:any){
    this.receiving_page = event;
    this.retrieveReceivings(this.currentClient.client_id);
    

  }  



  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.invoice_page = 1;
    this.receiving_page = 1;

    this.retrieveReceivings(this.currentClient.client_id);
  } 


  

}
