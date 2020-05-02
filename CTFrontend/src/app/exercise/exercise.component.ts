import { Component, OnInit } from '@angular/core';

@Component({
  //tag name almost like html selector
  //we can invoke this app by using <app-exercise tag>
  selector: 'app-exercise',
  //link to html
  templateUrl: './exercise.component.html',
  //link to css
  styleUrls: ['./exercise.component.css']
})
export class ExerciseComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
