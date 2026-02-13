import streamlit as st
from .config import DEFAULT_MODEL
from .models import get_available_models, refresh_model_list
from .session import reset_model_state


def render_model_management():
    """渲染模型管理界面"""
    with st.expander("📦 模型管理工具", expanded=True):
        col1, col2 = st.columns([2, 1], gap="small")
        with col1:
            # 模型选择
            available_models = get_available_models()
            if available_models:
                selected_model = st.selectbox(
                    "选择模型",
                    available_models,
                    index=0 if DEFAULT_MODEL not in available_models else available_models.index(DEFAULT_MODEL)
                )
                if selected_model != st.session_state['select_model']:
                    st.session_state['select_model'] = selected_model
                    st.session_state['ollama_model'] = False
                    st.rerun()
            else:
                st.warning("无法获取模型列表，请检查Ollama服务器连接")

        with col2:
            # 模型状态
            st.write(f"当前模型: {st.session_state['select_model']}")
            st.write(f"模型状态: {'已加载' if st.session_state['ollama_model'] else '未加载'}")

        # 操作按钮
        col3, col4, col5 = st.columns(3, gap="small")
        with col3:
            if st.button("🗑️ 清除聊天记录", use_container_width=True):
                from .messages import clear_messages
                clear_messages()
                st.success("聊天记录已清除")
                st.rerun()

        with col4:
            if st.button("🔄 重新加载", use_container_width=True):
                reset_model_state()
                st.success("模型已重置")

        with col5:
            if st.button("🔄 刷新模型列表", use_container_width=True):
                refresh_model_list()
                get_available_models()
                st.success("模型列表已刷新")
                st.rerun()


def render_error_message():
    """渲染错误信息"""
    if st.session_state['Model_error']:
        st.error(f"模型加载失败: {st.session_state['Model_error']}")
        if st.button("重试"):
            st.session_state['Model_error'] = None
            st.rerun()


def render_chat_interface():
    """渲染聊天界面"""
    # 聊天容器
    chat_container = st.container()

    # 显示历史消息
    with chat_container:
        from .messages import display_history_message
        display_history_message()

    # 聊天输入
    if prompt := st.chat_input("请输入消息..."):
        # 显示用户消息
        with st.chat_message('user'):
            st.markdown(prompt)

        # 添加用户消息到会话状态
        from .messages import add_user_message, add_assistant_message
        add_user_message(prompt)

        # 加载模型
        if not st.session_state['ollama_model']:
            with st.spinner("正在加载模型，请稍后...."):
                from .models import Model_test
                success, response = Model_test(st.session_state['select_model'])
                if success:
                    st.session_state['ollama_model'] = True
                    st.session_state['Model_error'] = None
                    st.success("模型加载成功！")
                else:
                    error_message = response
                    st.session_state['Model_error'] = error_message
                    st.error(f"模型加载失败: {error_message}")
                    return

        # 生成回复
        with st.spinner("正在思考..."):
            try:
                from .models import get_model_response
                response = get_model_response(
                    st.session_state['select_model'],
                    prompt
                )

                content = response['message']['content']
                thinking = response['message'].get('thinking', '')

                # 添加助手消息
                add_assistant_message(content, thinking)

                # 显示助手消息
                with st.chat_message('ai'):
                    if thinking:
                        st.caption(f"思考过程: {thinking}")
                        st.divider()
                    st.markdown(content)
                    st.divider()

            except Exception as e:
                # 忽略轻微错误
                if str(e) != "enter":
                    st.error(f"处理回复时出错: {e}")
                    if 'response' in locals():
                        st.write(f"响应结构: {response}")
