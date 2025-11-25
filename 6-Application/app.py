"""
Data Operating Theory Mastery Tool
Main Streamlit Application
"""
import streamlit as st
import json
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Data Operating Theory Mastery",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #2176AE 0%, #118AB2 100%);
    padding: 2rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}
.info-box {
    background: rgba(17, 138, 178, 0.1);
    border-left: 4px solid #118AB2;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
}
.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📊 Data Operating Theory Mastery Platform</h1>
        <p>Interactive Learning Tool for Lean Manufacturing in Gene Therapy Operations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = None
    
    # Sidebar
    st.sidebar.title("📈 Your Progress")
    progress = len(st.session_state.completed_sections) / 11 if st.session_state.completed_sections else 0
    st.sidebar.progress(progress)
    st.sidebar.caption(f"{len(st.session_state.completed_sections)}/11 sections completed")
    
    if st.session_state.quiz_score is not None:
        st.sidebar.metric("Quiz Score", f"{st.session_state.quiz_score}/10")
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Navigation:** Use the pages in the sidebar to explore:
    - 8 Core Principles
    - Data Architecture
    - Maturity Models
    - Lean Integration
    - And more!
    """)
    
    # Main content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📚 11 Modules</h3>
            <p>Comprehensive coverage of data operating theory</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>✅ 10 Quiz Questions</h3>
            <p>Test your understanding with immediate feedback</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>💼 Practice Questions</h3>
            <p>Prepare for technical interviews</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Welcome content
    st.markdown("## 🎯 Welcome to Your Learning Journey")
    
    tab1, tab2, tab3 = st.tabs(["Getting Started", "Learning Approach", "Tool Purpose"])
    
    with tab1:
        st.markdown("""
        ### What You'll Master
        
        This interactive platform helps you demonstrate expert-level understanding of:
        
        - **8 Core Principles** of Data Operating Theory with gene therapy examples
        - **Data Architecture** patterns (State, Event, Atomic, Structure capture)
        - **Maturity Models** (Data Aware, Data Informed, Data Driven)
        - **23 Knowledge Areas** from DAMA framework
        - **Lean Manufacturing Integration** with data operating principles
        - **Data Quality Standards** and risk assessment metrics
        - **User Impact Alignment** from strategy to execution
        """)
    
    with tab2:
        st.markdown("""
        ### Interactive Learning Approach
        
        - **Self-paced modules** with real-world examples
        - **Interactive quizzes** with immediate feedback
        - **Practice interview questions** with sample answers
        - **Progress tracking** across all sections
        - **Domain-specific scenarios** for gene therapy operations
        - **Lean manufacturing connections** throughout
        """)
    
    with tab3:
        st.markdown("""
        ### Why This Tool Exists
        
        **The Problem:** As a lean practitioner in gene therapy operations, I struggled to:
        - Continuously apply data operating theory principles in daily work
        - Map lean wastes to business optimizations
        - Navigate ad-hoc data requests without clear analytical asks
        - Prepare for technical discussions (1 hour searching transcripts/slides)
        
        **The Solution:** This "pocket guide" tool that:
        - Reduces prep time from 1 hour to <10 minutes (85% efficiency gain)
        - Provides quick reference during real-time discussions
        - Establishes baseline metrics for continuous improvement
        - Shifts team mindset to understand "why" before requesting work
        
        **The Impact:** Measurable business value through structured problem-solving
        and behavioral change in cross-functional teams.
        """)
    
    st.markdown("---")
    st.info("🚀 **Get Started:** Select a topic from the sidebar to begin learning!")

if __name__ == "__main__":
    main()
