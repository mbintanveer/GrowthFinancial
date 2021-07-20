import { Component, OnInit } from '@angular/core';
import { VendorService } from 'src/app/services/vendor.service';
import { Vendor } from 'src/app/models/vendor.model';
import { Vendor_Summary } from 'src/app/models/vendor.model';
import { ActivatedRoute, } from '@angular/router';

import { Payment } from 'src/app/models/payment.model';
import { PaymentService } from 'src/app/services/payment.service';

import { Bill } from 'src/app/models/bill.model';
import { BillService } from 'src/app/services/bill.service';


@Component({
  selector: 'app-view-vendor',
  templateUrl: './view-vendors.component.html',
  styleUrls: ['./view-vendors.component.css']
})

export class ViewVendorComponent implements OnInit {
  bill_page = 1;
  payment_page = 1;
  count = 0;
  tableSize = 10;
  tableSizesArr = [10];

  payments?: any;
  currentPayment: Payment = {};

  bills?: any;
  currentBill: Bill = {};

  currentIndex = -1;
  currentVendor: Vendor = {
    vendor_id: '',
    vendor_name: '',
  };

  getVendorSummary:Vendor_Summary ={
    vendor_name:'',
    get_one_month: 0,
    get_two_month: 0,
    get_three_month: 0,
    get_four_month: 0,
    get_total: 0,
  }

  constructor(private paymentService: PaymentService,
    private billService: BillService,
    private vendorService: VendorService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {

    this.getVendor(this.route.snapshot.params.id);
    this.retrievePayments(this.route.snapshot.params.id);
    this.retrieveBills(this.route.snapshot.params.id);
    this.get_Vendor_Summary(this.route.snapshot.params.id);
  }
  
  getVendor(id: string): void {
    this.vendorService.get(id)
      .subscribe(
        data => {
          this.currentVendor = data;
          console.log(this.currentVendor);
        },
        error => {
          console.log(error);
        });
  }

  get_Vendor_Summary(id: string): void {
    this.vendorService.get_Vendor_Summary(id)
      .subscribe(
        data => {
          this.getVendorSummary = data;

        },
        error => {
          console.log(error);
        });
  }


// payment_vendor_id: any
  retrievePayments(id: string): void {

    this.paymentService.findByVendor(id)
      .subscribe(
        data => {
          this.payments = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  retrieveBills(id: string): void {

    this.billService.findByVendor(id)
      .subscribe(
        data => {
          this.bills = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrievePayments(this.currentVendor.vendor_id);
    this.retrieveBills(this.currentVendor.vendor_id);
    this.currentPayment = {};
    this.currentBill = {};
    this.currentIndex = -1;
  }

  setActivePayment(payment: Payment, index: number): void {
    this.currentPayment =payment;
    this.currentIndex = index;
  }

  setActiveBill(bill: Bill, index: number): void {
    this.currentBill =bill;
    this.currentIndex = index;
  }

  bill_tabSize(event:any){
    this.bill_page = event;
    this.retrieveBills(this.currentVendor.vendor_id);
  }  

  payment_tabSize(event:any){
    this.payment_page = event;
    this.retrievePayments(this.currentVendor.vendor_id);
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.bill_page = 1;
    this.payment_page = 1;
    this.retrievePayments(this.currentVendor.vendor_id);
  } 


  

}
