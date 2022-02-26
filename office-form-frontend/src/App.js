import React from "react"
import { BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";

//pages
import Api from "./pages/api";


export default function App() {
  return (
    <Router>
      <Routes>

        <Route exact path="/" element={<h1>create the dasboard</h1>}/>

        <Route path="/api" element = {<Api/>}/>

        
        

      </Routes>
    </Router>
  );
}

