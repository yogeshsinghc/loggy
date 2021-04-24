import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable()
export class BackendService {
  // http = HttpClient
  constructor(private httpClient:HttpClient) {
    // this.http = http
  }

  getApps(){
    let returnTHis = this.httpClient.get("http://127.0.0.1:5000/getApps")
    console.log(returnTHis)
    return returnTHis
  }

  getLogs(appName){
    let returnTHis = this.httpClient.get("http://127.0.0.1:5000/getLogs/"+appName)
    console.log(returnTHis)
    return returnTHis
  }

  getMemory(){
    let returnTHis = this.httpClient.get("http://127.0.0.1:5000/getMemory")
    console.log(returnTHis)
    return returnTHis
  }

  postFilters(data){
    let returnTHis = this.httpClient.post("http://127.0.0.1:5000/filters",data)
    console.log(returnTHis)
    return returnTHis
  }
}
