// @flow
import React, { Component } from 'react';
import { Redirect } from 'react-router';
import { isNull } from 'util';
import './TestsManager.css';

const exec = require("child_process").exec;
const { remote, BrowserWindow } = require('electron')

const fs = require('fs');
const path = require('path')
const shell = require('shelljs');

type Props = {};

export default class TestsManager extends Component<Props> {

  mainWindow: BrowserWindow;

  constructor(props) {
    super(props);
    this.state = {
      testsPath: localStorage.getItem('tests_path') || null,
      testResults: null
    }
    this.loadTestResults()
    this.mainWindow = remote.getCurrentWindow()
  }

  runTest = (id) => {
    if (shell.which('python')) {
      // @todo replace this with dynamic path find
      this.mainWindow.hide()
      let command = null
      if(process.platform === 'darwin') {
        command = '../vnv/bin/python3 -m pytest ' + id;
      }
      else {
        command = "..\\vnv\\Scripts\\python.exe -m pytest " + id;
      }
      exec(command, { cwd: this.state.testsPath }, (error, stdout, stderr) => {
        if (error) {
          console.log('error', error);
        }
        console.log('stdout', stdout);
        console.log('stderr', stderr);
        this.mainWindow.show()
        this.reloadPage()
      });

    }
    else {
      alert('Please install python 3.6.6')
    }

  }

  loadTestResults = () => {
    if (isNull(this.state.testsPath)) {
      return
    }
    const filePath = path.join(this.state.testsPath, 'pyTest_runs.json')

    fs.readFile(filePath, 'utf8', (err, testResults) => {
      if (err || testResults === '') {
        alert('Unable to load test results file.')
        throw new Error('Unable to load test results file.')
      }
      this.setState({
        testResults: JSON.parse(testResults)
      });
    });
  }

  reloadPage = () => {
    this.loadTestResults()
  }

  resetTestsPath = () => {
    localStorage.removeItem('tests_path')
    this.setState({
      testsPath: null
    });
  }

  render() {
    if (isNull(this.state.testsPath)) {
      return <Redirect to='/' />
    }

    return (
      <div>
        <button onClick={this.resetTestsPath}>Clear tests path</button>
        <button onClick={this.reloadPage}>Reload</button>
        <p>Tests path: {this.state.testsPath} <button onClick={() => this.runTest('')}>Run all tests</button></p>

        <table>
          <thead />
          <tbody>
            {
              this.state.testResults && this.state.testResults.tests ?
                this.state.testResults.tests.map((test, index) => {
                  return (
                    <tr key={index}>
                      <td>
                        {test.test}
                      </td>
                      <td>
                        {test.description}
                      </td>
                      <td>
                        {test.duration.toFixed(2)}
                      </td>
                      <td>
                        <p className={test.status} >{test.status}</p>
                      </td>
                      <td>
                        -
                      </td>
                      <td>
                        <button onClick={() => this.runTest(test.test)}>Run again</button>
                      </td>
                    </tr>
                  )
                }) :
                <tr>
                  <td>
                    <p>No tests runned yet </p>
                  </td>
                </tr>
            }
          </tbody>
        </table>

      </div>
    )
  }
}
