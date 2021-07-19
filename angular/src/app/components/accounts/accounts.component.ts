import { Component, OnInit } from '@angular/core';
import { ClientService } from 'src/app/services/client.service';
import { Client } from 'src/app/models/client.model';
import { Client_Summary } from 'src/app/models/client.model';
import { ActivatedRoute} from '@angular/router';
import { VendorService } from 'src/app/services/vendor.service';


@Component({
  selector: 'app-accounts',
  templateUrl: './accounts.component.html',
  styleUrls: ['./accounts.component.css']
})

export class AccountsComponent implements OnInit {
  client_page = 1;
  vendor_page = 1;
  count = 0;
  client_tableSize = 10;
  vendor_tableSize = 10;
  tableSizesArr = [10];


  client_currentIndex = -1;
  vendor_currentIndex = -1;

  currentClient: Client = {
    client_id: '',
    client_name: '',}

  get_all_client_summary: any;
  get_all_vendor_summary:any;

  // Client_Summary ={
  //   client_name:'',
  //   get_one_month: 0,
  //   get_two_month: 0,
  //   get_three_month: 0,
  //   get_four_month: 0,
  //   get_total: 0,
  // }


  constructor(private clientService: ClientService,
    private vendorService: VendorService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {

    // this.retrieveReceivings(this.route.snapshot.params.id);
    this.get_all_client_summaries();
    this.get_all_vendor_summaries();
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

  get_all_client_summaries(): void {
    this.clientService.get_all_client_summaries()
      .subscribe(
        data => {
          this.get_all_client_summary = data;
          console.log(this.get_all_client_summary);
        },
        error => {
          console.log(error);
        });
  }

  get_all_vendor_summaries(): void {
    this.vendorService.get_all_vendor_summaries()
      .subscribe(
        data => {
          this.get_all_vendor_summary = data;
          console.log(this.get_all_vendor_summary);
        },
        error => {
          console.log(error);
        });
  }


  refreshList(): void {

    this.client_currentIndex = -1;
    this.vendor_currentIndex = -1;
  }

  
  tabSize_client(event:any){
    this.client_page = event;
  }  

  tabSize_vendor(event:any){
    this.vendor_page = event;
  }  

  tableData_client(event:any): void {
    this.client_tableSize = event.target.value;
    this.client_page = 1;
  } 

  tableData_vendor(event:any): void {
    this.vendor_tableSize = event.target.value;
    this.vendor_page = 1;
  } 


}
