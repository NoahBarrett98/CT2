import { Component, OnInit } from '@angular/core';
import { RoutineService } from '../routine.service';

@Component({
  selector: 'app-routine',
  templateUrl: './routine.component.html',
  styleUrls: ['./routine.component.css'],
  //add provider
  providers:[RoutineService]
})
export class RoutineComponent implements OnInit {

  constructor(private api:RoutineService) {
        this.getRoutines()}

  ngOnInit(): void {
  }
  AllRoutines = [{Routine:'Routine'}]
  //define function lower down
  getRoutines = () => {
    //subscribe to observable
    this.api.getAllRoutines().subscribe(
      data => {
          this.AllRoutines = data;
      },
      error => {
        console.log('error');
      }
    )
  }


}
