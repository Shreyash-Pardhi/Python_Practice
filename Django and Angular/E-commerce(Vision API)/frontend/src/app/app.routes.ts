import { Routes } from '@angular/router';
import { LoginComponent } from './Pages/login/login.component';
import { RegisterComponent } from './Pages/register/register.component';
import { UserHomeComponent } from './Pages/user-home/user-home.component';
import { AdminHomeComponent } from './Pages/admin-home/admin-home.component';
import { PageNotFoundComponent } from './Pages/page-not-found/page-not-found.component';

export const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'userHome', component: UserHomeComponent },
  { path: 'adminHome', component: AdminHomeComponent },
  { path: 'page-not-found', component: PageNotFoundComponent },
];
