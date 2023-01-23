import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { io } from 'socket.io-client'
import { createMessage } from '../../../store/message';
import styled from 'styled-components'

let socket;


const Chat = ({ props }) => {
    const dispatch = useDispatch()
    let postedMessage;
    const [messages, setMessages] = useState([])
    const [chatInput, setChatInput] = useState("")

    const currentUser = useSelector(state => state.session.user)
    const currentChannel = useSelector(state => state.channels.oneChannel)
    const channelMessages = currentChannel.messages

    // console.log('========CHAT========', postedMessage)

    useEffect(() => {
        socket = io();
        socket.emit("join", { user: currentUser.username, roomId: currentChannel.id })
        socket.on("chat", (chat) => {
            console.log("=====ON CHAT====", chat)
            setMessages(messages => [...messages, chat])
        })



        return (() => {
            socket.disconnect()
            setMessages([])
        })
    }, [currentChannel.id, currentUser.username])




    const sendChat = (e) => {
        e.preventDefault()
        postedMessage = {
            "body": chatInput,
            "channel_id": currentChannel.id,
            "author_id": currentUser.id
        }
        //emitting message
        socket.emit("chat", { roomId: currentChannel.id, user: `${currentUser.username}`, msg: `${chatInput}` });
        //clear input field
        dispatch(createMessage(postedMessage))
        setChatInput("")
    }

    const updateChatInput = (e) => {
        setChatInput(e.target.value)
        // console.log('=====UPDATE CHAT INPUT FUNC======', e.target.value)
    }

    return (
        <>
            <MessageContainer>
                <NewMessage>
                    {messages.map((message, ind) => (
                        <div key={ind}>{`${message.user}: ${message.msg}`}</div>
                    ))}
                </NewMessage>    
                <Message>
                    {currentChannel && channelMessages && channelMessages.map(message => (
                        <div key={message.id}>{`${message.author.username}: ${message.body}`}</div>
                    ))}
                </Message>
            </MessageContainer>
        
            <MessagesForm>
                <form onSubmit={sendChat}>
                    <input className="message-input" value={chatInput} onChange={updateChatInput} />
                    <MessageButton as="button" type='submit'>Send</MessageButton>
                </form>
            </MessagesForm>
        </>
    )
}

const MessageContainer = styled.div`
    margin: 4%;
    overflow: auto;
    display: flex;
    flex-direction: column-reverse;
`

const Message = styled.address`
    display: flex;
    flex-direction: column;
    gap: 10px;
`
const NewMessage = styled.address`
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
`

const MessageButton = styled.button`
    width: 100px;
    height: 28.8px;
    float: left;
    position: relative;
    background-color: white;
    border: 0;
`

const MessagesForm = styled.div`
    display: flex;
    margin-top: auto;
    padding: 20px;
    background-color: rgb(143, 176, 165);
`

export default Chat
