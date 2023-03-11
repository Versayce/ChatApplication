import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux"
import { Wrapper } from './DithcordStyles';
import Servers from './Servers/Servers'
import CurrentServer from './Servers/CurrentServer'
import { getAllServersByUserId } from '../../store/server';
import UsersList from '../UsersList';


function Dithcord() {
    const dispatch = useDispatch();
    const [ toggleChat, setToggleChat ] = useState(false)

    const currentUser = useSelector(state => state.session.user);
    const currentServerObj = useSelector(state => state.servers.oneServer);
    const currentServer = Object.values(currentServerObj)

    const userServersObj = useSelector(state => state.servers.allServers);
    const userServers = Object.values(userServersObj)

    console.log('', '\n', '--------------MAIN COMPONENT DATA--------------', '\n', toggleChat, '\n', '');

    useEffect(() => {
        // dispatch(getServers())
        dispatch(getAllServersByUserId(currentUser.id))
    }, [dispatch, currentServer.id, currentUser.id]);

    return(
        <Wrapper>
            <Servers user={currentUser} servers={userServers} setToggleChat={setToggleChat} />
            <CurrentServer server={currentServer} toggleChat={toggleChat} />
            <UsersList />
        </Wrapper>
    )

}


export default Dithcord
