import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import styled from 'styled-components';

function PrivateChats() {
    const dispatch = useDispatch();
    const currentUser = useSelector(state => state.session.user);

    // get chats from currentUser inspect key below
    console.log('', '\n', '--------------PM COMPONENT DATA--------------', '\n', currentUser, '\n', '--------------PM COMPONENT DATA--------------')
    
    useEffect(() => {
        //
    });


    return (
        <PmChat>
            PM's
        </PmChat>
    )
};

export default PrivateChats

const PmChat = styled.div `
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    border: 2px solid black;
    border-radius: 50px;
    margin: .3rem 1rem;
    background-color: rgba(30, 30, 30, 1);
    color: rgba(159, 159, 159, 1);
    font-size: 10pt;
`
