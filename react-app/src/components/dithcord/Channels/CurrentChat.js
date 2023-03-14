import React, { useEffect } from 'react';
import ChannelMessages from '../Messages/ChannelMessages';
import { useDispatch, useSelector } from 'react-redux';
import { getChannelMessages } from '../../../store/message';
import { MessageContainerWrapper } from '../DithcordStyles';


function CurrentChat({ chat, toggleChat }) {
    const dispatch = useDispatch();
    const currentChat = useSelector(state => state.pmchatrooms.oneChat);
    // const chatMessages = useSelector(state => state.messages.chatMessages);
    // const chatMessages = currentChat.messages

    const chatMessagesArray = currentChat.messages

    useEffect(() => {
        if(currentChat.id) {
            // dispatch(getChatMessages(currentChat.id));
        }

    }, [dispatch, currentChat])

    // console.log('', '\n', '--------------CURRENT CHAtS COMPONENT DATA--------------', '\n', chatMessagesArray, '\n', '')

    return (
        <MessageContainerWrapper>
            <ChannelMessages messages={chatMessagesArray} chatId={currentChat.id} toggleChat={toggleChat} />
        </MessageContainerWrapper>
    )
}


export default CurrentChat
