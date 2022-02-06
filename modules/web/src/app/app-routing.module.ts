import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainBoardComponent } from './flow/main-board/main-board.component'

const routes: Routes = [
  {
    path: 'flow',
    component: MainBoardComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
