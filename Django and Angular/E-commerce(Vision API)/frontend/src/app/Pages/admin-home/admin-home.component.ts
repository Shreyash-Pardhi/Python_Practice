import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { SharedAllService } from '../../shared-all.service';
import { FormsModule } from '@angular/forms';
import { LoaderService } from '../../loader.service';
import { CommonModule } from '@angular/common';
import { PageNotFoundComponent } from '../page-not-found/page-not-found.component';

@Component({
  selector: 'app-admin-home',
  standalone: true,
  imports: [RouterLink, FormsModule, CommonModule, PageNotFoundComponent],
  templateUrl: './admin-home.component.html',
  styleUrl: './admin-home.component.css',
  providers: [SharedAllService, Router],
})
export class AdminHomeComponent {
  selectedFile: File | null = null;

  USERNM?: any;
  isAdmin: Boolean = false;

  inp_data: any = {
    prodName: '',
    prodLink: '',
  };
  hidden: any;

  constructor(
    private service: SharedAllService,
    private router: Router,
    private loaderService: LoaderService
  ) {}

  ngOnInit(): void {
    this.service.currentUser().subscribe((res) => {
      this.isAdmin = res.userData['is_admin'];
      this.USERNM = res.userData['username'];
    });
  }
  addSingleProduct() {
    if (this.inp_data['prodName'] == '' || this.inp_data['prodLink'] == '') {
      alert('Please Enter both the fields to add product...');
    } else {
      this.loaderService.showLoader();
      this.service.addSinglePROD(this.inp_data).subscribe((res) => {
        if (res.success) {
          this.loaderService.hideLoader();
          alert(res.message);
        } else {
          this.loaderService.hideLoader();
          alert(res.message);
        }
      });
    }
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  addCSVfile(event: Event): void {
    event.preventDefault();
    if (this.selectedFile) {
      this.loaderService.showLoader();
      this.service.addCsvFile(this.selectedFile).subscribe((res) => {
        if (res.success) {
          this.loaderService.hideLoader();
          alert(res.message);
        } else {
          this.loaderService.hideLoader();
          alert(res.message);
        }
      });
    } else {
      alert('Please choose a csv file first!!!');
    }
  }

  userLogout() {
    this.loaderService.showLoader();
    this.service.logoutUser().subscribe((res) => {
      this.loaderService.hideLoader();
      this.router.navigateByUrl('/login');
    });
  }
}
