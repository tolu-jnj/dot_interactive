"""
8 Core Principles of Data Operating Theory
"""
import streamlit as st
from utils.data_loader import load_principles

st.set_page_config(page_title="8 Principles", page_icon="📋", layout="wide")

st.title("📋 The 8 Core Principles of Data Operating Theory")

st.markdown("""
These principles form the foundation of effective data operations, applicable across 
any industry including gene therapy manufacturing. Each principle connects to lean 
manufacturing concepts.
""")

principles = load_principles()

for i, principle in enumerate(principles['principles'], 1):
    with st.expander(f"{principle['icon']} {i}. {principle['name']}", expanded=(i==1)):
        st.markdown(f"**Definition:** {principle['definition']}")
        st.markdown(f"**Lean Connection:** {principle['lean_connection']}")
        
        st.markdown("**Gene Therapy Example:**")
        st.info(principle['example'])
        
        if i == 1:
            st.success("💡 **Interview Tip:** Don't confuse Available with Accessible. Available = data exists; Accessible = users can get it easily.")

st.markdown("---")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("principles")
    st.success("Section marked as completed!")
    st.balloons()
