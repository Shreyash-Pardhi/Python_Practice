import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

interface Response {
  success: boolean;
  u_status?: boolean;
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

  constructor(private http: HttpClient) { }

  registerUser(data: any) {
    return this.http.post<Response>(
      this.API_Endpoint + 'store/register/',
      data
    );
  }

  loginUser(data: any) {
    // const headers = new HttpHeaders({ 'X-CSRFToken': this.getCsrfToken() });
    return this.http.post<Response>(this.API_Endpoint + 'store/login/', data, { withCredentials: true });
  }

  logoutUser(): Observable<Response> {
    // const headers = new HttpHeaders({ 'X-CSRFToken': this.getCsrfToken() });
    return this.http.post<Response>(this.API_Endpoint + 'store/logout/', {}, { withCredentials: true });
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


  // private getCsrfToken(): any {
  //   const token = this.getCookie('csrftoken') || this.getMetaContent('csrf-token');
  //   return token;
  // }

  // private getCookie(name: string): string | null {
  //   const nameEQ = name + "=";
  //   const ca = document.cookie.split(';');
  //   for(let i=0;i < ca.length;i++) {
  //       let c = ca[i];
  //       while (c.charAt(0) == ' ') c = c.substring(1,c.length);
  //       if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  //   }
  //   return null;
  // }

  // private getMetaContent(name: string): string | null {
  //   const element: HTMLMetaElement | null = document.querySelector(`meta[name="${name}"]`);
  //   return element ? element.content : null;
  // }
}
