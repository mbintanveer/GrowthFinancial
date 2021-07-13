import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VendorsDetailsComponent } from './vendors-details.component';

describe('VendorsDetailsComponent', () => {
  let component: VendorsDetailsComponent;
  let fixture: ComponentFixture<VendorsDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VendorsDetailsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VendorsDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
