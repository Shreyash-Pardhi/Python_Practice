import { Routes } from '@angular/router';
import { HomeComponent } from './Pages/home/home.component';
import { PipesComponent } from './Pages/pipes/pipes.component';
import { SignalsComponent } from './Pages/signals/signals.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'pipes', component: PipesComponent },
  { path: 'signals', component: SignalsComponent },
];
