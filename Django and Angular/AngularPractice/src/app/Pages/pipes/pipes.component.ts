import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {
  DatePipe,
  JsonPipe,
  LowerCasePipe,
  TitleCasePipe,
  UpperCasePipe,
} from '@angular/common';
@Component({
  selector: 'app-pipes',
  standalone: true,
  imports: [
    RouterLink,
    DatePipe,
    UpperCasePipe,
    LowerCasePipe,
    TitleCasePipe,
    JsonPipe,
  ],
  templateUrl: './pipes.component.html',
  styleUrl: './pipes.component.css',
})
export class PipesComponent {
  date: number = Date.now();
  someString: string = 'Shreyash';
  jsonOBJ = {
    name: 'Angular',
    version: '18.1',
    previous: [17, 16, 15, 14],
    example: 'JsonPipe',
  };
}
