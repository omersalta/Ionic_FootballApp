import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StatPage } from './stat.page';

describe('StatPage', () => {
  let component: StatPage;
  let fixture: ComponentFixture<StatPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StatPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StatPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
