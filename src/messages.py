import streamlit as st


def display_message(message):
    """显示单条消息"""
    if isinstance(message, dict) and 'role' in message and 'content' in message:
        with st.chat_message(message['role']):
            if 'thinking' in message and message['thinking']:
                st.caption(f"思考过程: {message['thinking']}")
                st.divider()
            if isinstance(message['content'], set):
                st.markdown(next(iter(message['content'])))
            else:
                st.markdown(message['content'])


def display_history_message():
    """显示历史消息"""
    try:
        for message in st.session_state['messages']:
            display_message(message)
    except Exception as e:
        st.error(f"显示消息时出错: {e}")


def add_user_message(content):
    """添加用户消息"""
    st.session_state['messages'].append({
        'role': 'user',
        'content': content
    })


def add_assistant_message(content, thinking=''):
    """添加助手消息"""
    message = {
        'role': 'ai',
        'content': content
    }
    if thinking:
        message['thinking'] = thinking
    st.session_state['messages'].append(message)


def clear_messages():
    """清除所有消息"""
    st.session_state['messages'] = []


def get_message_count():
    """获取消息数量"""
    return len(st.session_state['messages'])


def get_last_message():
    """获取最后一条消息"""
    if st.session_state['messages']:
        return st.session_state['messages'][-1]
    return None
