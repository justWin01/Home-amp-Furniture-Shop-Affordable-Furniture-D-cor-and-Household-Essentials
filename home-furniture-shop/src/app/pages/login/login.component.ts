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
  email = '';
  password = '';
  message = '';

  // Sign Up modal fields
  isSignUpOpen = false;
  signupName = '';
  signupEmail = '';
  signupPassword = '';
  signupContact = '';
  signupAddress = '';
  signUpMessage = '';

  constructor(private userService: UserService, private router: Router) {}

  // Login method
  onLogin() {
    if (!this.email || !this.password) {
      this.message = 'Please enter email and password';
      return;
    }

    this.userService.login(this.email, this.password).subscribe({
      next: (res: any) => {
        this.message = 'Login successful!';
        setTimeout(() => this.message = '', 5000);
        if (res.token) localStorage.setItem('token', res.token);
        this.router.navigate(['/customerui']);
      },
      error: (err: any) => {
        this.message = 'Login failed: ' + (err.error?.message || err.message);
        setTimeout(() => this.message = '', 5000);
      }
    });
  }

  // Sign Up modal methods
  openSignUpModal() {
    this.isSignUpOpen = true;
  }

  closeSignUpModal() {
    this.isSignUpOpen = false;
    this.signUpMessage = '';
  }

  onSignUp() {
    if (!this.signupName || !this.signupEmail || !this.signupPassword || !this.signupContact || !this.signupAddress) {
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
        setTimeout(() => this.message = '', 5000);
      }
    });
  }
}
