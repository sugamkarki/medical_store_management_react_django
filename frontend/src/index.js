import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import MainComponent from "./components/MainComponent";
import Login from "./pages/Login";
ReactDOM.render(
  <Router>
    <Switch>
      <Route exact path="/" component={Login} />
      <Route exact path="/home" component={MainComponent} />
    </Switch>
  </Router>,
  document.getElementById("root")
);
