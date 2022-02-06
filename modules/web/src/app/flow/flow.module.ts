import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainBoardComponent } from './main-board/main-board.component';
import { X6Directive } from './x6.directive';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    MainBoardComponent,
    X6Directive
  ]
})
export class FlowModule { }
