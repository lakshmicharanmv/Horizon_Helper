import streamlit as st
from src.orchestrator import handle_user_query

# Page config with purple and blue luxury styling
st.set_page_config(
    page_title="Horizon Helper - Luxury Travel", 
    page_icon="H",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Purple and blue luxury sidebar with same background as main
with st.sidebar:
    st.markdown("""
    <style>
    .sidebar-premium {
        background: linear-gradient(135deg, 
            rgba(139, 92, 246, 0.9) 0%, 
            rgba(99, 102, 241, 0.85) 30%, 
            rgba(59, 130, 246, 0.8) 70%,
            rgba(6, 182, 212, 0.7) 100%);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 20px 40px rgba(79, 70, 229, 0.2);
        position: relative;
        overflow: hidden;
        animation: gradientShift 8s ease infinite;
        background-size: 400% 400%;
    }
    
    .sidebar-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, 
            #8b5cf6, #6366f1, #3b82f6, #06b6d4);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-premium">', unsafe_allow_html=True)
    st.markdown("""
    <h1 style='
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-align: center;
        animation: textGlow 3s ease-in-out infinite;
    '>Horizon Helper</h1>
    """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style='
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(224, 231, 255, 0.1) 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #e0e7ff;
            margin-bottom: 1rem;
        '>
            <h3 style='color: #0f172a; margin-top: 0; font-size: 1.1rem; font-weight: 700;'>Luxury Travel Assistant</h3>
            <p style='color: #1e293b; margin: 0.5rem 0; font-size: 0.95rem; font-weight: 500;'>Your premium companion for extraordinary journeys</p>
        </div>
        
        <div style='
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(224, 231, 255, 0.08) 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
        '>
            <h4 style='color: #0f172a; font-size: 1rem; margin-top: 0; font-weight: 700;'>Premium Features</h4>
            <div style='display: flex; flex-direction: column; gap: 0.8rem;'>
                <div style='padding: 0.8rem; background: rgba(255, 255, 255, 0.15); border-radius: 8px; border-left: 3px solid #ffffff;'>
                    <span style='color: #0f172a; font-weight: 700;'>Real-time Insights</span>
                    <p style='color: #334155; font-size: 0.85rem; margin: 0.3rem 0 0 0; font-weight: 500;'>Live weather & destination data</p>
                </div>
                <div style='padding: 0.8rem; background: rgba(255, 255, 255, 0.15); border-radius: 8px; border-left: 3px solid #e0e7ff;'>
                    <span style='color: #0f172a; font-weight: 700;'>Luxury Destination Guides</span>
                    <p style='color: #334155; font-size: 0.85rem; margin: 0.3rem 0 0 0; font-weight: 500;'>Curated premium locations</p>
                </div>
                <div style='padding: 0.8rem; background: rgba(255, 255, 255, 0.15); border-radius: 8px; border-left: 3px solid #c7d2fe;'>
                    <span style='color: #0f172a; font-weight: 700;'>Premium Travel Planning</span>
                    <p style='color: #334155; font-size: 0.85rem; margin: 0.3rem 0 0 0; font-weight: 500;'>Personalized itineraries</p>
                </div>
                <div style='padding: 0.8rem; background: rgba(255, 255, 255, 0.15); border-radius: 8px; border-left: 3px solid #a5b4fc;'>
                    <span style='color: #0f172a; font-weight: 700;'>Exclusive Recommendations</span>
                    <p style='color: #334155; font-size: 0.85rem; margin: 0.3rem 0 0 0; font-weight: 500;'>VIP experiences & deals</p>
                </div>
            </div>
        </div>
        
        <div style='
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(224, 231, 255, 0.1) 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.25);
        '>
            <h4 style='color: #0f172a; font-size: 1rem; margin-top: 0; font-weight: 700;'>Quick Examples</h4>
            <div style='display: flex; flex-direction: column; gap: 0.7rem;'>
                <div style='
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(224, 231, 255, 0.2) 100%);
                    color: #0f172a;
                    padding: 0.8rem;
                    border-radius: 8px;
                    font-weight: 700;
                    font-size: 0.9rem;
                    text-align: left;
                    cursor: pointer;
                    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
                    transition: all 0.3s ease;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                '>
                    Luxury stays in Dubai with weather
                </div>
                <div style='
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(224, 231, 255, 0.2) 100%);
                    color: #0f172a;
                    padding: 0.8rem;
                    border-radius: 8px;
                    font-weight: 700;
                    font-size: 0.9rem;
                    text-align: left;
                    cursor: pointer;
                    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
                    transition: all 0.3s ease;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                '>
                    Golden triangle tour India
                </div>
                <div style='
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(224, 231, 255, 0.2) 100%);
                    color: #0f172a;
                    padding: 0.8rem;
                    border-radius: 8px;
                    font-weight: 700;
                    font-size: 0.9rem;
                    text-align: left;
                    cursor: pointer;
                    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
                    transition: all 0.3s ease;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                '>
                    Premium experiences in Paris
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Purple and blue luxury hero section
st.markdown(
    """
    <div style='
        background: linear-gradient(135deg, 
            rgba(139, 92, 246, 0.9) 0%, 
            rgba(99, 102, 241, 0.85) 30%, 
            rgba(59, 130, 246, 0.8) 70%,
            rgba(6, 182, 212, 0.7) 100%);
        border-radius: 24px;
        padding: 4rem 3rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 30px 60px rgba(79, 70, 229, 0.3);
        border: 2px solid rgba(139, 92, 246, 0.3);
        animation: gradientShift 8s ease infinite;
        background-size: 400% 400%;
    '>
        <div style='text-align: center; position: relative; z-index: 2;'>
            <h1 style='
                background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem;
                font-weight: 900;
                margin-bottom: 0.5rem;
                letter-spacing: -1px;
                text-shadow: 0 8px 16px rgba(79, 70, 229, 0.3);
                animation: textGlow 3s ease-in-out infinite;
            '>Horizon Helper</h1>
            <p style='
                color: #e0e7ff;
                font-size: 1.3rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                text-shadow: 0 2px 4px rgba(79, 70, 229, 0.5);
                animation: fadeInOut 4s ease-in-out infinite;
            '>Experience Travel in Premium Luxury</p>
            <div style='
                height: 4px;
                background: linear-gradient(90deg, 
                    transparent 0%, 
                    #e0e7ff 20%, 
                    #8b5cf6 50%, 
                    #3b82f6 80%, 
                    transparent 100%);
                border-radius: 4px;
                margin: 2rem auto;
                width: 60%;
                box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
                animation: pulse 2s ease-in-out infinite;
            '></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Purple and blue luxury CSS with animations and darker text
st.markdown("""
<style>
:root {
    --purple-primary: linear-gradient(135deg, #8b5cf6 0%, #6366f1 50%, #3b82f6 100%);
    --purple-secondary: linear-gradient(135deg, #c7d2fe 0%, #e0e7ff 50%, #dbeafe 100%);
    --purple-dark: linear-gradient(135deg, #4c1d95 0%, #3730a3 50%, #1e40af 100%);
    --purple-light: linear-gradient(135deg, #fafafa 0%, #f8fafc 50%, #f1f5f9 100%);
    --glass-bg: rgba(139, 92, 246, 0.1);
    --glass-border: rgba(99, 102, 241, 0.3);
    --shadow-purple: 0 20px 40px rgba(79, 70, 229, 0.2);
    --shadow-glow: 0 0 30px rgba(139, 92, 246, 0.4);
    --border-radius-premium: 20px;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes textGlow {
    0%, 100% { text-shadow: 0 8px 16px rgba(79, 70, 229, 0.3); }
    50% { text-shadow: 0 8px 25px rgba(139, 92, 246, 0.6); }
}

@keyframes fadeInOut {
    0%, 100% { opacity: 0.9; }
    50% { opacity: 1; }
}

@keyframes pulse {
    0%, 100% { transform: scaleX(1); }
    50% { transform: scaleX(1.05); }
}

@keyframes containerSlide {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.chat-bubble {
    padding: 1.4rem 2rem;
    border-radius: 20px;
    font-size: 1.05rem;
    max-width: 70%;
    word-break: break-word;
    margin-bottom: 1.2rem;
    display: inline-block;
    animation: slideInBubble 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    line-height: 1.6;
    backdrop-filter: blur(10px);
    border: 2px solid var(--glass-border);
    box-shadow: var(--shadow-purple);
    position: relative;
    overflow: hidden;
    font-weight: 600;
}

.chat-bubble::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--purple-primary);
    animation: borderGlow 2s ease-in-out infinite;
}

@keyframes borderGlow {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
}

@keyframes slideInBubble {
    from {
        opacity: 0;
        transform: translateY(25px) scale(0.95);
        filter: blur(5px);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

@keyframes bubbleGlow {
    0%, 100% { 
        box-shadow: var(--shadow-purple);
    }
    50% { 
        box-shadow: var(--shadow-purple), 0 0 25px rgba(139, 92, 246, 0.4);
    }
}

.chat-bubble.user {
    background: var(--purple-dark);
    color: #f8fafc !important;
    margin-left: auto;
    margin-right: 0;
    text-align: right;
    float: right;
    clear: both;
    animation: bubbleGlow 4s ease-in-out infinite;
    border: 2px solid #8b5cf6;
}

.chat-bubble.assistant {
    background: var(--purple-secondary);
    color: #0f172a !important;
    margin-right: auto;
    margin-left: 0;
    text-align: left;
    float: left;
    clear: both;
    border: 2px solid #6366f1;
    font-weight: 600;
}

/* Purple and blue input styling */
.stTextInput>div>div {
    background: var(--purple-light) !important;
    border-radius: 16px !important;
    border: 2px solid #8b5cf6 !important;
    box-shadow: var(--shadow-purple) !important;
    animation: inputFocus 3s ease-in-out infinite;
}

@keyframes inputFocus {
    0%, 100% { border-color: #8b5cf6; }
    50% { border-color: #3b82f6; }
}

.stTextInput>div>div>input {
    border: none !important;
    border-radius: 14px !important;
    padding: 1.2rem 1.5rem !important;
    font-size: 1.05rem !important;
    background: transparent !important;
    font-weight: 600;
    color: #0f172a !important;
    transition: all 0.3s ease !important;
}

.stTextInput>div>div>input:focus {
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3) !important;
    border: none !important;
    transform: translateY(-2px);
}

.stTextInput>div>div>input::placeholder {
    color: #475569 !important;
    font-weight: 500;
}

/* Sidebar styling to match main background */
.stSidebar {
    background: linear-gradient(135deg, 
        rgba(139, 92, 246, 0.9) 0%, 
        rgba(99, 102, 241, 0.85) 30%, 
        rgba(59, 130, 246, 0.8) 70%,
        rgba(6, 182, 212, 0.7) 100%) !important;
    animation: gradientShift 8s ease infinite !important;
    background-size: 400% 400% !important;
}

/* Purple scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(139, 92, 246, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: var(--purple-primary);
    border-radius: 10px;
    animation: scrollbarGlow 2s ease-in-out infinite;
}

@keyframes scrollbarGlow {
    0%, 100% { background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%); }
    50% { background: linear-gradient(135deg, #6366f1 0%, #3b82f6 100%); }
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
}

/* Floating animations */
@keyframes floatPurple {
    0%, 100% { 
        transform: translateY(0px) rotate(0deg);
        filter: drop-shadow(0 5px 15px rgba(139, 92, 246, 0.4));
    }
    33% { 
        transform: translateY(-12px) rotate(5deg);
        filter: drop-shadow(0 10px 25px rgba(99, 102, 241, 0.6));
    }
    66% { 
        transform: translateY(-6px) rotate(-3deg);
        filter: drop-shadow(0 8px 20px rgba(59, 130, 246, 0.5));
    }
}

.floating-purple {
    animation: floatPurple 6s ease-in-out infinite;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .chat-bubble {
        max-width: 85%;
        padding: 1.2rem 1.5rem;
    }
    
    .chat-container {
        padding: 1.5rem;
        max-height: 50vh;
    }
}

/* Make all text darker for better readability */
body {
    color: #0f172a !important;
    font-weight: 500;
}

.stMarkdown {
    color: #0f172a !important;
    font-weight: 500;
}

.stMarkdown p {
    color: #0f172a !important;
    font-weight: 500;
}

.stMarkdown li {
    color: #0f172a !important;
    font-weight: 500;
}

.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color: #0f172a !important;
    font-weight: 700;
}

/* Ensure all text in the app has good contrast */
[data-testid="stMarkdownContainer"] {
    color: #0f172a !important;
}

.st-bq {
    color: #0f172a !important;
}

.st-emotion-cache-1q7spjk {
    color: #0f172a !important;
}

/* Chat container specific styling */
.chat-container {
    color: #0f172a !important;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Display chat history with purple and blue chat bubbles
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    sender_class = "user" if sender == "user" else "assistant"
    if sender_class == "assistant":
        st.markdown(f'<div class="chat-bubble {sender_class}">', unsafe_allow_html=True)
        st.markdown(message, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="chat-bubble {sender_class}">{message}</div>',
            unsafe_allow_html=True,
        )
st.markdown('</div>', unsafe_allow_html=True)

# Purple and blue chat input
def submit():
    user_input = st.session_state.user_input
    if user_input.strip():
        st.session_state.chat_history.append(("user", user_input))
        response = handle_user_query(user_input)
        st.session_state.chat_history.append(("assistant", response))
        st.session_state.user_input = ""  # Clear input

st.text_input(
    "Type your message...",
    key="user_input",
    on_change=submit,
    placeholder="Ask about luxury destinations, premium experiences, or travel planning...",
    help="Press Enter to send - Experience luxury travel planning"
)