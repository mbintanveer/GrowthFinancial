import { Component, OnInit } from '@angular/core';
import { InvoiceService } from 'src/app/services/invoice.service';
import { ActivatedRoute, Router } from '@angular/router';

import { Client} from 'src/app/models/client.model';
import { ClientService } from 'src/app/services/client.service';
import { Invoice } from 'src/app/models/invoice.model';

@Component({
  selector: 'app-invoice-details',
  templateUrl: './invoices-details.component.html',
  styleUrls: ['./invoices-details.component.css']
})

export class InvoicesDetailsComponent implements OnInit {
  
  status : any = "4";
  currentInvoice: Invoice = {
    invoice_id: '',
    invoice_description: '',
    // invoice_amount: 0,
    invoice_client:'',
    date_created:''
    ,
    
  };
  message = '';
  clients?: Client[];
  constructor(
    private invoiceService: InvoiceService,
    private clientService: ClientService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.retrieveClients();
      this.getInvoice(this.route.snapshot.params.id);
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

    getInvoice(id: string): void {
      this.invoiceService.get(id)
        .subscribe(
          data => {
            this.currentInvoice = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        invoice_id: this.currentInvoice.invoice_id,
        invoice_description: this.currentInvoice.invoice_description,
        // invoice_amount: 0,
        date_created:'',
        invoice_client:'',
      };
  
      this.message = '';
  
      this.invoiceService.update(this.currentInvoice.invoice_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateInvoice(): void {
  
      this.invoiceService.update(this.currentInvoice.invoice_id, this.currentInvoice)
        .subscribe(
            
          error => {
            console.log(error);
          });
        this.router.navigate(['/View-Clients/'+this.currentInvoice.invoice_client]);
          
    }
  
    deleteInvoice(): void {
      this.invoiceService.delete(this.currentInvoice.invoice_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This invoice was deleted successfully!';
            this.router.navigate(['/View-Clients/'+this.currentInvoice.invoice_client]);
          },
          error => {
            console.log(error);
          });
    }
  }

