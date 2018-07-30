import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TestsPageComponent } from './tests-page.component';

describe('TestsPageComponent', () => {
  let component: TestsPageComponent;
  let fixture: ComponentFixture<TestsPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TestsPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TestsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
