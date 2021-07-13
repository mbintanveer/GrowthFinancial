import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReceivingsListComponent } from './receivings-list.component';

describe('ReceivingsListComponent', () => {
  let component: ReceivingsListComponent;
  let fixture: ComponentFixture<ReceivingsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReceivingsListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReceivingsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
