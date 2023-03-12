import React from 'react';
import Chat from '../LiveChat/Chat'
import PmChat from '../LiveChat/PmChat';


function ChannelMessages({ messages, toggleChat }) {
    // console.log('', '\n', '--------------CHANNEL MESSAGES COMPONENT DATA--------------', '\n', toggleChat, '\n', '')

    return (
        <>
        {toggleChat === false ? <Chat /> : <PmChat />}
        </>
    )
}

export default ChannelMessages
