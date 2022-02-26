import styled from "styled-components";
import { Colors } from "../gobal";

export const LeaveFormMain = styled.div`
  margin: 20px auto 100px;
  background-color: ${Colors.darkest};
  width: 50%;
  border-radius:12px; 
  color:${Colors.lightest};
  text-align: center;
  padding: 30px;
  form{
    text-align:left;
    padding: 30px 30px 0;
    width: 100%;
  }
  h1{
      color:${Colors.light}
  }
  label{
      display:inline-block;
      padding: 10px 10px 10px 0;
      font-size: 1.25rem;
  }
  input{
      display:inline-block;
      padding: 10px;
      outline-color:${Colors.darkest};
      border-color:${Colors.light};
      width: 100%;
      border-radius: 8px;
      background-color:${Colors.lightest};
      color:${Colors.darkest};
      border-width:3px;

  }
  textarea{
      padding: 10px;
      display:block;
      border-color:${Colors.light};
      outline-color:${Colors.darkest};
      border-radius: 8px;
      background-color:${Colors.lightest};
      color:${Colors.darkest};
      width: 100%;
      border-width:3px;

  }
  button{
    border-radius: 8px;
    padding: 5px 20px;
    background-color: ${Colors.light};
    outline : None;
    border-color: ${Colors.light};
    color:${Colors.darkest};
    margin:  20px 20px 20px 0;
  }
  `
