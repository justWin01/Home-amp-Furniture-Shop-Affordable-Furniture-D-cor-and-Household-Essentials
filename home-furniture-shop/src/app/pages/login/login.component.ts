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

  // ================= CUSTOMER LOGIN =================
  email = '';
  password = '';
  message = '';

  // ================= SIGN UP MODAL =================
  isSignUpOpen = false;
  signupName = '';
  signupEmail = '';
  signupPassword = '';
  signupContact = '';
  signupAddress = '';
  signUpMessage = '';

  // ================= ADMIN MODAL =================
  isAdminModalOpen = false;
  adminMode: 'login' | 'register' = 'login';

  // Admin Login fields
  adminEmail = '';
  adminPassword = '';
  adminMessage = '';

  // Admin Register fields
  adminRegisterName = '';
  adminRegisterEmail = '';
  adminRegisterPassword = '';
  adminRegisterMessage = '';

  constructor(private userService: UserService, private router: Router) {}

  // ================= HELPER =================
  private showMessage(
    field: 'message' | 'signUpMessage' | 'adminMessage' | 'adminRegisterMessage',
    text: string,
    timeout: number = 5000
  ) {
    (this as any)[field] = text;
    setTimeout(() => (this as any)[field] = '', timeout);
  }

  private resetAdminFields() {
    this.adminEmail = '';
    this.adminPassword = '';
    this.adminMessage = '';
    this.adminRegisterName = '';
    this.adminRegisterEmail = '';
    this.adminRegisterPassword = '';
    this.adminRegisterMessage = '';
  }

  // ================= CUSTOMER LOGIN =================
  onLogin() {
    if (!this.email || !this.password) {
      this.showMessage('message', 'Please enter email and password');
      return;
    }

    this.userService.login(this.email, this.password).subscribe({
      next: (res: any) => {
        this.showMessage('message', 'Login successful!');
        if (res.token) localStorage.setItem('token', res.token);
        this.router.navigate(['/customer/dashboard']);
      },
      error: (err: any) => this.showMessage('message', 'Login failed: ' + (err.error?.message || err.message))
    });
  }

  // ================= SIGN UP CUSTOMER =================
  openSignUpModal() { this.isSignUpOpen = true; }
  closeSignUpModal() { this.isSignUpOpen = false; this.signUpMessage = ''; }





  onSignUp() {
    if (!this.signupName || !this.signupEmail || !this.signupPassword || !this.signupContact || !this.signupAddress) {
      this.showMessage('signUpMessage', 'Please fill all fields');
      return;
    }

    const data = {
      full_name: this.signupName,
      email: this.signupEmail,
      password: this.signupPassword,
      contact_number: this.signupContact,
      address: this.signupAddress
    };

    this.userService.signup(data).subscribe({
      next: () => this.showMessage('signUpMessage', 'Sign Up successful! You can now log in.', 2000),
      error: (err: any) => this.showMessage('signUpMessage', 'Sign Up failed: ' + (err.error?.message || err.message))
    });
  }

  // ================= FORGOT PASSWORD =================
  openForgotPassword() {
    this.router.navigate(['/forgot-password']);
  }

  // ================= ADMIN MODAL =================
  openAdminModal(mode: 'login' | 'register' = 'login') {
    this.isAdminModalOpen = true;
    this.adminMode = mode;
    this.resetAdminFields();
  }

  closeAdminModal() {
    this.isAdminModalOpen = false;
    this.resetAdminFields();
  }

  toggleAdminMode() {
    this.adminMode = this.adminMode === 'login' ? 'register' : 'login';
    this.resetAdminFields();
  }

  // ================= ADMIN LOGIN =================
  onAdminLogin() {
    if (!this.adminEmail || !this.adminPassword) {
      this.showMessage('adminMessage', 'Please enter admin email and password');
      return;
    }

    this.userService.adminLogin(this.adminEmail, this.adminPassword).subscribe({
      next: (res: any) => {
        this.showMessage('adminMessage', 'Admin login successful!', 1500);
        if (res.token) localStorage.setItem('admin_token', res.token);
        this.closeAdminModal();
        this.router.navigate(['/admin/dashboard']);
      },
      error: (err: any) => this.showMessage('adminMessage', 'Admin login failed: ' + (err.error?.message || err.message))
    });
  }

  // ================= ADMIN REGISTRATION =================
  onAdminRegister() {
    if (!this.adminRegisterName || !this.adminRegisterEmail || !this.adminRegisterPassword) {
      this.showMessage('adminRegisterMessage', 'Please fill all fields');
      return;
    }

    const data = {
      full_name: this.adminRegisterName,
      email: this.adminRegisterEmail,
      password: this.adminRegisterPassword
    };
  }
}
