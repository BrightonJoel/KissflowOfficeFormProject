import React from "react";
import { DashboardMain, DashboardForm } from "./dashboardStyles";
import { useNavigate } from 'react-router-dom';

export default function Dashboard(){
    const navigate = useNavigate();
    return(
        <DashboardMain>
            <h1>Request Forms</h1>
            <DashboardForm >
                <h2>Leave Request Form</h2>
                <p>This form is used to request leave from mangers or higher-ups</p>
                <button onClick={() => navigate('/leaveForm')}>Request Leave</button>
            </DashboardForm>
        </DashboardMain>
        )
}