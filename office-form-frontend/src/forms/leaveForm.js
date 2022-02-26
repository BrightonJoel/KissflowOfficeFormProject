import React, {useState} from "react";
import { LeaveFormMain } from "./leaveFormStyles";

export default function LeaveFrom() {
    const [statusMessage ,setStateMessage] = useState(null);
    return (
        <LeaveFormMain>
            <h1>Leave Request form</h1>
            <form>
                <label htmlFor="EmpId">Employee ID : </label>
                <input htmlFor="EmpId" type="text" autoFocus/>
                <label htmlFor="EmpEmail">Company Email ID : </label>
                <input htmlFor="EmpEmail" type="email" />
                <label htmlFor="fromdate">From date : </label>
                <input htmlFor="fromdate" type="date"></input>
                <label htmlFor="todate">To date : </label>
                <input htmlFor="todate" type="date" />
                <label htmlFor="reason">Reason htmlFor Leave : </label>
                <textarea rows="5" htmlFor="reason" minLength="10"></textarea>
                {statusMessage ? (
                <p>{statusMessage}</p>
                ):(console.log("Message is null"))}
                <button type="submit">Submit</button>
                <button type="reset">Reset</button>
            </form>

        </LeaveFormMain>
    )
}