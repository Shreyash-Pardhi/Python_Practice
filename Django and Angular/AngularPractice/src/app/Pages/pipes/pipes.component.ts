import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {
  AsyncPipe,
  DatePipe,
  JsonPipe,
  LowerCasePipe,
  TitleCasePipe,
  UpperCasePipe,
} from '@angular/common';
import { interval, map, Observable } from 'rxjs';
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
    AsyncPipe,
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

  currTime: Observable<Date> = new Observable<Date>();

  constructor() {
    this.currTime = interval(1000).pipe(map(() => new Date()));
  }
}
