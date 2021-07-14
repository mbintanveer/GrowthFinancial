import { Component, OnInit } from '@angular/core';
import { VendorService } from 'src/app/services/vendor.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Vendor } from 'src/app/models/vendor.model';

@Component({
  selector: 'app-vendor-details',
  templateUrl: './vendors-details.component.html',
  styleUrls: ['./vendors-details.component.css']
})

export class VendorsDetailsComponent implements OnInit {
  currentVendor: Vendor = {
    vendor_id: '',
    vendor_name: '',
  };
  message = '';

  constructor(
    private vendorService: VendorService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getVendor(this.route.snapshot.params.id);
      console.log('hi')
    }
  
    getVendor(id: string): void {
      this.vendorService.get(id)
        .subscribe(
          data => {
            this.currentVendor = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        vendor_id: this.currentVendor.vendor_id,
        vendor_name: this.currentVendor.vendor_name
      };
  
      this.message = '';
  
      this.vendorService.update(this.currentVendor.vendor_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateVendor(): void {
  
      this.vendorService.update(this.currentVendor.vendor_id, this.currentVendor)
        .subscribe(
            
          error => {
            console.log(error);
          });
        this.router.navigate(['/Vendors']);
          
    }
  
    deleteVendor(): void {
      this.vendorService.delete(this.currentVendor.vendor_id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This vendor was deleted successfully!';
            this.router.navigate(['/Vendors']);
          },
          error => {
            console.log(error);
          });
    }
  }

