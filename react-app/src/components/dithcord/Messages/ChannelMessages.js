import React from 'react';
import Chat from '../LiveChat/Chat'
import PmChat from '../LiveChat/PmChat';


function ChannelMessages({ messages, channelId, toggleChat }) {
    console.log('', '\n', '--------------CHANNEL MESSAGES COMPONENT DATA--------------', '\n', messages, '\n', '')

    return (
        <>
        {toggleChat === true ? <Chat /> : <PmChat newmessages={messages} />}
        </>
    )
}

export default ChannelMessages
