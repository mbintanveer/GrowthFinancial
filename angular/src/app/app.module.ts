import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { NgxPaginationModule } from 'ngx-pagination';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddClientComponent } from './components/add-client/add-client.component';
import { ClientDetailsComponent } from './components/client-details/client-details.component';
import { ClientsListComponent } from './components/client-list/client-list.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ExpensesListComponent } from './components/expenses-list/expenses-list.component';
import { AddExpensesComponent } from './components/add-expenses/add-expenses.component';
import { ExpensesDetailsComponent } from './components/expenses-details/expenses-details.component';
import { VendorsDetailsComponent } from './components/vendors-details/vendors-details.component';
import { VendorsListComponent } from './components/vendors-list/vendors-list.component';
import { AddVendorsComponent } from './components/add-vendors/add-vendors.component';
import { SummaryComponent } from './components/summary/summary.component';
import { CashflowsComponent } from './components/cashflows/cashflows.component';
import { AccountsComponent } from './components/accounts/accounts.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { ViewClientComponent } from './components/view-client/view-client.component';
import { ViewVendorComponent } from './components/view-vendors/view-vendors.component';
import { AddReceivingsComponent } from './components/add-receivings/add-receivings.component';
import { ReceivingsListComponent } from './components/receivings-list/receivings-list.component';
import { ReceivingsDetailsComponent } from './components/receivings-details/receivings-details.component';
import { ViewInvoicesComponent } from './components/view-invoices/view-invoices.component';
import { AddInvoicesComponent } from './components/add-invoices/add-invoices.component';
import { InvoicesDetailsComponent } from './components/invoices-details/invoices-details.component';
import { InvoicesListComponent } from './components/invoices-list/invoices-list.component';

import { AddBillsComponent } from './components/add-bills/add-bills.component';
import { AddPaymentsComponent } from './components/add-payments/add-payments.component';
import { BillsDetailsComponent } from './components/bills-details/bills-details.component';
import { PaymentsDetailsComponent } from './components/payments-details/payments-details.component';
 
@NgModule({
  declarations: [
    AppComponent,
    AddClientComponent,
    ClientDetailsComponent,
    ClientsListComponent,
    NavbarComponent,
    // AddReceivingsComponent,
    // ReceivingsDetailsComponent,
    // ReceivingsListComponent,
    ExpensesListComponent,
    AddExpensesComponent,
    ExpensesDetailsComponent,
    VendorsDetailsComponent,
    VendorsListComponent,
    AddVendorsComponent,
    SummaryComponent,
    CashflowsComponent,
    AccountsComponent,
    SidebarComponent,
    ViewClientComponent,
    ViewVendorComponent,
    AddReceivingsComponent,
    ReceivingsListComponent,
    ReceivingsDetailsComponent,
    ViewInvoicesComponent,
    AddInvoicesComponent,
    InvoicesDetailsComponent,
    InvoicesListComponent,
    AddBillsComponent,
    AddPaymentsComponent,
    BillsDetailsComponent,
    PaymentsDetailsComponent,
  ],

  imports: [
    AppRoutingModule,
    RouterModule,
    NgxPaginationModule,
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
