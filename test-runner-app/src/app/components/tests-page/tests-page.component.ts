import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-tests-page',
  templateUrl: './tests-page.component.html',
  styleUrls: ['./tests-page.component.scss']
})
export class TestsPageComponent implements OnInit {

  path: String
  constructor(private router: Router) {
    const testsPath = localStorage.getItem('tests_path')
    if (!testsPath) {
      router.navigate(['']);
    }
    this.path = testsPath
  }

  ngOnInit() {
  }

}
