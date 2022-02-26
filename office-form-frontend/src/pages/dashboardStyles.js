import styled from "styled-components";
import {Colors} from "../gobal"

export const DashboardMain = styled.div`
    margin: 20px auto;
    width: 60%;
    text-align:center;
    background-color:${Colors.darkest};
    color: ${Colors.lightest};
    border-radius: 12px;
    padding:20px 30px 40px;
    h1{
        color:${Colors.light};
    }

`
export const DashboardForm = styled.div`
    text-align:left;
    background-color:${Colors.dark};
    border-radius: 12px;
    padding: 30px 30px 50px;
    margin: 20px 0;

    h2{
        color: ${Colors.light};
    }

    button{
        float: right;
        border-radius: 8px;
        padding: 5px 10px;
        background-color: ${Colors.light};
        outline : None;
        border-color: ${Colors.light};
    }

    `