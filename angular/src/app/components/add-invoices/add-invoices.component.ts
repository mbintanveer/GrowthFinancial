import { Component, OnInit } from '@angular/core';
import { Invoice } from 'src/app/models/invoice.model';
import { InvoiceService } from 'src/app/services/invoice.service';

import { Client} from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';

import { Router } from '@angular/router';

@Component({
  selector: 'app-add-invoice',
  templateUrl: './add-invoices.component.html',
  styleUrls: ['./add-invoices.component.css']
})

export class AddInvoicesComponent implements OnInit {
  invoice: Invoice = {
    invoice_id: '',
    invoice_description: '',
    invoice_status: '',
    // invoice_amount: 0,
    date_created: '2020-01-01',
  };
  submitted = false;
  clients?: Client[];

  constructor (private invoiceService: InvoiceService,
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

  saveInvoice(): void {
    const data = {
      invoice_id: this.invoice.invoice_id,
      invoice_description: this.invoice.invoice_description,
      // invoice_amount:this.invoice.invoice_amount,
      date_created: this.invoice.date_created,
      invoice_client:this.invoice.invoice_client,
      invoice_status:this.invoice.invoice_status
    };
    

    this.invoiceService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Invoices']);
        },
        error => {
          console.log(error);
        });
  }

  newInvoice(): void {
    this.submitted = false;
    this.invoice = {
      invoice_description: '',
      
    };
     
  }
}