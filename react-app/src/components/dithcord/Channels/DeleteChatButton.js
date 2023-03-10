import { useDispatch, useSelector } from "react-redux"

import { clearMessages } from "../../../store/message";
import { clearOneChats, destroyChat } from "../../../store/pm";
import { ChannelButtons } from "../DithcordStyles";

const DeleteChatButton = ({ chatId }) => {
    const dispatch = useDispatch();
    const currentServerObj = useSelector(state => state.servers.oneServer);
    const currentServer = Object.values(currentServerObj)
    const currentUser = useSelector(state => state.session.user);
    const currentChat = useSelector(state => state.pmchatrooms.oneChat);

    // console.log('INSIDE DELETE CHAt BUTTON -----------------------------------------------', currentServer)

    const deleteChatButton = async (e) => {
        e.preventDefault();
        dispatch(clearMessages())
        dispatch(clearOneChats())
        dispatch(destroyChat(chatId));
    };

    return (
        <ChannelButtons as="button" onClick={deleteChatButton}>
            Del
        </ChannelButtons>    
    );
};


export default DeleteChatButton;
