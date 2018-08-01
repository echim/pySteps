import React, { Component } from 'react';
import TestsManager from '../components/TestsManager';

type Props = {};

export default class TestsPage extends Component<Props> {
  props: Props;

  render() {
    return <TestsManager />;
  }
}
