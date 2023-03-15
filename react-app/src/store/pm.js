const LOAD_ALL_CHATS = 'chats/getAllChats';
const LOAD_CHAT = 'chats/loadChat';
const ADD_CHAT = 'chats/addChat';
const DELETE_CHAT = 'chats/deleteChat';
const CLEAR_ONE_CHATS = 'chats/clearChats';
const CLEAR_ALL_CHATS = 'chats/clearAllChats';

//------------------------------   ACTIONS   ------------------------------//

export const loadAllChats = (chats) => {
    return {
        type: LOAD_ALL_CHATS,
        chats,
    };
};

export const loadChat = (chat) => {
    return {
        type: LOAD_CHAT,
        chat,
    };
};

export const addChat = (chat) => {
    return {
        type: ADD_CHAT,
        chat,
    };
};

export const deleteChat = (chatId) => {
    return {
        type: DELETE_CHAT,
        chatId,
    };
};

export const clearOneChats = () => {
    return {
        type: CLEAR_ONE_CHATS,
    }
}

export const clearAllChats = () => {
    return {
        type: CLEAR_ALL_CHATS,
    }
}

//------------------------------   THUNKS   ------------------------------//

export const getAllChatsByUserId = (userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/chats`);
    if (res.ok) {
        const data = await res.json();
        dispatch(loadAllChats(data));
    };
};

export const getChat = (chatId) => async (dispatch) => {
    const res = await fetch(`/api/chats/${chatId}`);

    if (res.ok) {
        const data = await res.json();
        dispatch(loadChat(data));
        return data;
    };
};

export const newChat = (chat) => async (dispatch) => {
    // console.log("in new chat thunk", chat)
    const { user1Id, user2Id, name } = chat
    const res = await fetch('/api/chats/new', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(chat),
    });
    if (res.ok) {
        const data = await res.json();
        const { id } = data
        const chat = {
            id,
            user1Id,
            user2Id,
        }
        dispatch(joinChat(chat))
        dispatch(addChat(data));
        return data;
    };
};

//TODO finish creating join chat thunk: 
export const joinChat = (chat) => async (dispatch) => {
    console.log("=== === User Joining Chatroom === ===", chat)
    const res = await fetch(`/api/users/${chat.user1Id}/chats/${chat.id}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(chat),
    });
    if(res.ok) {
        const data = await res.json();
        return data;
    }
}

export const destroyChat = (chatId, userId) => async dispatch => {
    const res = await fetch(`/api/chats/${chatId}`, {
        method: 'DELETE',
    });
    if (res.ok) {
        dispatch(deleteChat(chatId));
        dispatch(getAllChatsByUserId(userId)); 
        return { 'message' : 'Successfully Deleted' };
    };
};

//------------------------------   REDUCER   ------------------------------//

const initialState = { allChats: {}, oneChat: {} };
const chatReducer = (state = initialState, action) => {
    switch (action.type) {

        case LOAD_ALL_CHATS:
            {
                const newState = { allChats: {}, oneChat: {} };
                console.log('chat reducer::::::', action.chats)
                action.chats.chats.forEach(chat => {
                    newState.allChats[chat.id] = chat
                });
                return newState;
            }

        case LOAD_CHAT:
            {
                const newState = { allChats: {...state.allChats}, oneChat: {...state.oneChat} };
                newState.oneChat = action.chat;
                return newState;   
            }
            
        case ADD_CHAT:
            {
                const newState = { allChats: {...state.allChats}, oneChat: {...state.oneChat} };    
                newState.allChats[action.chat.id] = action.chat;
                newState.oneChat[action.chat.id] = action.chat;
                return newState;            
            }
            
        case DELETE_CHAT:
            {
                const newState = { allChats: {...state.allChats}, oneChat: {...state.oneChat} }; 
                delete newState.oneChat[action.chatId]
                delete newState.allChats[action.chatId]
                return newState
            }
            
        case CLEAR_ONE_CHATS:
            {
                const newState = { allChats: {...state.allChats}, oneChat: {}}
                return newState
            }
                
        case CLEAR_ALL_CHATS:
            {
                const newState = { allChats: {}, oneChat: {}}
                return newState
            }
            
        default:
            return state;
    }
}

export default chatReducer;
