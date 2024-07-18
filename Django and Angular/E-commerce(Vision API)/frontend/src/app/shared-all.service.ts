import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

interface AuthResponse {
  success: boolean;
  message: string;
}

interface userHomeResponce {
  success: boolean;
  s_title: string;
  message: string;
  data: any;
}

@Injectable({
  providedIn: 'root',
})
export class SharedAllService {
  readonly API_Endpoint = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) {}

  registerUser(data: any) {
    return this.http.post<AuthResponse>(
      this.API_Endpoint + 'store/register/',
      data
    );
  }

  loginUser(data: any) {
    return this.http.post<AuthResponse>(
      this.API_Endpoint + 'store/login/',
      data
    );
  }

  logoutUser() {
    return this.http.get<AuthResponse>(this.API_Endpoint + 'store/logout/');
  }

  userHome(data?: any): Observable<userHomeResponce> {
    if (data && Object.keys(data).length > 0) {
      return this.http.post<userHomeResponce>(
        this.API_Endpoint + 'store/Home/',
        data
      );
    } else {
      return this.http.get<userHomeResponce>(this.API_Endpoint + 'store/Home/');
    }
  }
}
