import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { SharedAllService } from '../../shared-all.service';
import { CommonModule } from '@angular/common';
import { LoaderService } from '../../loader.service';

@Component({
  selector: 'app-user-home',
  standalone: true,
  imports: [FormsModule, RouterLink, CommonModule],
  templateUrl: './user-home.component.html',
  styleUrl: './user-home.component.css',
  providers: [SharedAllService, Router],
})
export class UserHomeComponent {
  constructor(private service: SharedAllService, private router: Router, private loaderService: LoaderService,) { }

  data: any;
  ti: any;
  search_query: any = {
    search_txt: '',
  };

  ngOnInit(): void {
    this.getAllData();
  }

  getAllData() {
    this.loaderService.showLoader();
    this.service.userHome(this.search_query).subscribe((res) => {
      if (res.success) {
        this.data = res.data;
        this.ti = res.s_title;
        this.loaderService.hideLoader();
      } else {
        this.loaderService.hideLoader();
        alert(res.message);
      }
    });
  }
  userLogout() {
    this.service.logoutUser().subscribe(
      (res) => {
        // if (res.success) {
        //   alert(res.message);
        this.router.navigateByUrl('/login');
        // } else {
        //   alert(res.message);
        // }
      }
      // (error) => {
      //   console.error('Registration error:', error);
      // }
    );
  }
}
