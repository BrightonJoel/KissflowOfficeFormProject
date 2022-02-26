import React, { useEffect, useState } from "react"

function App() {


  const [data, setData] = useState();

  useEffect(() => 
    fetch("/members").then(
      res => {
        return res.json()
      }
    ).then(
      data => {
        // some stuff
        setData(data)
        console.log(data)
      }
    ).catch(err => {
      // some error handling
      console.log("data traction failed!!")
    })
  ,[])
  return (
    <p>nothing to show :|</p>

  );
}

export default App;
