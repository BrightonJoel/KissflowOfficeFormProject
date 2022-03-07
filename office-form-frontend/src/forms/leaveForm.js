import React, { useState } from "react";
import { LeaveFormMain } from "./leaveFormStyles";

export default function LeaveFrom() {
    const [statusMessage, setStatusMessage] = useState(null);
    const [empid, setEmpid] = useState("");
    const [empEmail, setEmpEmail] = useState("");
    const [fromDate, setFromDate] = useState("");
    const [toDate, setToDate] = useState("")
    const [reason, setReason] = useState("");

    let handleSubmit = async (e) => {
        e.preventDefault();
        try {
          let res = await fetch("http://localhost:5000/api/leaveFormSubmit", {
            method: "POST",
            headers : {
                'Content-Type':'application/json'
          },
            body: JSON.stringify({
              empid: empid,
              email: empEmail,
              fromdate: fromDate,
              todate: toDate,
              reason: reason
            }),
          });
          let resJson = await res.json();
          if (res.status === 200) {
            setEmpid("");
            setEmpEmail("");
            setFromDate("");
            setToDate("");
            setReason("")
            setStatusMessage(resJson['message']);
          } else {
            setStatusMessage(resJson['message']);
          }
          
        } catch (err) {
          console.log(err);
        }
      };


    return (
        <LeaveFormMain>
            <h1>Leave Request form</h1>
            <form>
                <label htmlFor="EmpId">Employee ID* : </label>
                <input htmlFor="EmpId" type="text" autoFocus required 
                value={empid}  onChange={(event) => setEmpid(event.target.value)} />

                <label htmlFor="EmpEmail" >Company Email ID* : </label>
                <input htmlFor="EmpEmail" type="email" required 
                value={empEmail} onChange={(event) => setEmpEmail(event.target.value)}/>

                <label htmlFor="fromdate">From date* : </label>
                <input htmlFor="fromdate" type="date" required
                value={fromDate} onChange={(event) => setFromDate(event.target.value)}/>

                <label htmlFor="todate">To date* : </label>
                <input htmlFor="todate" type="date" required 
                value={toDate} onChange={(event) => setToDate(event.target.value)}/>

                <label htmlFor="reason">Reason for leave* : </label>
                <textarea rows="5" htmlFor="reason" minLength="10" required
                value={reason}  onChange={(event) => setReason(event.target.value)}></textarea>

                {statusMessage ? (
                    <p>{statusMessage}</p>
                ) : (console.log("Message is null"))}
                <button type="submit" onClick = {handleSubmit}>Submit</button>
                <button type="reset">Reset</button>
            </form>

        </LeaveFormMain>
    )
}