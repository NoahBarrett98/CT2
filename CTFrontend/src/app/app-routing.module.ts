import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

//add new imports
import { exerciseComponent } from './exercise/exercise.component';
import { routineComponent } from './routine/routine.component';
import { routine-listComponent } from './routine-list/routine-list.component';
import { sign-inComponent } from './sign-in/sign-in.component';

const routes: Routes = [
  //adding routes
  {
    path: 'routine-list',
    component: routine-listComponent,
    data: { title: 'List of Routines' }
  },
  {
    path: 'routine/:id',
    component: routineComponent,
    data: { title: 'view of routine' }
  },
  {
    path: 'exercise/:id',
    component: exerciseComponent,
    data: { title: 'view of exercise' }
  },

  {
    path: 'sign-in',
    component: sign-inComponent,
    data: { title: 'sign in' }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
