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
  tableSize = 10;
  tableSizesArr = [10];

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

  searchVendors(): void {
    this.currentVendor = {};
    this.currentIndex = -1;

    this.vendorService.findByVendorName(this.vendor_name)
      .subscribe(
        data => {
          this.vendors = data;
          this.page=1
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

}


