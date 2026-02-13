import pytest
from src.session import init_session_state
from src.models import get_ollama_client
from src.config import DEFAULT_MODEL, AVAILABLE_MODELS


@pytest.fixture
def init_state():
    """初始化会话状态"""
    init_session_state()


def test_init_session_state(init_state):
    """测试会话状态初始化"""
    import streamlit as st
    assert 'messages' in st.session_state
    assert 'ollama_model' in st.session_state
    assert 'Model_error' in st.session_state
    assert 'client' in st.session_state
    assert 'select_model' in st.session_state
    assert st.session_state['select_model'] == DEFAULT_MODEL


def test_model_config():
    """测试模型配置"""
    assert DEFAULT_MODEL in AVAILABLE_MODELS
    assert len(AVAILABLE_MODELS) > 0


def test_get_ollama_client():
    """测试获取Ollama客户端"""
    client = get_ollama_client()
    assert client is not None


if __name__ == "__main__":
    pytest.main([__file__])
