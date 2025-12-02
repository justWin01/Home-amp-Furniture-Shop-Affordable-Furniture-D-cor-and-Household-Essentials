import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  slides = [
    { image: 'assets/images/furniture.jpg', caption: 'Wooden furniture collection' },
    { image: 'assets/images/decor.jpg', caption: 'Home décor items' },
    { image: 'assets/images/essentials.jpg', caption: 'Home essentials' }
  ];

  currentSlide = 0;
  slideInterval: any;

  ngOnInit() {
    this.startSlider();
  }

  startSlider() {
    this.slideInterval = setInterval(() => {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    }, 3000); // change image every 3 seconds
  }

  pauseSlider() {
    clearInterval(this.slideInterval);
  }

  resumeSlider() {
    this.startSlider();
  }

  prevSlide() {
    this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
  }

  nextSlide() {
    this.currentSlide = (this.currentSlide + 1) % this.slides.length;
  }
}
