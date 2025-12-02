import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UserService } from '../../services/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  // Customer login
  email = '';
  password = '';
  message = '';

  // Sign Up modal
  isSignUpOpen = false;
  signupName = '';
  signupEmail = '';
  signupPassword = '';
  signupContact = '';
  signupAddress = '';
  signUpMessage = '';

  // Admin login modal
  isAdminLoginOpen = false;
  adminEmail = '';
  adminPassword = '';
  adminMessage = '';

  constructor(private userService: UserService, private router: Router) {}

  // ================= CUSTOMER LOGIN =================
  onLogin() {
    if (!this.email || !this.password) {
      this.message = 'Please enter email and password';
      return;
    }

    this.userService.login(this.email, this.password).subscribe({
      next: (res: any) => {
        this.message = 'Login successful!';
        setTimeout(() => (this.message = ''), 5000);

        if (res.token) localStorage.setItem('token', res.token);

        // Redirect directly to customer dashboard
        this.router.navigate(['/customer/dashboard']);
      },
      error: (err: any) => {
        this.message = 'Login failed: ' + (err.error?.message || err.message);
        setTimeout(() => (this.message = ''), 5000);
      }
    });
  }


  // ================= SIGN UP =================
  openSignUpModal() {
    this.isSignUpOpen = true;
  }

  closeSignUpModal() {
    this.isSignUpOpen = false;
    this.signUpMessage = '';
  }

  onSignUp() {
    if (!this.signupName || !this.signupEmail || !this.signupPassword ||
        !this.signupContact || !this.signupAddress) {
      this.signUpMessage = 'Please fill all fields';
      return;
    }

    const signupData = {
      full_name: this.signupName,
      email: this.signupEmail,
      password: this.signupPassword,
      contact_number: this.signupContact,
      address: this.signupAddress
    };

    this.userService.signup(signupData).subscribe({
      next: (res: any) => {
        this.signUpMessage = 'Sign Up successful! You can now log in.';
        setTimeout(() => this.closeSignUpModal(), 2000);
      },
      error: (err: any) => {
        this.signUpMessage = 'Sign Up failed: ' + (err.error?.message || err.message);
      }
    });
  }

  // ================= FORGOT PASSWORD =================
  openForgotPassword() {
    this.router.navigate(['/forgot-password']);
  }

  // ================= ADMIN LOGIN =================
  openAdminLoginModal() {
    this.isAdminLoginOpen = true;
  }

  closeAdminLoginModal() {
    this.isAdminLoginOpen = false;
    this.adminMessage = '';
  }

  onAdminLogin() {
    if (!this.adminEmail || !this.adminPassword) {
      this.adminMessage = 'Please enter admin email and password';
      return;
    }

    this.userService.adminLogin(this.adminEmail, this.adminPassword).subscribe({
      next: (res: any) => {
        this.adminMessage = 'Admin login successful!';
        setTimeout(() => {
          this.adminMessage = '';
          this.closeAdminLoginModal();
        }, 1500);

        if (res.token) localStorage.setItem('admin_token', res.token);

        this.router.navigate(['/admin/dashboard']);
      },
      error: (err: any) => {
        this.adminMessage = 'Admin login failed: ' + (err.error?.message || err.message);
        setTimeout(() => (this.adminMessage = ''), 5000);
      }
    });
  }
}
