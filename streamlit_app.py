import streamlit as st
import time
from src.config import APP_TITLE, APP_ICON, APP_LAYOUT
from src.session import init_session_state
from src.ui import render_model_management, render_error_message, render_chat_interface
from src.models import refresh_model_list, get_available_models


def main():
    """主要应用函数加载"""
    # 设置主页面配置参数
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout=APP_LAYOUT
    )
    
    # 初始化会话状态
    init_session_state()

    # 自动刷新模型列表（每5分钟）
    current_time = time.time()
    if current_time - st.session_state['last_refresh_time'] > 300:  # 5分钟 = 300秒
        # 清除缓存
        refresh_model_list()
        # 重新获取模型列表
        get_available_models()
        # 更新最后刷新时间
        st.session_state['last_refresh_time'] = current_time

    # 页面标题
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.write("与AI模型进行对话，支持思考过程显示")
    st.divider()

    # 渲染模型管理工具
    render_model_management()

    # 显示错误信息
    render_error_message()

    # 渲染聊天界面
    render_chat_interface()


if __name__ == "__main__":
    main()
