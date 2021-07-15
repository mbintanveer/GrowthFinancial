import { Component, OnInit } from '@angular/core';
import { Vendor } from 'src/app/models/vendor.model';
import { VendorService } from 'src/app/services/vendor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-vendor',
  templateUrl: './add-vendors.component.html',
  styleUrls: ['./add-vendors.component.css']
})

export class AddVendorsComponent implements OnInit {
  vendor: Vendor = {
    vendor_id: '',
    vendor_name: '',

  };
  submitted = false;

  constructor (private vendorService: VendorService,
    private router: Router){ }

  ngOnInit(): void {
  }

  saveVendor(): void {
    const data = {
      vendor_id: this.vendor.vendor_id,
      vendor_name: this.vendor.vendor_name
    };
    

    this.vendorService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
          this.router.navigate(['/Vendors']);
        },
        error => {
          console.log(error);
        });
  }

  newVendor(): void {
    this.submitted = false;
    this.vendor = {
      vendor_name: '',
      
    };
     
  }
}