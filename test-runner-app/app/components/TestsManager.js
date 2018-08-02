// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './TestsManager.css';
import { Redirect } from 'react-router';
import { isNull } from 'util';
var fs = require('fs');
var path = require('path')

type Props = {};

export default class TestsManager extends Component<Props> {

  constructor(props) {
    super(props);
    this.state = {
      testsPath: localStorage.getItem('tests_path') || null,
      testResults: null
    }

    this.loadTestResults()
  }

  render() {
    if (isNull(this.state.testsPath)) {
      return <Redirect to='/' />
    }

    return (
      <div>
        <button onClick={this.resetTestsPath}>Clear tests path</button>
        <button onClick={this.reloadPage}>Reload</button>
        <p>Tests path: {this.state.testsPath}</p>

        <div>
          {
            this.state.testResults && this.state.testResults.tests ?
              this.state.testResults.tests.map((test, index) => {
                const options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
                const date = new Date(test.timestamp * 1000)
                return (
                  <div key={index}>
                    <p>-------------------------------------------------------------------------------------------------</p>
                    <p>Name: {test.test}</p>
                    <p className={test.status} >Status: {test.status}</p>
                    <p>Duration: {test.duration} seconds</p>
                    <p>Run Date: {date.toLocaleDateString('en-US', options)}</p>
                  </div>
                )
              }) : null
          }
        </div>

      </div>
    )
  }


  loadTestResults = () => {
    if (isNull(this.state.testsPath)) {
      return
    }
    const filePath = path.join(this.state.testsPath, 'pyTest_runs.json')

    fs.readFile(filePath, 'utf8', (err, testResults) => {
      if (err) {
        alert('Unable to load test results file.')
        throw new Error('Unable to load test results file.')
      }
      this.setState({
        testResults: JSON.parse(testResults)
      });
    });
  }

  reloadPage = () => {
    window.location.reload()
  }

  resetTestsPath = () => {
    localStorage.removeItem('tests_path')
    this.setState({
      testsPath: null
    });
  }
}
