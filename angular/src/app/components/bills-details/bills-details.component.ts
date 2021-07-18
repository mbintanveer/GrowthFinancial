import { Component, OnInit } from '@angular/core';
import { BillService } from 'src/app/services/bill.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Bill } from 'src/app/models/bill.model';

@Component({
  selector: 'app-bill-details',
  templateUrl: './bills-details.component.html',
  styleUrls: ['./bills-details.component.css']
})

export class BillsDetailsComponent implements OnInit {
  currentBill: Bill = {
    bill_id: '',
    bill_description: '',
    bill_amount: 0,
    bill_vendor:'',
    date_created:''
    ,
    
  };
  message = '';

  constructor(
    private billService: BillService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getBill(this.route.snapshot.params.id);
      console.log('hi')
    }
  
    getBill(id: string): void {
      this.billService.get(id)
        .subscribe(
          data => {
            this.currentBill = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        bill_id: this.currentBill.bill_id,
        bill_description: this.currentBill.bill_description,
        bill_amount: 0,
        date_created:'',
        bill_vendor:'',
      };
  
      this.message = '';
  
      this.billService.update(this.currentBill.bill_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateBill(): void {
  
      this.billService.update(this.currentBill.bill_id, this.currentBill)
        .subscribe(
            
          error => {
            console.log(error);
          });
        this.router.navigate(['/Bills']);
          
    }
  
    deleteBill(): void {
      this.billService.delete(this.currentBill.bill_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This bill was deleted successfully!';
            this.router.navigate(['/Bills']);
          },
          error => {
            console.log(error);
          });
    }
  }

