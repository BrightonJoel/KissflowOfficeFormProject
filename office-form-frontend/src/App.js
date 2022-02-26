import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

//pages
import Api from "./pages/api";
import About from "./pages/about";
import Dashboard from "./pages/dashboard"
import Header from "./topAndBottomComponent/header";
import Footer from "./topAndBottomComponent/footer"

export default function App() {
  return (
    <Router>
      <Routes>

        <Route exact path="/"
          element={
            <React.Fragment>

              <Header name="Dashboard" />
              <Dashboard />
              <Footer name="Dashbord" />

            </React.Fragment>}
        />

        <Route path="/api" element={
          <React.Fragment>

            <Header name="Dashboard" />
            <Api />
            <Footer name="Dashbord" />

          </React.Fragment>}
        />

        <Route path="/about" element={
          <React.Fragment>
            
            <Header/>
            <About />
            <Footer name="Dashbord" />

          </React.Fragment>}
        />

      </Routes>
    </Router>
  );
}

