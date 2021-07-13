import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddReceivingsComponent } from './add-receivings.component';

describe('AddReceivingsComponent', () => {
  let component: AddReceivingsComponent;
  let fixture: ComponentFixture<AddReceivingsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddReceivingsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddReceivingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
