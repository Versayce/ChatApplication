import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getChannel } from '../../../store/channel';
import { getChat } from '../../../store/pm';
import { getChannelMessages } from '../../../store/message';
import AddChannelFormModal from '../Forms/ChannelForm/Add/AddChannelFormModal';
import EditChannelFormModal from '../Forms/ChannelForm/Edit/EditChannelFormModal';
import ServerDropDownMenu from '../Servers/ServerDropDownMenu';
import DeleteChannelButton from './DeleteChannelButton';
import DeleteChatButton from './DeleteChatButton';
import LogoutButton from '../../auth/LogoutButton';
import styled from 'styled-components';

function Channels({ channels, toggleChat, setToggleChat }) {
    const dispatch = useDispatch();
    const currentChatsObj = useSelector(state => state.pmchatrooms.allChats)
    const currentChats = Object.values(currentChatsObj)
    const currentChannels = Object.values(channels)
    const currentServerObj = useSelector(state => state.servers.oneServer)
    const currentServer = Object.values(currentServerObj)
    const sessionUser = useSelector(state => state.session.user)

    console.log('INSIDE OF CHANNELS COMPONENT', currentChats)

    const getOneChannel = (channelId) => {
        if (channelId) {
            setToggleChat(false)
            dispatch(getChannel(channelId))
            dispatch(getChannelMessages(channelId))
            // socket.emit("join", {user: currentUser.username, roomId: channelId})
        }
    }

    const getOneChat = (chatId) => {
        if (chatId) {
            setToggleChat(true)
            dispatch(getChat(chatId))
            //TODO keep chat buttons from disappearing
            // dispatch(getChatMessages(chatId))
            // socket.emit("join", {user: currentUser.username, roomId: channelId})
        }
    }


    return (
        <>
            <DropDown>
                <div className='server-name'>
                    {currentServer && currentServer[0]?.name}
                </div>
                <ServerDropDownMenu />
            </DropDown>
            {/* TODO break down into smaller components */}
            {toggleChat === true ? <ChatsContainer>
                {currentChats && currentChats.map((chat) => (
                    <ChannelOptions key={chat.id} >
                        <Chat onClick={() => getOneChat(chat.id)} key={chat.id}>
                            <h3 key={chat.id}>
                                {console.log('', '\n', '--------------CHAts COMPONENT DATA--------------', '\n', chat, '\n', '')}
                                {sessionUser.username === chat.users[0].username ? chat.users[1]?.username : chat.users[0].username}
                            </h3>
                        </Chat>
                        
                        <ChannelOptionButtons>
                            <DeleteChatButton key={chat.id} chatId={chat.id} />
                        </ChannelOptionButtons>
                    </ChannelOptions>
                ))}
            </ChatsContainer>
            // Render below if above condition is not met
            : <ChannelsContainer>
                {currentChannels && currentChannels.map((channel) => (
                    <ChannelOptions key={channel.id} >
                        <Channel onClick={() => getOneChannel(channel.id)} key={channel.id}>
                            {/* {console.log('', '\n', '--------------CHANNELS COMPONENT DATA--------------', '\n', channel, '\n', '')} */}
                            <h3 key={channel.id}>{channel.name}</h3>
                        </Channel>
                        {sessionUser
                            && (currentServer && sessionUser.id === currentServer[0]?.ownerId)
                            && (
                                <div>
                                    <ChannelOptionButtons>
                                        <EditChannelFormModal />
                                        <DeleteChannelButton key={channel.id} channelId={channel.id} />
                                    </ChannelOptionButtons>
                                </div>
                            )
                        }
                    </ChannelOptions>
                ))}
            </ChannelsContainer>}
            
            <UserInfo>
                <div className="logout-div">
                    <div className='currentuser-info'>
                    <img className="current-user-image" src={sessionUser.profile_img} alt={sessionUser.username} />
                    <p className='logout-username'>{sessionUser.username}</p>
                    </div>
                </div>
                <div className='logout-button-container'>
                <LogoutButton />
                </div>
            </UserInfo>
        </>
    )
}


const ChannelsContainer = styled.div `
    width: 100%;
    background-color: rgba(49, 49, 49, 0.8);
    height: 90%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    box-sizing: border-box;
`

const ChatsContainer = styled.div `
    width: 100%;
    background-color: rgba(49, 49, 49, 0.8);
    height: 90%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    box-sizing: border-box;
`

const Channel = styled.div `
    box-sizing: border-box;
    color: rgba(178, 178, 178, 1);
    margin: 10px 20px;
`

const Chat = styled.div `
    box-sizing: border-box;
    color: rgba(178, 178, 178, 1);
    margin: 10px 20px;
`

const DropDown = styled.div `
    background-color: #454545;
    height: fit-content;
`

const UserInfo = styled.div `
    width: 100%;
    height: 168px;
    display: flex;
    flex-direction: column;
    background-color: #454545;
    position: static;
`

const ChannelOptions = styled.div `
    box-sizing: border-box;
    display: flex;
    width: 100%;
    padding-top: 20px;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0px;
    &:hover{
        background-color: rgba(111, 111, 111, 1);
        cursor: pointer;
    }
`
const ChannelOptionButtons = styled.div `
    display: flex;
    flex-direction: row;
    gap: 5px;
    margin: 0px 10px;
`


export default Channels
