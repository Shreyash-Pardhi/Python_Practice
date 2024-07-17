import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedAllService {
  readonly API_Endpoint = 'http://127.0.0.1:8000/'

  constructor(private http:HttpClient) {}

  registerUser(data: any){
      return this.http.post(this.API_Endpoint + 'store/register/',data);
  }
}
