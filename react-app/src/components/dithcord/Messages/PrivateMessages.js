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
            
        </PmChat>
    )
};

export default PrivateChats

const PmChat = styled.div `
    display: flex;
    box-sizing: border-box;
`
