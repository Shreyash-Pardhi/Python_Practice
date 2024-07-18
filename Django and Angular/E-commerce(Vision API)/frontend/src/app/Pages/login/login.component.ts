import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { SharedAllService } from '../../shared-all.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [SharedAllService, Router]
})
export class LoginComponent {
  constructor(private service: SharedAllService, private router:Router) { }

  title: string = "Login";
  data: any = {
    username: '',
    password: ''
  };

  UserLogin(): any {
    console.log(this.data);
    this.service.loginUser(this.data).subscribe((res) => {
      if (res.success) {
        this.router.navigateByUrl('/userHome');
        alert(res.message);
      } else {
        alert(res.message);
      }
    });
  }
}
