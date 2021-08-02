import React, { useState } from "react";
import "adminbsb-materialdesign/plugins/bootstrap/css/bootstrap.css";
import "adminbsb-materialdesign/plugins/node-waves/waves.css";
import "adminbsb-materialdesign/plugins/animate-css/animate.css";
import "adminbsb-materialdesign/css/style.css";
import GoogleFontLoader from "react-google-font-loader";
import AuthHandler from "../utils/AuthHandler";
function Login() {
  document.body.className = "login-page";
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    loginStatus: 0,
  });
  const formSubmit = (event) => {
    event.preventDefault();
    // console.log(formData);
    setFormData({ ...formData, loginStatus: 1 });
    AuthHandler.login(formData.username, formData.password, handleResponse);
  };
  const handleResponse = (data) => {
    console.log(data);
    if (data.error) {
      setFormData({ ...formData, loginStatus: 4 });
    } else {
      setFormData({ ...formData, loginStatus: 3 });
    }
  };
  const getMessage = () => {
    if (formData.loginStatus === 0) {
      return "";
    } else if (formData.loginStatus === 1) {
      return (
        <div className="alert alert-warning">
          <strong>Logging In!</strong> Please wait!!
        </div>
      );
    } else if (formData.loginStatus === 3) {
      return (
        <div className="alert alert-success">
          <strong>Login Success!</strong>
        </div>
      );
    } else if (formData.loginStatus === 4) {
      return (
        <div className="alert alert-danger">
          <strong>Invalid Login!</strong>
        </div>
      );
    }
  };
  return (
    <>
      <GoogleFontLoader
        fonts={[
          {
            font: "Roboto",
            weights: [400, "400i"],
          },
        ]}
        subsets={["latin", "cyrillic-ext"]}
      />
      <GoogleFontLoader
        fonts={[
          {
            font: "Material+Icons",
          },
        ]}
      />
      <div className="login-box">
        <div className="logo">
          <a>
            Admin<b>BSB</b>
          </a>
          <small>Admin BootStrap Based - Material Design</small>
        </div>
        <div className="card">
          <div className="body">
            <form id="sign_in" method="POST" onSubmit={formSubmit}>
              <div className="msg">Sign in to start your session</div>
              <div className="input-group">
                <span className="input-group-addon">
                  <i className="material-icons">person</i>
                </span>
                <div className="form-line">
                  <input
                    type="text"
                    className="form-control"
                    name="username"
                    placeholder="Username"
                    required
                    onChange={(e) => {
                      setFormData({ ...formData, username: e.target.value });
                    }}
                  />
                </div>
              </div>
              <div className="input-group">
                <span className="input-group-addon">
                  <i className="material-icons">lock</i>
                </span>
                <div className="form-line">
                  <input
                    type="password"
                    className="form-control"
                    name="password"
                    placeholder="Password"
                    required
                    onChange={(e) => {
                      setFormData({ ...formData, password: e.target.value });
                    }}
                  />
                </div>
              </div>
              <div className="row">
                <div className="col-xs-8 p-t-5">
                  <input
                    type="checkbox"
                    name="rememberme"
                    id="rememberme"
                    className="filled-in chk-col-pink"
                  />
                  <label htmlFor="rememberme">Remember Me</label>
                </div>
                <div className="col-xs-4">
                  <button
                    className="btn btn-block bg-pink waves-effect"
                    type="submit"
                    onClick={formSubmit}
                  >
                    SIGN IN
                  </button>
                </div>
              </div>
              <div className="row m-t-15 m-b--20">
                <div className="col-xs-6">
                  <a href="sign-up.html">Register Now!</a>
                </div>
                <div className="col-xs-6 align-right">
                  <a href="forgot-password.html">Forgot Password?</a>
                </div>
              </div>
              {getMessage()}
              {/* <div class="alert alert-success">
                                <strong>Well done!</strong> You successfully read this important alert message.
                            </div> */}
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login;
