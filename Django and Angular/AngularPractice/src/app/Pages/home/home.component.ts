import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  template: ` <h1 class="text-8xl text-center mt-10">Angular-18 Practice</h1> `,
})
export class HomeComponent {}
