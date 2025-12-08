import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';   // ✅ Required for *ngIf, *ngFor etc.

@Component({
  selector: 'app-customer-header',
  standalone: true,
  imports: [CommonModule],    // ⬅️ MUST ADD THIS
  templateUrl: './customer-header.component.html',
  styleUrls: ['./customer-header.component.css']
})
export class CustomerHeaderComponent {

  constructor(private router: Router) {}

  logout() {
    // remove token
    localStorage.removeItem('token');
    localStorage.removeItem('role');   // Optional but recommended

    // redirect to login page
    this.router.navigate(['/login']);
  }
}
