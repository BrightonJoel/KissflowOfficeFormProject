import styled from "styled-components";
import { Colors } from "../gobal";

export const FooterMain = styled.div`
    background-color: ${Colors.darkest};
    position: fixed;
    bottom: 0;
    width: 100%;
    h1{
        color: ${Colors.lightest};
        font-size: 25px;
        padding: 20px 0;
    }
  `