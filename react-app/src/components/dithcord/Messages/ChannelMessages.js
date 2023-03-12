import React from 'react';
import Chat from '../LiveChat/Chat'


function ChannelMessages({ messages, channelId }) {
    console.log('', '\n', '--------------CHANNEL MESSAGES COMPONENT DATA--------------', '\n', messages, '\n', '')

    return (
        <Chat newmessages={messages} />
    )
}

export default ChannelMessages
