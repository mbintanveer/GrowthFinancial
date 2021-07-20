import { Component, OnInit } from '@angular/core';
import { ReceivingService } from 'src/app/services/receiving.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Receiving } from 'src/app/models/receiving.model';

@Component({
  selector: 'app-receiving-details',
  templateUrl: './receivings-details.component.html',
  styleUrls: ['./receivings-details.component.css']
})

export class ReceivingsDetailsComponent implements OnInit {
  currentReceiving: Receiving = {
    receiving_id: '',
    receiving_description: '',
    receiving_amount: 0,
    receiving_client:'',
    date_created:''
    ,
    
  };
  message = '';

  constructor(
    private receivingService: ReceivingService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.getReceiving(this.route.snapshot.params.id);
      console.log('hi')
    }
  
    getReceiving(id: string): void {
      this.receivingService.get(id)
        .subscribe(
          data => {
            this.currentReceiving = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        receiving_id: this.currentReceiving.receiving_id,
        receiving_description: this.currentReceiving.receiving_description,
        receiving_amount: 0,
        date_created:'',
        receiving_client:'',
      };
  
      this.message = '';
  
      this.receivingService.update(this.currentReceiving.receiving_id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateReceiving(): void {
  
      this.receivingService.update(this.currentReceiving.receiving_id, this.currentReceiving)
        .subscribe(
            
          error => {
            console.log(error);
          });
          this.router.navigate(['/View-Clients/'+this.currentReceiving.receiving_client]);
          
    }
  
    deleteReceiving(): void {
      this.receivingService.delete(this.currentReceiving.receiving_id)
        .subscribe(
          response => {
            this.message = response.message ? response.message : 'This receiving was deleted successfully!';
            this.router.navigate(['/View-Clients/'+this.currentReceiving.receiving_client]);
          },
          
          error => {
            console.log(error);
          });
    }
  }

