import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-customer-header',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './customer-header.component.html',
  styleUrls: ['./customer-header.component.css']
})
export class CustomerHeaderComponent {

  menuActive: boolean = false;
  profileActive: boolean = false;

  user = {
    fullname: 'John Doe',
    address: '123 Main St, City'
  };

  constructor(private router: Router) {}

  toggleMenu() {
    this.menuActive = !this.menuActive;
  }

  toggleProfile() {
    this.profileActive = !this.profileActive;
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('role');
    this.router.navigate(['/login']);
  }
}
