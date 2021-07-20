import { Component, OnInit } from '@angular/core';
import { PaymentService } from 'src/app/services/payment.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Payment } from 'src/app/models/payment.model';


import { Vendor} from 'src/app/models/vendor.model';
import { VendorService } from 'src/app/services/vendor.service';

@Component({
  selector: 'app-payment-details',
  templateUrl: './payments-details.component.html',
  styleUrls: ['./payments-details.component.css']
})

export class PaymentsDetailsComponent implements OnInit {
  currentPayment: Payment = {
    payment_id: '',
    payment_description: '',
    payment_amount: 0,
    payment_vendor:'',
    date_created:''
    ,
    
  };
  message = '';
  vendors?: Vendor[];
  
  constructor(
    private paymentService: PaymentService,
    private vendorService: VendorService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getPayment(this.route.snapshot.params.id);
      this.retrieveVendors();
    }
  
    retrieveVendors(): void {
      this.vendorService.getAll()
        .subscribe(
          data => {
            this.vendors = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }

    getPayment(id: string): void {
      this.paymentService.get(id)
        .subscribe(
          data => {
            this.currentPayment = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        payment_id: this.currentPayment.payment_id,
        payment_description: this.currentPayment.payment_description,
        payment_amount: 0,
        date_created:'',
        payment_vendor:'',
      };
  
      this.message = '';
  
      this.paymentService.update(this.currentPayment.payment_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updatePayment(): void {
  
      this.paymentService.update(this.currentPayment.payment_id, this.currentPayment)
        .subscribe(
            
          error => {
            console.log(error);
          });
          this.router.navigate(['/View-Vendors/'+this.currentPayment.payment_vendor]);
          
    }
  
    deletePayment(): void {
      this.paymentService.delete(this.currentPayment.payment_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This payment was deleted successfully!';
            this.router.navigate(['/View-Vendors/'+this.currentPayment.payment_vendor]);
          },
          error => {
            console.log(error);
          });
    }
  }

