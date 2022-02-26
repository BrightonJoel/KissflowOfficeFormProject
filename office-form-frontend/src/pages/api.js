import React , {useEffect, useState} from "react";

export default function Api(){
    const [data, setData] = useState(null);

  useEffect(() =>
    fetch("/members").then(
      res => {
        return res.json()
      }
    ).then(
      data => {
        // some stuff
        setData(data)
        console.log(data.member[0])
      }
    ).catch(err => {
      // some error handling
      console.log("data traction failed!!")
    })
    , [])
return(
    <div>
    {
      (data) ? (
        data.member.map((member, index) => (
          <p key={index}> {member}</p>
        ))

      ) : (
        <p>loading the api </p>
      )
    }

  </div > )
}