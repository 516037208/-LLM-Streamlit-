# Streamlit 智能聊天助手

一个基于 Streamlit 和 Ollama 的智能聊天应用，支持多种模型选择、思考过程显示和实时模型管理。

## 功能特性

- 🤖 **多种模型支持**：支持 DeepSeek R1 系列模型（8B/14B/32B/64B）
- 💭 **思考过程显示**：展示模型的思考过程，增加对话透明度
- 🔄 **自动模型管理**：每5分钟自动刷新模型列表
- 📦 **模型管理工具**：提供模型选择、状态显示和手动刷新功能
- 💾 **聊天记录管理**：支持清除聊天记录，保持界面整洁
- 🔒 **安全的错误处理**：优雅处理各种异常情况，确保应用稳定运行

## 技术栈

- **前端框架**：Streamlit
- **后端服务**：Ollama（本地 LLM 服务）
- **开发语言**：Python 3.8+

## 安装步骤

### 1. 安装依赖

```bash
# 克隆项目后，进入项目目录
cd streamlit_chat_assistant

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 Ollama

确保您已安装并启动 Ollama 服务：

1. 下载并安装 Ollama：[Ollama 官网](https://ollama.com/download)
2. 启动 Ollama 服务
3. 拉取模型（例如）：
   ```bash
   ollama pull deepseek-r1:8b
   ```

### 3. 运行应用

```bash
# 运行 Streamlit 应用
streamlit run streamlit_app.py
```

## 使用方法

### 基本使用

1. 在浏览器中打开应用（默认地址：`http://localhost:8501`）
2. 在底部输入框中输入消息，按 Enter 发送
3. 查看模型的回复和思考过程

### 模型管理

- **选择模型**：在左侧"模型管理工具"中选择不同的模型
- **清除聊天记录**：点击"清除聊天记录"按钮
- **重新加载模型**：当模型出现问题时，点击"重新加载"按钮
- **刷新模型列表**：当 Ollama 服务器上的模型发生变化时，点击"刷新模型列表"按钮

## 项目结构

```
streamlit_chat_assistant/
├── README.md              # 项目说明
├── requirements.txt       # 依赖项
├── .gitignore             # Git 忽略文件
├── streamlit_app.py       # 主应用入口
├── src/                   # 源代码
│   ├── __init__.py
│   ├── config.py          # 配置管理
│   ├── session.py         # 会话状态管理
│   ├── models.py          # 模型管理
│   ├── messages.py        # 消息管理
│   └── ui.py              # 界面组件
├── tests/                 # 测试文件
│   └── test_utils.py
├── docs/                  # 文档
│   └── usage.md
└── examples/              # 示例
    └── demo.py
```

## 配置说明

### 模型配置

在 `src/config.py` 中可以配置默认模型和可用模型列表：

```python
DEFAULT_MODEL = 'deepseek-r1:8b'
AVAILABLE_MODELS = [
    'deepseek-r1:8b',
    'deepseek-r1:14b',
    'deepseek-r1:32b',
    'deepseek-r1:64b'
]
```

### Ollama 服务器配置

默认连接到本地 Ollama 服务器 `http://localhost:11434`。如果您的 Ollama 服务在不同地址运行，请修改 `src/config.py` 中的 `OLLAMA_HOST` 配置。

## 故障排除

### 常见问题

1. **模型加载失败**
   - 检查 Ollama 服务是否正在运行
   - 确认模型已正确拉取
   - 检查网络连接

2. **响应缓慢**
   - 需要有合适的显卡与足够显存
   - 可以尝试使用更小的模型（如 8B 版本）
   - 确保您的计算机有足够的内存和 CPU 资源

3. **无法连接到 Ollama**
   - 检查 Ollama 服务状态
   - 确认端口 11434 是否可访问

### 查看日志

应用运行时的日志会显示在终端中，包含详细的错误信息和操作记录。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 许可证

MIT License
