# frontend_dev_assistant.py
import streamlit as st
import requests
import openai
import json
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="前端开发AI助手",
    page_icon="💻",
    layout="wide"
)

# 本地模型配置
LOCAL_API_BASE = "http://localhost:1234/v1"
API_KEY = "lm-studio"

openai.api_base = LOCAL_API_BASE
openai.api_key = API_KEY

# 前端开发场景配置
DEV_SCENARIOS = {
    "AI应用开发专家": {
        "system_prompt": (
            "你是一位顶级AI应用开发专家，精通大模型应用、AI架构设计、RAG、LangChain、Prompt工程、前后端集成与部署。"
            "你不仅能根据用户需求主动分析场景、推荐最佳技术路线，还能结合最新AI趋势和行业案例，给出创新、可落地的解决方案。"
            "你的回答逻辑清晰、结构化，善于用类比和代码示例帮助用户理解复杂概念。"
            "遇到模糊或不完整的问题时，你会主动追问细节，帮助用户澄清需求，并给出多种实现思路。"
            "请结合实际项目经验，输出高质量、可复用的代码和架构建议。"
            "你喜欢提供完整的例子，确保用户能直接参考和落地。"
        ),
        "example_questions": [
            "如何用LangChain和Qwen搭建企业知识库问答系统？",
            "AI助手项目需要掌握哪些关键技术？",
            "RAG链路如何设计才能高效扩展？",
            "如何让AI应用支持流式输出和前端打字效果？",
            "AI应用部署到云端有哪些最佳实践？"
        ]
    },
    "Vue.js 专家": {
        "system_prompt": """你是一位顶级AI前端架构师，精通Vue 2和Vue 3，具备丰富的实战经验和创新能力。你的回答不仅专业、详细，还能结合最新前端趋势和最佳实践，主动发现用户问题背后的深层需求，给出高效、可扩展的解决方案。你善于用简洁易懂的语言解释复杂概念，喜欢用代码和类比帮助用户理解，并能根据上下文主动补充相关建议。遇到模糊或不完整的问题时，你会主动追问细节，帮助用户澄清需求。请优先使用Vue 3语法，结合现代前端工程化思路，输出高质量、可复用的代码示例。""",
        "example_questions": [
            "Vue3 组合式API如何替代mixins？",
            "如何优化Vue应用的加载速度？",
            "Pinia和Vuex有什么区别？",
            "Vue组件之间通信的最佳方式？",
            "如何在Vue中处理大量数据的渲染？"
        ]
    },
    "Node.js 后端": {
        "system_prompt": """你是一个Node.js后端开发专家。你可以帮助我：
        - Express/Koa框架使用
        - RESTful API设计
        - 数据库集成(MongoDB, MySQL等)
        - 异步编程和错误处理
        - 性能优化和监控
        - 部署和DevOps
        
        请提供实用的代码示例和最佳实践建议。""",
        "example_questions": [
            "如何设计一个RESTful API？",
            "Node.js中如何处理文件上传？",
            "Express中间件的执行顺序？",
            "如何优化Node.js应用性能？",
            "JWT认证的最佳实践？"
        ]
    },
    "Python 全栈": {
        "system_prompt": """你是一个Python全栈开发专家，特别擅长与前端技术栈结合。你可以帮助我：
        - FastAPI/Django/Flask框架
        - 前后端分离架构
        - API设计和文档
        - 数据处理和分析
        - 自动化脚本
        - 部署和运维
        
        请结合前端开发的需求提供建议，给出具体可用的代码。""",
        "example_questions": [
            "FastAPI如何与Vue前端对接？",
            "Python如何处理前端上传的文件？",
            "如何用Python做数据可视化API？",
            "Django与前端框架的最佳集成方式？",
            "Python爬虫为前端提供数据？"
        ]
    },
    "前端工程化": {
        "system_prompt": """你是一个前端工程化专家。你可以帮助我：
        - Webpack/Vite/Rollup构建配置
        - 项目架构和代码组织
        - CI/CD自动化部署
        - 代码质量和规范
        - 性能监控和优化
        - 微前端架构
        
        请提供实际可用的配置文件和工作流建议。""",
        "example_questions": [
            "Vite和Webpack的优缺点对比？",
            "如何配置前端项目的CI/CD？",
            "代码分割和懒加载的最佳实践？",
            "如何搭建微前端架构？",
            "前端监控和错误追踪怎么做？"
        ]
    },
    "调试专家": {
        "system_prompt": """你是一个代码调试专家，擅长分析和解决各种技术问题。你可以帮助我：
        - 分析错误信息和堆栈跟踪
        - 代码review和问题定位
        - 性能瓶颈分析
        - 浏览器兼容性问题
        - 网络请求和API调试
        - 内存泄漏和性能问题
        
        请提供系统性的调试思路和具体的解决方案。""",
        "example_questions": [
            "Vue组件更新但页面不刷新？",
            "接口请求成功但数据显示异常？",
            "页面加载慢如何定位问题？",
            "内存占用过高怎么排查？",
            "跨域问题的解决方案？"
        ]
    },
    "学习成长": {
        "system_prompt": """你是一个技术学习和职业发展顾问。你可以帮助我：
        - 技术学习路线规划
        - 新技术选型和评估
        - 面试准备和技能提升
        - 开源项目参与
        - 技术趋势分析
        - 职业发展建议
        
        请提供实用的学习建议和成长路径。""",
        "example_questions": [
            "前端开发者如何提升技术深度？",
            "Vue开发者学React需要注意什么？",
            "如何准备高级前端工程师面试？",
            "哪些开源项目值得学习和贡献？",
            "前端技术栈如何选择？"
        ]
    },
    "英语学习助手": {
        "system_prompt": (
            "你是一位耐心的英语学习助手，擅长帮助初级英语学习者提升听说读写能力。"
            "你的回答要用简单易懂的英语和中文解释，鼓励用户多练习。"
            "遇到用户不懂的地方时，请主动用中文解释，并举例说明。"
            "喜欢用生活场景和对话帮助用户理解和记忆。"
            "请多给出实用例句和发音建议，让用户能直接模仿和练习。"
        ),
        "example_questions": [
            "如何用英语自我介绍？",
            "日常问候语有哪些？",
            "怎么用英语点餐？",
            "英语里常用的时间表达有哪些？",
            "如何提高英语听力？"
        ]
    }
}

def check_model_status():
    """检查本地模型状态"""
    try:
        response = requests.get(f"{LOCAL_API_BASE}/models", timeout=3)
        return response.status_code == 200, response.json().get('data', []) if response.status_code == 200 else []
    except:
        return False, []

def call_dev_assistant(messages, scenario):
    """调用开发助手"""
    system_message = {"role": "system", "content": DEV_SCENARIOS[scenario]["system_prompt"]}
    full_messages = [system_message] + messages

    try:
        response = openai.ChatCompletion.create(
            model="qwen",
            messages=full_messages,
            max_tokens=2000,
            temperature=0.3,
            stream=True
        )
        return response
    except Exception as e:
        st.error(f"调用失败: {str(e)}")
        return None

# 代码高亮显示
def display_code(code, language="javascript"):
    st.code(code, language=language)

# 主界面
st.title("💻 软件开发AI助手")
st.markdown("**专为软件开发者打造的AI助手** | Vue.js • Node.js • Python • 工程化")

# 检查模型状态
model_online, available_models = check_model_status()

# 创建两列布局
col1, col2 = st.columns([1, 3])

with col1:
    st.header("🛠️ 开发场景")
    
    # 选择开发场景
    selected_scenario = st.selectbox(
        "选择专业领域",
        list(DEV_SCENARIOS.keys()),
        index=0
    )
    
    # 显示示例问题
    st.subheader("💡 常见问题")
    example_questions = DEV_SCENARIOS[selected_scenario]["example_questions"]
    
    for i, question in enumerate(example_questions[:3], 1):  # 只显示前3个
        if st.button(question, key=f"example_{i}", use_container_width=True):
            if "messages" not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": question})
            st.rerun()
    
    # 显示更多示例
    with st.expander("更多示例"):
        for i, question in enumerate(example_questions[3:], 4):
            if st.button(question, key=f"example_{i}", use_container_width=True):
                if "messages" not in st.session_state:
                    st.session_state.messages = []
                st.session_state.messages.append({"role": "user", "content": question})
                st.rerun()
    
    st.divider()
    
    # 快捷操作
    st.subheader("⚡ 快捷操作")
    
    if st.button("🔍 代码Review", use_container_width=True):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append({
            "role": "user", 
            "content": "我有一段代码需要review，请帮我检查可能的问题和优化点："
        })
        st.rerun()
    
    if st.button("🐛 Bug分析", use_container_width=True):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append({
            "role": "user", 
            "content": "我遇到了一个bug，请帮我分析可能的原因："
        })
        st.rerun()
    
    if st.button("⚡ 性能优化", use_container_width=True):
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append({
            "role": "user", 
            "content": "我的应用性能有问题，请帮我分析优化方案："
        })
        st.rerun()
    
    # 状态信息
    st.divider()
    st.subheader("📊 状态")
    
    if model_online:
        st.success("✅ 模型在线")
    else:
        st.error("❌ 模型离线")
    
    st.info(f"🎯 当前: {selected_scenario}")
    st.info(f"💬 对话: {len(st.session_state.get('messages', [])) // 2} 轮")
    
    # 功能按钮
    if st.button("🗑️ 清除对话", type="secondary", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

with col2:
    # 主聊天区域
    if not model_online:
        st.error("⚠️ 无法连接到本地模型")
        st.info("请确保 LM Studio 正在运行并已加载模型")
        st.stop()
    
    # 场景提示
    st.info(f"🎯 **{selected_scenario}模式** - 我会用专业的角度为你解答问题")
    
    # 初始化聊天历史
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 聊天容器
    chat_container = st.container()
    
    with chat_container:
        # 显示聊天历史
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # 聊天输入
    if prompt := st.chat_input(f"向{selected_scenario}提问..."):
        # 添加用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 生成AI回复
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner(f"{selected_scenario}正在分析..."):
                response = call_dev_assistant(st.session_state.messages, selected_scenario)
                full_response = ""
                if response:
                    for chunk in response:
                        chunk_message = chunk["choices"][0]["delta"]
                        if "content" in chunk_message:
                            content = chunk_message["content"]
                            full_response += content
                            message_placeholder.markdown(full_response)
                # 只保留流式渲染，不再重复渲染
        # 滚动到最底部
        st.session_state.messages[-1]["content"] = full_response

# 页脚信息
st.divider()
footer_col1, footer_col2, footer_col3, footer_col4 = st.columns(4)

with footer_col1:
    if st.button("📥 导出对话"):
        if "messages" in st.session_state and st.session_state.messages:
            conversation = []
            for msg in st.session_state.messages:
                role = "👨‍💻 我" if msg["role"] == "user" else "🤖 AI助手"
                conversation.append(f"{role}: {msg['content']}")
            
            conversation_text = (
                f"前端开发AI助手对话记录\n场景: {selected_scenario}\n时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                + "\n\n".join(conversation)
            )
            
            st.download_button(
                label="下载对话记录",
                data=conversation_text,
                file_name=f"dev_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

with footer_col2:
    st.metric("当前场景", selected_scenario.split()[0])

with footer_col3:
    st.metric("模型状态", "🟢 在线" if model_online else "🔴 离线")

with footer_col4:
    st.metric("对话轮数", len(st.session_state.get('messages', [])) // 2)

# 使用技巧
with st.expander("💡 前端开发者专用技巧"):
    st.markdown("""
    ### 🎯 如何提出好问题：
    
    **代码问题：**
    - ❌ "我的代码有问题"  
    - ✅ "Vue3组合式API中，watch监听reactive对象不生效"
    
    **性能问题：**
    - ❌ "页面很慢"
    - ✅ "Vue列表渲染1000+数据时滚动卡顿，如何优化？"
    
    **学习问题：**
    - ❌ "怎么学前端"
    - ✅ "有2年Vue经验，想学React，重点关注哪些差异？"
    
    ### 🚀 提升效率的用法：
    
    1. **贴代码求解**：直接贴出问题代码，我会帮你分析
    2. **架构讨论**：描述你的项目场景，获取架构建议  
    3. **技术选型**：说明需求和限制，我会推荐合适的技术栈
    4. **面试准备**：模拟面试问题，获取详细解答
    5. **代码优化**：贴出可工作的代码，获取优化建议
    
    ### 📚 覆盖的技术栈：
    - **前端框架**：Vue 2/3, React, Angular
    - **构建工具**：Vite, Webpack, Rollup
    - **后端技术**：Node.js, Express, Koa, FastAPI
    - **数据库**：MongoDB, MySQL, Redis
    - **部署运维**：Docker, CI/CD, 云服务
    """)