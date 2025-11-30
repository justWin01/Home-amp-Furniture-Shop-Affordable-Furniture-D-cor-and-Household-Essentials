import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

interface LoginResponse {
  message: string;
  token?: string; // optional, if your backend returns JWT
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:5000/api/users'; // your Flask backend URL

  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<LoginResponse> {
    const payload = { email, password };
    return this.http.post<LoginResponse>(`${this.apiUrl}/login`, payload)
      .pipe(
        catchError(this.handleError)
      );
  }

  register(data: any) {
    return this.http.post(`${this.apiUrl}/register`, data)
      .pipe(catchError(this.handleError));
  }



  // Add more user functions if needed
  // e.g., register(), getProfile(), etc.

  private handleError(error: any) {
    let errorMsg = 'An unknown error occurred';

    if (error instanceof HttpErrorResponse) {
      // Backend returned an unsuccessful response code
      if (error.error && error.error.message) {
        errorMsg = error.error.message;
      } else {
        errorMsg = `Server returned code ${error.status}`;
      }
    } else if (error && error.message) {
      // Other kind of error
      errorMsg = error.message;
    }

    return throwError(() => new Error(errorMsg));
  }

}
