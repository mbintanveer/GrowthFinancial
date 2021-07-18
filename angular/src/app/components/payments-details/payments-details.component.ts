import { Component, OnInit } from '@angular/core';
import { PaymentService } from 'src/app/services/payment.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Payment } from 'src/app/models/payment.model';

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

  constructor(
    private paymentService: PaymentService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getPayment(this.route.snapshot.params.id);
      console.log('hi')
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
        this.router.navigate(['/Payments']);
          
    }
  
    deletePayment(): void {
      this.paymentService.delete(this.currentPayment.payment_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This payment was deleted successfully!';
            this.router.navigate(['/Payments']);
          },
          error => {
            console.log(error);
          });
    }
  }

