// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.css';
import { remote } from 'electron'
import { Redirect } from 'react-router';

export default class Home extends Component<Props> {

  constructor(props) {
    super(props);
    this.state = {
      testsPath: localStorage.getItem('tests_path') || null,
    }
  }

  render() {
    if (this.state.testsPath !== null) {
      return <Redirect to='/tests' />
    }

    return (
      <div>
        <div>
          <button onClick={() => { this.onSelectTestsPath() }}>Select tests path</button>
        </div>
      </div>
    );
  }

  onSelectTestsPath() {
    remote.dialog.showOpenDialog({ properties: ['openDirectory'] }, this.handleNewPath);
  }

  handleNewPath = (newPath) => {
    if (newPath && newPath[0]) {
      localStorage.setItem('tests_path', newPath[0])
      this.setState({
        testsPath: newPath[0]
      });
    }
    else
      alert('No valid path')
  }
}
