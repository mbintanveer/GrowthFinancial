import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReceivingsDetailsComponent } from './receivings-details.component';

describe('ReceivingsDetailsComponent', () => {
  let component: ReceivingsDetailsComponent;
  let fixture: ComponentFixture<ReceivingsDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReceivingsDetailsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReceivingsDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
