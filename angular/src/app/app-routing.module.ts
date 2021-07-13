import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SummaryComponent } from './components/summary/summary.component';

import { ClientsListComponent } from './components/client-list/client-list.component';
import { ClientDetailsComponent } from './components/client-details/client-details.component';
import { AddClientComponent } from './components/add-client/add-client.component';

import { ServicesListComponent } from './components/services-list/services-list.component';

import { ExpensesListComponent } from './components/expenses-list/expenses-list.component';
import { ExpensesDetailsComponent } from './components/expenses-details/expenses-details.component';
import { AddExpensesComponent } from './components/add-expenses/add-expenses.component';

import { ReceivingsListComponent } from './components/receivings-list/receivings-list.component';
import { ReceivingsDetailsComponent } from './components/receivings-details/receivings-details.component';
import { AddReceivingsComponent } from './components/add-receivings/add-receivings.component';

import { VendorsListComponent } from './components/vendors-list/vendors-list.component';
import { VendorsDetailsComponent } from './components/vendors-details/vendors-details.component';
import { AddVendorsComponent } from './components/add-vendors/add-vendors.component';

const routes: Routes = [
  { path: '', redirectTo: 'Summary', pathMatch: 'full' },
  { path: 'Clients', component: ClientsListComponent },
  { path: 'Clients/:id', component: ClientDetailsComponent },
  { path: 'add', component: AddClientComponent },

  { path: 'Services', component: ServicesListComponent },

  { path: 'Expenses', component: ExpensesListComponent },
  { path: 'Expenses/:id', component: ExpensesDetailsComponent },
  { path: 'add', component: AddExpensesComponent }

  { path: 'Receivings', component: ReceivingsListComponent },
  { path: 'Receivings/:id', component: ReceivingsDetailsComponent },
  { path: 'add', component: AddReceivingsComponent },

  { path: 'Vendors', component: VendorsListComponent },
  { path: 'Vendors/:id', component: VendorsDetailsComponent },
  { path: 'add', component: AddVendorsComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
