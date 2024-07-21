import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';

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
  private tokenKey = '';
  private csrfToken?: any;

  constructor(private http: HttpClient) {  }

  // getCsrfToken(): string {
  //   const name = 'csrftoken';
  //   const value = `; ${document.cookie}`;
  //   const parts = value.split(`; ${name}=`);
  //   if (parts.length === 2) {
  //     return parts.pop().split(';').shift();
  //   }
  //   return '';
  // }


  registerUser(data: any) {
    return this.http.post<Response>(
      this.API_Endpoint + 'store/register/',
      data
    );
  }

  loginUser(data: any) {
    return this.http.post<Response>(this.API_Endpoint + 'store/login/', data, { withCredentials: true }).pipe(
      tap((res: any) => {
        if (res.success) {
          localStorage.setItem('token', res.res['token']);
        }
      })
    );
  }

  logoutUser(): Observable<Response> {
    const headers = this.getAuthHeaders();
    return this.http.post<Response>(this.API_Endpoint + 'store/logout/', {}, { headers: headers, withCredentials: true }).pipe(
      tap(() => {
        localStorage.removeItem('token');
      })
    );
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

  addSinglePROD(data: any) {
    return this.http.post<Response>(
      this.API_Endpoint + 'store/addProduct/',
      data
    );
  }

  addCsvFile(file: File) {
    const formdata = new FormData();
    formdata.append('file', file);

    return this.http.post<Response>(
      this.API_Endpoint + 'store/addProductFile/',
      formdata
    );
  }

  currentUser() {
    const headers = this.getAuthHeaders();
    return this.http.get<Response>(this.API_Endpoint + 'store/currentUser/', { headers: headers });
  }

  getAuthHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');
    let headers = new HttpHeaders()
      .set('Authorization', `Token ${token}`);
    // .set('X-CSRFToken', this.csrfToken);
    console.log(headers)
    return headers;
  }
}
