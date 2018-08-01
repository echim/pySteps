/* eslint flowtype-errors/show-errors: 0 */
import React from 'react';
import { Switch, Route } from 'react-router';
import App from './containers/App';
import HomePage from './containers/HomePage';
import TestsPage from './containers/TestsPage';

export default () => (
  <App>
    <Switch>
      <Route path="/tests" component={TestsPage} />
      <Route path="/" component={HomePage} />
    </Switch>
  </App>
);
