import { Component, OnInit } from '@angular/core';
import { ElectronService } from '../../providers/electron.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(public electronService: ElectronService, private router: Router) {
    if (localStorage.getItem('tests_path')) {
      this.router.navigate(['/tests']);
    }
  }

  onSelectTestsPath() {
    this.electronService.selectDirectory().subscribe((tests_path) => {
      localStorage.setItem('tests_path', String(tests_path));
      this.router.navigate(['/tests']);
    }, (err) => {
      alert('Unable to load tests path')
    })
  }

  ngOnInit() {
  }

}
