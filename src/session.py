import streamlit as st
import time
from .config import DEFAULT_MODEL


def init_session_state():
    """初始化会话状态"""
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    if 'ollama_model' not in st.session_state:
        st.session_state['ollama_model'] = False
    if 'Model_error' not in st.session_state:
        st.session_state['Model_error'] = None
    if 'client' not in st.session_state:
        st.session_state['client'] = None
    if 'select_model' not in st.session_state:
        st.session_state['select_model'] = DEFAULT_MODEL
    if 'model_cache' not in st.session_state:
        st.session_state['model_cache'] = None
    if 'cache_time' not in st.session_state:
        st.session_state['cache_time'] = None
    if 'last_refresh_time' not in st.session_state:
        st.session_state['last_refresh_time'] = time.time()


def get_session_state():
    """获取会话状态"""
    return st.session_state


def update_session_state(key, value):
    """更新会话状态"""
    st.session_state[key] = value


def reset_model_state():
    """重置模型状态"""
    st.session_state['ollama_model'] = False
    st.session_state['Model_error'] = None
    st.session_state['client'] = None


def reset_cache():
    """重置缓存"""
    if 'model_cache' in st.session_state:
        del st.session_state['model_cache']
    if 'cache_time' in st.session_state:
        del st.session_state['cache_time']
