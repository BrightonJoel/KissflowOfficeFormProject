import React, { useState } from "react";
import { LeaveFormMain } from "./leaveFormStyles";

export default function LeaveFrom() {
    const [statusMessage, setStateMessage] = useState(null);
    return (
        <LeaveFormMain>
            <h1>Leave Request form</h1>
            <form>
                <label htmlFor="EmpId">Employee ID* : </label>
                <input htmlFor="EmpId" type="text" autoFocus required />
                <label htmlFor="EmpEmail" >Company Email ID* : </label>
                <input htmlFor="EmpEmail" type="email" required />
                <label htmlFor="fromdate">From date* : </label>
                <input htmlFor="fromdate" type="date" required></input>
                <label htmlFor="todate">To date* : </label>
                <input htmlFor="todate" type="date" required />
                <label htmlFor="reason">Reason for leave* : </label>
                <textarea rows="5" htmlFor="reason" minLength="10" required></textarea>
                {statusMessage ? (
                    <p>{statusMessage}</p>
                ) : (console.log("Message is null"))}
                <button type="submit">Submit</button>
                <button type="reset">Reset</button>
            </form>

        </LeaveFormMain>
    )
}