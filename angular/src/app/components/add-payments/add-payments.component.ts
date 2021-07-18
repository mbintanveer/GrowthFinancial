import { Component, OnInit } from '@angular/core';
import { Payment } from 'src/app/models/payment.model';
import { PaymentService } from 'src/app/services/payment.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-payment',
  templateUrl: './add-payments.component.html',
  styleUrls: ['./add-payments.component.css']
})

export class AddPaymentsComponent implements OnInit {
  payment: Payment = {
    payment_id: '',
    payment_description: '',
    payment_amount: 0,
    date_created: '2020-01-01',
  };
  submitted = false;

  constructor (private paymentService: PaymentService,
    private router: Router){ }

  ngOnInit(): void {
  }

  savePayment(): void {
    const data = {
      payment_id: this.payment.payment_id,
      payment_description: this.payment.payment_description,
      payment_amount:this.payment.payment_amount,
      date_created: this.payment.date_created,
      payment_vendor:this.payment.payment_vendor

    };
    

    this.paymentService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Payments']);
        },
        error => {
          console.log(error);
        });
  }

  newPayment(): void {
    this.submitted = false;
    this.payment = {
      payment_description: '',
      
    };
     
  }
}