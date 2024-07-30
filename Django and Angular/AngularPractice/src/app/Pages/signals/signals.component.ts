import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-signals',
  standalone: true,
  imports: [],
  templateUrl: './signals.component.html',
  styleUrl: './signals.component.css',
})
export class SignalsComponent {
  name = signal<string>('Shreyash');
  num1 = signal<number>(20);
  num2 = signal<number>(50);

  changeName() {
    this.name.set('Ketan');
  }

  swap() {
    const tmp = this.num1;
    this.num1 = this.num2;
    this.num2 = tmp;
  }
}
