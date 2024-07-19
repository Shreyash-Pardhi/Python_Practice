import { HttpClient } from '@angular/common/http';
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

  constructor(private http: HttpClient) {}

  registerUser(data: any) {
    return this.http.post<Response>(
      this.API_Endpoint + 'store/register/',
      data
    );
  }

  loginUser(data: any) {
    return this.http.post<Response>(this.API_Endpoint + 'store/login/', data);
  }

  logoutUser(): Observable<Response> {
    return this.http.post<Response>(this.API_Endpoint + 'store/logout/', {});
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
}
