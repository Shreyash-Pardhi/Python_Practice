import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SharedAllService } from '../../shared-all.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
  providers: [SharedAllService],
})
export class RegisterComponent {
  constructor(private service: SharedAllService) {}

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
    });
  }
}
