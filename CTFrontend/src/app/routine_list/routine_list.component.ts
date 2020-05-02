import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-routine_list',
  templateUrl: './routine_list.component.html',
  styleUrls: ['./routine_list.component.css']
})
export class RoutineListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  Description = ''
  RoutineName = 'Routine Name';
  RoutineList = []
  onKey_RName(event: any) { // without type info
    this.RoutineName = event.target.value;
  }
  onKey_Add_Exercise(event: any) { // without type info
    this.RoutineList.push(event.target.value);
  }

  saveRoutine() {
    //save method for db interaction
  
  }


  /*
  RoutineList = []
  Title = 'Enter Title'
  wait_for_title = false
  commited = false
  public getTitle(Title: string){
      console.log(Title);
      this.title = Title

  public getExercise(Name: string){
    this.RoutineList.push(Name);

  }*/

}
