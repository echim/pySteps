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

        <table>
          <thead></thead>
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
                    </tr>
                  )
                }) : null
            }
          </tbody>
        </table>

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
    this.loadTestResults()
  }

  resetTestsPath = () => {
    localStorage.removeItem('tests_path')
    this.setState({
      testsPath: null
    });
  }
}
