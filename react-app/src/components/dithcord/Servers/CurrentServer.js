import React, { useEffect } from 'react';
import styled from 'styled-components';
import Channels from '../Channels/Channels'
import CurrentChannel from '../Channels/CurrentChannel'
import ServerUsers from './ServerUsers';
import { useDispatch, useSelector } from 'react-redux';
import { getOneServer } from '../../../store/server';


function CurrentServer({ server, toggleChat }) {
    const dispatch = useDispatch();
    const serverChannels = useSelector((state) => state.channels.allChannels)
    const currentChannel = useSelector((state) => state.channels.oneChannel)
    const currentServer = useSelector((state) => state.servers.oneServer)

    // console.log('', '\n', '--------------CURRENT SERVERS COMPONENT DATA--------------', '\n', currentServer, '\n', '')

    useEffect(() => {
        if(server.id) {
            dispatch(getOneServer(server.id))
        }
    },[dispatch, server])

    return (
        <>
        <ChannelsWrapper>
            <Channels channels={serverChannels} server={currentServer} toggleChat={toggleChat} />
        </ChannelsWrapper>
        <CurrentChannel channel={currentChannel}/>
        <ServerUsers />
        </>
    )
}


export default CurrentServer


const ChannelsWrapper = styled.div`
display: flex;
flex-direction: column;
width: 25%;
`
