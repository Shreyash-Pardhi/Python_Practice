import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { SharedAllService } from '../../shared-all.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [SharedAllService]
})
export class LoginComponent {
  constructor(private service: SharedAllService) { }

  title: string = "Login";
  data: any = {
    username: '',
    password: ''
  };

  UserLogin(): any {
    console.log(this.data);
    this.service.loginUser(this.data).subscribe((res) => {
      if (res.success) {
        alert(res.message);
      } else {
        alert(res.message);
      }
    });
  }
}
