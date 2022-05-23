import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SinglePageListComponent } from './single-page-list.component';

describe('SinglePageListComponent', () => {
  let component: SinglePageListComponent;
  let fixture: ComponentFixture<SinglePageListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SinglePageListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SinglePageListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
