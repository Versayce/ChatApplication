import React from 'react';
import { ServerWrapper, ImageWrapper, ServerImageWrapper } from '../DithcordStyles';
import styled from 'styled-components';
import { useDispatch } from 'react-redux';
import { clearServer, getOneServer } from '../../../store/server';
import { clearAllChannels, getAllChannelsByServerId, getChannel, loadChannel } from '../../../store/channel';
import { clearMessages, getChannelMessages } from '../../../store/message';
import NewServerFormModal from '../Forms/ServerForm/Add/NewServerFormModal'
import AllServersModal from './AllServersList';
import PrivateMessaging from '../Messages/PrivateMessages'
import { getAllChatsByUserId } from '../../../store/pm';

function Servers({ user, servers }) {
    const dispatch = useDispatch()

    console.log('', '\n', '--------------SERVERS COMPONENT DATA--------------', '\n', user, '\n', '')

    const handlePm = () => {
        // clear all server channels and channel messages + pm messages first
        dispatch(clearMessages())
        // dispatch(clearPmMessages())
        dispatch(clearAllChannels())
        dispatch(clearServer())
        // handle grabbing all pm chat rooms by userId here:
        dispatch(getAllChatsByUserId(user.id))
        return
    }

    const oneServer = (serverId, channelId) => {
        dispatch(clearMessages())
        if(serverId) {
            dispatch(getAllChannelsByServerId(serverId))
            dispatch(getOneServer(serverId))
        }if(channelId) {
            dispatch(getChannel(channelId))
            dispatch(getChannelMessages(channelId))
        }else {
            dispatch(loadChannel({}))
        }
        return
    }

    
    return (
        <ServerWrapper>
            <PmChatButton onClick={() => handlePm()}>PM's</PmChatButton>
            <AllServersModal />
            <NewServerFormModal />
            <UserServers>
                {servers && servers?.map((server) => (
                    <div onClick={() => oneServer(server.id, server.channels[0]?.id)} key={server.id}>
                            {server.serverImage.length === 3 ? 
                                <ImageWrapper>
                                    <div className='private-server-imagename'>
                                        {server.serverImage}
                                    </div>
                                </ImageWrapper> : <ImageWrapper as="img" src={server.serverImage} />
                            }
                    </div>
                ))}
            </UserServers>
        </ServerWrapper>
    )
}


export default Servers


const PmChatButton = styled.button`
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

const UserServers = styled.div`

`
