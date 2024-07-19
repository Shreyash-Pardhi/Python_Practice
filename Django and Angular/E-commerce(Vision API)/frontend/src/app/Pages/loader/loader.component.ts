import { Component } from '@angular/core';
import { LoaderService } from '../../loader.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-loader',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './loader.component.html',
  styleUrl: './loader.component.css'
})
export class LoaderComponent {
  isLoading: boolean = false;

  constructor(private loaderService: LoaderService) {}

  ngOnInit() {
    this.loaderService.loaderState.subscribe((state: boolean) => {
      this.isLoading = state;
    });
  }
}
