// @flow
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './TestsManager.css';
import { Redirect } from 'react-router';
import { isNull } from 'util';

type Props = {};

export default class TestsManager extends Component<Props> {

  constructor(props) {
    super(props);
    this.state = {
      testsPath: localStorage.getItem('tests_path') || null,
    }
  }

  render() {
    if (isNull(this.state.testsPath)) {
      return <Redirect to='/' />
    }

    return (
      <div>
        <button onClick={this.resetTestsPath}>Clear tests path</button>
        <Link to="/home">to Home</Link>
        <p>Tests path: {this.state.testsPath}</p>
      </div>
    )
  }

  resetTestsPath = () => {
    localStorage.removeItem('tests_path')
    this.setState({
      testsPath: null
    });
  }
}
