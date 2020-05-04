import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class RoutineService {
  //for testing this will be on localport
  baseurl ="http://localhost:8000";
  //accept json
  httpHeaders = new HttpHeaders({'Content-type':'application/json'})
  constructor(private http: HttpClient) { }
  getAllRoutines(): Observable<any>{
    //get routines from rest api
    return this.http.get(this.baseurl + "/Routine/",
                          {headers: this.httpHeaders})
  }
  }
