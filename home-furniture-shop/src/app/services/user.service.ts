import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// Interface for login response
interface LoginResponse {
  message: string;
  role?: string;
  user?: any;
  token?: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private apiUrl = 'http://127.0.0.1:5000/api/users'; // Flask backend

  constructor(private http: HttpClient) {}

  // CUSTOMER LOGIN
  login(email: string, password: string): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.apiUrl}/login`, { email, password })
      .pipe(catchError(this.handleError));
  }

  // CUSTOMER SIGNUP
  signup(data: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/signup`, data)
      .pipe(catchError(this.handleError));
  }

  // ADMIN LOGIN
  adminLogin(email: string, password: string): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.apiUrl}/admin/login`, { email, password })
      .pipe(catchError(this.handleError));
  }


  // ERROR HANDLING
  private handleError(error: any) {
    let errorMsg = 'An unknown error occurred';

    if (error instanceof HttpErrorResponse) {
      if (error.error && error.error.error) {
        errorMsg = error.error.error;
      }
      else if (error.error && error.error.message) {
        errorMsg = error.error.message;
      }
      else {
        errorMsg = `Server returned code ${error.status}`;
      }
    }
    else if (error && error.message) {
      errorMsg = error.message;
    }

    return throwError(() => new Error(errorMsg));
  }
}
