import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

//add new imports
import { ExerciseComponent } from './exercise/exercise.component';
import { RoutineComponent } from './routine/routine.component';
import { RoutineListComponent } from './routine_list/routine_list.component';
import { SignInComponent } from './sign-in/sign-in.component';

const routes: Routes = [
  //adding routes
  {
    path: 'routine-list',
    component: RoutineListComponent,
    data: { title: 'List of Routines' }
  },
  {
    path: 'routine/:id',
    component: RoutineComponent,
    data: { title: 'view of routine' }
  },
  {
    path: 'exercise/:id',
    component: ExerciseComponent,
    data: { title: 'view of exercise' }
  },

  {
    path: 'sign-in',
    component: SignInComponent,
    data: { title: 'sign in' }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
