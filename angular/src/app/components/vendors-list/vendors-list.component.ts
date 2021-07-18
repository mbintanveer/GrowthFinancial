import { Component, OnInit } from '@angular/core';
import { Vendor } from 'src/app/models/vendor.model';
import { VendorService } from 'src/app/services/vendor.service';

@Component({
  selector: 'app-vendor-list',
  templateUrl: './vendors-list.component.html',
  styleUrls: ['./vendors-list.component.css']
})

export class VendorsListComponent implements OnInit {


  currentVendor: Vendor = {};
  currentIndex = -1;
  vendor_name = '';

  vendors?: any;
  page = 1;
  count = 0;
  tableSize = 5;
  tableSizesArr = [5];

  constructor(private vendorService: VendorService) { }

  ngOnInit(): void {
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
  
  refreshList(): void {
    this.retrieveVendors();
    this.currentVendor = {};
    this.currentIndex = -1;
  }

  setActiveVendor(vendor: Vendor, index: number): void {
    this.currentVendor = vendor;
    this.currentIndex = index;
  }

  
  tabSize(event:any){
    this.page = event;
    this.retrieveVendors();
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrieveVendors();
  } 
  // searchTitle(): void {
  //   this.currentClient = {};
  //   this.currentIndex = -1;

  //   this.clientService.findByTitle(this.title)
  //     .subscribe(
  //       data => {
  //         this.clients = data;
  //         console.log(data);
  //       },
  //       error => {
  //         console.log(error);
  //       });
  // }
}


