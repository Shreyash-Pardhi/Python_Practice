import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SharedAllService } from '../../shared-all.service';
import { Router, RouterLink } from '@angular/router';


@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, RouterLink],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
  providers: [SharedAllService, Router],
})
export class RegisterComponent {
  constructor(private service: SharedAllService, private router:Router) { }

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
    this.service.registerUser(this.data).subscribe((res) => {
      alert(res.toString());
      // this.router.navigate(['/login']);
    }
      // (error) => {
      //   console.error('Registration error:', error);
      // }
    );
  }
}
