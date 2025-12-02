import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// Interface for login response
interface LoginResponse {
  message: string;
  role?: string;  // your backend returns role
  user?: any;     // user object
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:5000/api/users'; // Flask backend URL

  constructor(private http: HttpClient) {}

  // Customer login
  login(email: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login`, { email, password })
      .pipe(catchError(this.handleError));
  }

  // Customer signup
  signup(data: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/signup`, data)
      .pipe(catchError(this.handleError));
  }

  // Optional: Admin login
  adminLogin(email: string, password: string): Observable<LoginResponse> {
    const payload = { email, password };
    return this.http.post<LoginResponse>(`${this.apiUrl}/admin/login`, payload)
      .pipe(catchError(this.handleError));
  }

  // Optional: Admin registration
  registerAdmin(data: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/admin/register`, data)
      .pipe(catchError(this.handleError));
  }

  // Error handler
  private handleError(error: any) {
    let errorMsg = 'An unknown error occurred';

    if (error instanceof HttpErrorResponse) {
      if (error.error && error.error.error) {
        // Backend sends { error: "message" }
        errorMsg = error.error.error;
      } else if (error.error && error.error.message) {
        errorMsg = error.error.message;
      } else {
        errorMsg = `Server returned code ${error.status}`;
      }
    } else if (error && error.message) {
      errorMsg = error.message;
    }

    return throwError(() => new Error(errorMsg));
  }
}
