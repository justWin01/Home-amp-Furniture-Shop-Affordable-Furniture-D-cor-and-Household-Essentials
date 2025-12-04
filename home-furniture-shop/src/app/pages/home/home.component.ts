import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],   // <-- REQUIRED for *ngFor
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, OnDestroy {

  slides = [
    { image: 'images/decor.jpg', caption: 'Decor Collection' },
    { image: 'images/essentials.jpg', caption: 'Home Essentials' },
    { image: 'images/furniture.png', caption: 'Premium Furniture' }
  ];


  currentSlide = 0;
  private intervalId: any;

  ngOnInit(): void {
    this.startAutoSlide();
  }

  ngOnDestroy(): void {
    this.pauseSlider();
  }

  startAutoSlide(): void {
    this.intervalId = setInterval(() => {
      this.nextSlide();
    }, 3000);
  }

  pauseSlider(): void {
    clearInterval(this.intervalId);
  }

  resumeSlider(): void {
    this.startAutoSlide();
  }

  nextSlide(): void {
    this.currentSlide = (this.currentSlide + 1) % this.slides.length;
  }

  prevSlide(): void {
    this.currentSlide =
      (this.currentSlide - 1 + this.slides.length) % this.slides.length;
  }
}
