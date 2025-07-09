import streamlit as st
import time
from Components import PyCodeAgent

st.set_page_config(
    page_title="PyCode Agent",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def initialize_agent():
    return PyCodeAgent()

if 'agent' not in st.session_state:
    st.session_state.agent = initialize_agent()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'processing' not in st.session_state:
    st.session_state.processing = False

if 'current_input' not in st.session_state:
    st.session_state.current_input = ""


def extract_code_from_response(resp):
    """Extract Python code from the agent's response."""
    if not resp:
        return None

    resp = resp.replace("```python", '')
    resp = resp.replace("```", '')

    return resp

    # code_lines = response.split('\n')
    # code_content = []

    # for line in code_lines:
    #     line = line.strip()
    #     # Check if line looks like Python code
    #     if (line.startswith('def ') or
    #             line.startswith('class ') or
    #             line.startswith('import ') or
    #             line.startswith('from ') or
    #             any(keyword in line for keyword in
    #                 ['print(', 'return ', 'if ', 'for ', 'while ', '=', '+=', '-=', '*=', '/=']) or
    #             line.startswith('    ')):  # Indented lines
    #         code_content.append(line)
    #
    # return '\n'.join(code_content) if code_content else None


def display_chat_history():
    """Display the chat history in a formatted way."""
    if not st.session_state.chat_history:
        st.info("🤖 Start a conversation by asking me to write some Python code!")
        return

    st.subheader("💬 Conversation History")

    for i, (user_msg, agent_response) in enumerate(st.session_state.chat_history):
        # User message
        with st.container():
            st.markdown("**👤 You:**")
            st.write(user_msg)

        # Agent response
        with st.container():
            st.markdown("**🤖 Agent:**")

            if agent_response:
                # Try to extract and display code
                extracted_code = extract_code_from_response(agent_response)

                if extracted_code:
                    st.code(extracted_code, language='python')
                else:
                    st.write(agent_response)

        if i < len(st.session_state.chat_history) - 1:
            st.divider()


# Main App Layout
col1, col2 = st.columns([3, 1])

with col1:
    # Header
    st.title("🐍 PyCode Agent")
    st.markdown("Your AI-powered Python coding assistant with persistent memory and code running capability")

    # Chat Interface
    st.header("💬 Chat with the Agent")

    # Display chat history
    display_chat_history()

    # Input form
    with st.form(key='code_request_form', clear_on_submit=True):
        user_input = st.text_area(
            "What would you like me to code for you?",
            height=100,
            placeholder="Example: Write a function to calculate the factorial of a number",
            value=st.session_state.current_input,
            key="user_input_field"
        )

        col_submit, col_clear = st.columns([1, 1])

        with col_submit:
            submit_button = st.form_submit_button(
                "🚀 Generate Code",
                disabled=st.session_state.processing,
                use_container_width=True
            )

        with col_clear:
            clear_history_button = st.form_submit_button(
                "🗑️ Clear History",
                use_container_width=True
            )

    # Handle clear history
    if clear_history_button:
        st.session_state.chat_history = []
        st.session_state.current_input = ""
        st.success("✅ Chat history cleared!")
        st.rerun()

    # Process the request
    if submit_button and user_input.strip():
        st.session_state.processing = True
        st.session_state.current_input = ""  # Clear the input after submission

        # Show processing indicator
        with st.spinner("🤖 Agent is thinking and coding..."):
            try:
                # Generate response using the persistent agent
                response = st.session_state.agent.generate(user_input)

                # Extract the output from the response
                if isinstance(response, dict) and 'output' in response:
                    agent_output = response['output'].strip()
                else:
                    agent_output = str(response).strip()

                # Add to chat history
                st.session_state.chat_history.append((user_input, agent_output))

                # Success message
                st.success("✅ Code generated successfully!")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Please check your API key and network connection.")

        st.session_state.processing = False
        st.rerun()

with col2:
    st.sidebar.header("🔧 Agent Controls")

    st.sidebar.subheader("📊 Statistics")
    total_conversations = len(st.session_state.chat_history)
    memory_size = st.session_state.agent.get_memory_size()

    col_stat1, col_stat2 = st.sidebar.columns(2)
    with col_stat1:
        st.metric("Conversations", total_conversations)
    with col_stat2:
        st.metric("Memory", memory_size)

    status = "🟢 Ready" if not st.session_state.processing else "🟡 Processing"
    st.sidebar.metric("Status", status)

    st.sidebar.subheader("⚙️ Controls")

    if st.sidebar.button("🔄 Reset Agent Memory", use_container_width=True):
        st.session_state.agent.reset_agent()
        st.sidebar.success("✅ Agent memory reset!")
        time.sleep(1)
        st.rerun()

    if st.sidebar.button("🧹 Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.sidebar.success("✅ Chat history cleared!")
        time.sleep(1)
        st.rerun()

    st.sidebar.subheader("ℹ️ Features")
    st.sidebar.info("""
    **🎯 Core Features:**
    - 🐍 Python code generation
    - 🧮 Mathematical calculations
    - 🔄 Code execution and testing
    - 💭 Persistent conversation memory
    - 🎯 Context-aware responses
    - 🔍 Automatic code extraction
    """)

    st.sidebar.subheader("💡 Example Prompts")
    st.sidebar.markdown("Click on any example to use it:")

    example_prompts = [
        "Remove all the columns in sample_dataset.csv file except the Revenue",
        'Write me a python script to find the square root of 32.',
        "Write a function to sort a list of dictionaries by a key",
        "Create a class to manage a simple bank account",
        "Write a function to find the longest common substring",
        "Make a well designed plot of product category and revenue from sample_dataset2.csv and save as test.png file",
    ]

    for i, prompt in enumerate(example_prompts):
        if st.sidebar.button(
                f"📝 {prompt[:35]}{'...' if len(prompt) > 35 else ''}",
                key=f"example_{i}",
                use_container_width=True
        ):
            st.session_state.current_input = prompt
            st.rerun()

    st.sidebar.subheader("💡 Tips")
    st.sidebar.markdown("""
    **For best results:**
    - Be specific about requirements
    - Mention input/output formats
    - Ask for error handling
    - Request test cases
    - Specify performance needs
    """)

st.divider()
st.markdown("🤖 Powered by Google Gemini & LangChain | Built with ❤️ using Streamlit")
st.caption("Agent memory persists across conversations for better context understanding")

with st.expander("🔍 Session Information"):
    st.write(f"**Agent initialized:** ✅")
    st.write(f"**Total conversations:** {len(st.session_state.chat_history)}")
    st.write(f"**Agent memory size:** {st.session_state.agent.get_memory_size()} messages")
    st.write(f"**Processing status:** {'🟡 Processing' if st.session_state.processing else '🟢 Ready'}")

st.caption('Built by Divyansh Vishwkarma')
st.caption('Github   : https://github.com/Divyansh900/PyCodeAgent')
st.caption('LinkedIn : https://www.linkedin.com/in/divyanshvishwkarma')