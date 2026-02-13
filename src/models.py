import ollama
import time
import streamlit as st
from .config import OLLAMA_HOST, AVAILABLE_MODELS, CACHE_DURATION


def get_ollama_client():
    """获取Ollama客户端实例"""
    if st.session_state['client'] is None:
        st.session_state['client'] = ollama.Client(host=OLLAMA_HOST)
    return st.session_state['client']


def load_model_library():
    """加载可用模型库"""
    client = get_ollama_client()
    try:
        models = client.list()
        return models.get('models', [])
    except Exception as e:
        st.error(f"加载模型库失败: {e}")
        return []


def get_available_models():
    """获取可用模型列表（带缓存）"""
    try:
        # 检查缓存是否存在且有效
        if 'model_cache' in st.session_state and 'cache_time' in st.session_state:
            if st.session_state['cache_time'] is not None:
                cache_age = time.time() - st.session_state['cache_time']
                if cache_age < CACHE_DURATION:
                    return st.session_state['model_cache']

        # 尝试从服务器获取模型
        models = load_model_library()
        if models:
            model_list = [model['model'] for model in models]
            st.session_state['model_cache'] = model_list
            st.session_state['cache_time'] = time.time()
            return model_list

    except Exception as e:
        st.error(f"获取模型列表失败: {e}")

    # 如果获取失败，使用预设模型列表
    st.session_state['model_cache'] = AVAILABLE_MODELS
    st.session_state['cache_time'] = time.time()
    return AVAILABLE_MODELS


def Model_test(model_name):
    """测试模型连接"""
    client = get_ollama_client()
    try:
        response = client.chat(
            model=model_name,
            messages=[{"role": "user", "content": "你好"}]
        )
        return True, response
    except Exception as e:
        return False, str(e)


def refresh_model_list():
    """手动刷新模型列表"""
    if 'model_cache' in st.session_state:
        del st.session_state['model_cache']
    if 'cache_time' in st.session_state:
        del st.session_state['cache_time']


def get_model_response(model_name, prompt):
    """获取模型响应"""
    client = get_ollama_client()
    try:
        response = client.chat(
            model=model_name,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        return response
    except Exception as e:
        raise Exception(f"获取模型响应失败: {e}")
