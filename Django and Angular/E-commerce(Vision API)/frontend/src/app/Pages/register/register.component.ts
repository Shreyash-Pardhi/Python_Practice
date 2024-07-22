import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SharedAllService } from '../../shared-all.service';
import { Router, RouterLink } from '@angular/router';
import { LoaderService } from '../../loader.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, RouterLink],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
  providers: [SharedAllService, Router],
})
export class RegisterComponent {
  constructor(
    private service: SharedAllService,
    private router: Router,
    private loaderService: LoaderService
  ) {}

  title: string = 'Register';
  is_ad: boolean = false;
  data: any = {
    username: '',
    email: '',
    password1: '',
    password2: '',
    is_admin: this.is_ad,
  };
  UserRegister() {
    this.loaderService.showLoader();
    this.service.registerUser(this.data).subscribe(
      (res) => {
        if (res.success) {
          this.loaderService.hideLoader();
          alert(res.message);
          this.router.navigateByUrl('/login');
        } else {
          this.loaderService.hideLoader();
          alert(res.message);
        }
      }
      // (error) => {
      //   console.error('Registration error:', error);
      // }
    );
  }
}
