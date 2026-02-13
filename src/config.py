# 项目配置

# 默认模型
DEFAULT_MODEL = 'deepseek-r1:8b'

# 可用模型列表
AVAILABLE_MODELS = [
    'deepseek-r1:8b',
    'deepseek-r1:14b',
    'deepseek-r1:32b',
    'deepseek-r1:64b'
]

# Ollama 服务器地址
OLLAMA_HOST = 'http://localhost:11434'

# 缓存配置
CACHE_DURATION = 300  # 缓存有效期（秒），默认5分钟

# 应用配置
APP_TITLE = "智能聊天助手"
APP_ICON = "💬"
APP_LAYOUT = "wide"
