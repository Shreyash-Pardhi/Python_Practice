import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { SharedAllService } from '../../shared-all.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [SharedAllService, Router],
})
export class LoginComponent {
  constructor(private service: SharedAllService, private router: Router) {}

  user?:String;
  title: String = 'Login';

  data: any = {
    username: '',
    password: '',
  };

  UserLogin(): any {
    this.service.loginUser(this.data).subscribe((res) => {
      if (res.success) {
        if (res.u_status) {
          this.router.navigateByUrl('/adminHome');
        } else {
          this.router.navigateByUrl('/userHome');
        }
      } else {
        alert(res.message);
      }
    });
  }
}
