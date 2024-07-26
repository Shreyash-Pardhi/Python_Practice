import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable, tap } from 'rxjs';
import { loginSuccess, logout } from './Storage/userInfo.action';

interface Response {
  success: boolean;
  u_status?: boolean;
  message: string;
  userData?: any;
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

  constructor(private http: HttpClient, private store: Store) {}

  registerUser(data: any) {
    return this.http.post<Response>(
      this.API_Endpoint + 'store/register/',
      data
    );
  }

  loginUser(data: any) {
    return this.http
      .post<Response>(this.API_Endpoint + 'store/login/', data, {
        withCredentials: true,
      })
      .pipe(
        tap((res: any) => {
          if (res.success) {
            localStorage.setItem('token', res.userInfo['token']);
            this.store.dispatch(
              loginSuccess({
                username: res.userInfo.user['username'],
                isAdmin: res.userInfo.user['is_admin'],
              })
            );
          }
        })
      );
  }

  logoutUser(): Observable<Response> {
    const headers = this.getAuthHeaders();
    return this.http
      .get<Response>(this.API_Endpoint + 'store/logout/', {
        headers: headers,
        withCredentials: true,
      })
      .pipe(
        tap(() => {
          localStorage.removeItem('token');
          this.store.dispatch(logout());
        })
      );
  }

  userHome(data?: any): Observable<userHomeResponce> {
    const headers = this.getAuthHeaders();
    if (data && Object.keys(data).length > 0) {
      return this.http.post<userHomeResponce>(
        this.API_Endpoint + 'store/Home/',
        data,
        {
          headers: headers,
          withCredentials: true,
        }
      );
    } else {
      return this.http.get<userHomeResponce>(this.API_Endpoint + 'store/Home/');
    }
  }

  addSinglePROD(data: any) {
    const headers = this.getAuthHeaders();
    return this.http.post<Response>(
      this.API_Endpoint + 'store/addProduct/',
      data,
      {
        headers: headers,
        withCredentials: true,
      }
    );
  }

  addCsvFile(file: File) {
    const headers = this.getAuthHeaders();
    const formdata = new FormData();
    formdata.append('file', file);

    return this.http.post<Response>(
      this.API_Endpoint + 'store/addProductFile/',
      formdata,
      {
        headers: headers,
        withCredentials: true,
      }
    );
  }

  currentUser() {
    const headers = this.getAuthHeaders();
    return this.http.get<Response>(this.API_Endpoint + 'store/currentUser/', {
      headers: headers,
    });
  }

  getAuthHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');
    let headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return headers;
  }
}
