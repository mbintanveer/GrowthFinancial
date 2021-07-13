import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddClientComponent } from './components/add-client/add-client.component';
import { ClientDetailsComponent } from './components/client-details/client-details.component';
import { ClientsListComponent } from './components/client-list/client-list.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AddReceivingsComponent } from './components/add-receivings/add-receivings.component';
import { ReceivingsDetailsComponent } from './components/receivings-details/receivings-details.component';
import { ReceivingsListComponent } from './components/receivings-list/receivings-list.component';
import { ServicesListComponent } from './services-list/services-list.component';
import { ExpensesListComponent } from './expenses-list/expenses-list.component';
import { AddExpensesComponent } from './components/add-expenses/add-expenses.component';
import { ExpensesDetailsComponent } from './components/expenses-details/expenses-details.component';
import { VendorsDetailsComponent } from './components/vendors-details/vendors-details.component';
import { VendorsListComponent } from './components/vendors-list/vendors-list.component';
import { AddVendorsComponent } from './components/add-vendors/add-vendors.component';
import { SummaryComponent } from './components/summary/summary.component';

@NgModule({
  declarations: [
    AppComponent,
    AddClientComponent,
    ClientDetailsComponent,
    ClientsListComponent,
    NavbarComponent,
    AddReceivingsComponent,
    ReceivingsDetailsComponent,
    ReceivingsListComponent,
    ServicesListComponent,
    ExpensesListComponent,
    AddExpensesComponent,
    ExpensesDetailsComponent,
    VendorsDetailsComponent,
    VendorsListComponent,
    AddVendorsComponent,
    SummaryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
