import { Component } from '@angular/core';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { SharedAllService } from '../../shared-all.service';
import { Router, RouterLink } from '@angular/router';
import { LoaderService } from '../../loader.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, RouterLink, ReactiveFormsModule],
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

  pas = /^(?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])(?=\D*\d).{6,}$/;
  Registration_data: FormGroup = new FormGroup({
    username: new FormControl('', [Validators.required]),
    email: new FormControl('', [
      Validators.required,
      Validators.pattern('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'),
    ]),
    password1: new FormControl('', [
      Validators.required,
      Validators.pattern(this.pas),
    ]),
    password2: new FormControl('', [
      Validators.required,
      Validators.minLength(5),
    ]),
    is_admin: new FormControl(false),
  });

  // data: any = {
  //   username: '',
  //   email: '',
  //   password1: '',
  //   password2: '',
  //   is_admin: false,
  // };
  UserRegister() {
    // this.loaderService.showLoader();
    // this.service.registerUser(this.data).subscribe((res) => {
    //   if (res.success) {
    //     this.loaderService.hideLoader();
    //     alert(res.message);
    //     this.router.navigateByUrl('/login');
    //   } else {
    //     this.loaderService.hideLoader();
    //     alert(res.message);
    //   }
    // });
    console.log(this.Registration_data.value);
  }
}
