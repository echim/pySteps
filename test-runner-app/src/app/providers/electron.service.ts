import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable'
import { ipcRenderer, webFrame, remote } from 'electron';
import * as childProcess from 'child_process';
import * as fs from 'fs';



@Injectable()
export class ElectronService {

  ipcRenderer: typeof ipcRenderer;
  webFrame: typeof webFrame;
  remote: typeof remote;
  childProcess: typeof childProcess;
  fs: typeof fs;

  constructor() {
    // Conditional imports
    if (this.isElectron()) {
      this.ipcRenderer = window.require('electron').ipcRenderer;
      this.webFrame = window.require('electron').webFrame;
      this.remote = window.require('electron').remote;

      this.childProcess = window.require('child_process');
      this.fs = window.require('fs');
    }
  }

  isElectron = () => {
    return window && window.process && window.process.type;
  }

  selectDirectory = () => {
    return new Observable((observer) => {
      this.remote.dialog.showOpenDialog({ properties: ['openDirectory'] }, (pathInfo) => {
        if (!pathInfo || !pathInfo[0]) {
          observer.error(new Error('Unable to get path'))
        }
        observer.next(pathInfo[0])
      });
    })
  }

}
