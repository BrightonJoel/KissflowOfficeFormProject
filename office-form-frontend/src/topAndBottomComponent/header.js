import React from "react";
import {Link} from "react-router-dom";
import {HeaderMain} from "./headerStyles";

export default function Header(props){
    return(
        <HeaderMain>
           <center>
            <Link to="/"><h1>Home</h1> </Link>
            <Link to="/api"><h1>Api</h1></Link>
            <Link to ="/about"> <h1>About</h1> </Link>
            </center>
        </HeaderMain>
    )
}