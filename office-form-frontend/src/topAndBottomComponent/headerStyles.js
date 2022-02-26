import styled from 'styled-components'
import { Colors } from '../gobal'

export const HeaderMain = styled.div`
    background-color: ${Colors.darkest};
  a{
      display: inline-block;
      margin:  10px 40px;
      padding: 20px 50px;
      text-decoration: None;
      color: ${Colors.lightest};
      border-radius : 12px;
      
  }
  h1{
    font-size: 30px;
  }
  a:hover{
    color: ${Colors.light};
    background-color: ${Colors.dark}
  }
  `