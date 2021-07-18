import { Component, OnInit } from '@angular/core';
import { Bill } from 'src/app/models/bill.model';
import { BillService } from 'src/app/services/bill.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-bill',
  templateUrl: './add-bills.component.html',
  styleUrls: ['./add-bills.component.css']
})

export class AddBillsComponent implements OnInit {
  bill: Bill = {
    bill_id: '',
    bill_description: '',
    bill_amount: 0,
    date_created: '2020-01-01',
    bill_vendor:''

  };
  submitted = false;

  constructor (private billService: BillService,
    private router: Router){ }

  ngOnInit(): void {
  }

  saveBill(): void {
    const data = {
      bill_id: this.bill.bill_id,
      bill_description: this.bill.bill_description,
      bill_amount:this.bill.bill_amount,
      date_created: this.bill.date_created,
      bill_vendor:this.bill.bill_vendor,
      // bill_status:this.bill.bill_status
    };
    

    this.billService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Bills']);
        },
        error => {
          console.log(error);
        });
  }

  newBill(): void {
    this.submitted = false;
    this.bill = {

      bill_description: '',
    };
     
  }
}