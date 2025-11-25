"""
User Impact Alignment - Three Levels of Design
"""
import streamlit as st

st.set_page_config(page_title="User Impact", page_icon="🎯", layout="wide")

st.title("🎯 User Impact Alignment: Three Levels of Design")

st.markdown("""
Business transformation requires alignment between strategy, standards, and execution.
The Three Levels of Design framework connects them.
""")

# Three Levels
st.markdown("## 📊 The Three Levels")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Level 1️⃣: Conceptual
    
    **What:** Strategic vision & objectives
    
    **Who:** Executives, business leaders
    
    **Questions:**
    - What are we trying to achieve?
    - How does data support strategy?
    
    **Gene Therapy Example:**
    "Reduce batch cycle time by 40% while maintaining quality"
    
    **Outputs:**
    - Strategic goals
    - Success metrics
    - Investment justification
    """)

with col2:
    st.markdown("""
    ### Level 2️⃣: Business
    
    **What:** Standards, KPIs, processes
    
    **Who:** Operations, compliance, data teams
    
    **Questions:**
    - What processes need to change?
    - What data do we need?
    - What are acceptable standards?
    
    **Gene Therapy Example:**
    "QC results in dashboard within 2 hours of test completion; trending shows 3-sigma limits"
    
    **Outputs:**
    - Data standards
    - KPIs & targets
    - Process workflows
    - Governance rules
    """)

with col3:
    st.markdown("""
    ### Level 3️⃣: Technical
    
    **What:** Systems, tools, architecture
    
    **Who:** Engineers, architects, developers
    
    **Questions:**
    - What systems enable this?
    - How do we build/integrate?
    - What technology stack?
    
    **Gene Therapy Example:**
    "LIMS → Kafka queue → Analytics engine → Tableau dashboard"
    
    **Outputs:**
    - System architecture
    - Data pipelines
    - Tool selection
    - Infrastructure requirements
    """)

st.markdown("---")

st.markdown("## 🔗 How They Connect")

st.success("""
**Strategy → Standards → Technology (Top-Down)**

Executives decide: "Reduce cycle time 40%"
↓
Operations teams define: "QC data available in 2 hours" and "Setup time ≤30 min"
↓
Technical teams build: LIMS integration and automated dashboard

**Technology Enables → Standards Are Met → Strategy Achieved (Bottom-Up)**

If technology fails → cannot meet standards → strategy cannot be achieved
If standards unclear → technology over/under-builds → strategy wastes money
If strategy not clear → teams build the wrong things
""")

st.markdown("---")

st.markdown("## ⚠️ Common Misalignments (Interview Gold)")

misalignments = [
    {
        "problem": "Clear Strategy, Poor Standards",
        "example": "Exec: 'We need real-time data visibility' but Operations doesn't define what 'real-time' means or which data matters",
        "result": "Technical team builds everything; 90% unused",
        "fix": "Standards must specify: Which 5 data points? 2-minute latency? Which users?"
    },
    {
        "problem": "Clear Standards, Wrong Technology",
        "example": "Operations: 'Need data in 2 hours' but Technology chooses batch ETL that takes 6 hours",
        "result": "SLA missed; standards cannot be met",
        "fix": "Technology review must confirm timing before implementation"
    },
    {
        "problem": "Great Technology, No Business Case",
        "example": "Technical team builds beautiful real-time system but Operations never uses it",
        "result": "Money spent; value not achieved; strategy unchanged",
        "fix": "Start with strategy & business case; build only what's needed"
    },
    {
        "problem": "All Three Misaligned",
        "example": "Exec wants faster decisions; Operations doesn't measure decision time; Technology builds analytics no one uses",
        "result": "Project fails",
        "fix": "Monthly alignment reviews: Is strategy clear? Are standards measurable? Does technology enable them?"
    }
]

for i, mal in enumerate(misalignments, 1):
    with st.expander(f"{i}. {mal['problem']}"):
        st.markdown(f"**Example:** {mal['example']}")
        st.markdown(f"**Result:** 🚨 {mal['result']}")
        st.markdown(f"**Fix:** ✓ {mal['fix']}")

st.markdown("---")

st.markdown("## 💡 Interview Strategy")

st.warning("""
**When asked "How would you design a data system for [X]?" answer in 3 levels:**

1. **Conceptual:** "First, I'd understand the business objective. Is it reducing cycle time? Improving quality? Compliance? This determines everything downstream."

2. **Business:** "Then I'd work with operations to define standards. What specific metrics? What data is needed? What's an acceptable performance threshold?"

3. **Technical:** "Finally, I'd recommend technology. Based on the standards, here's what infrastructure makes sense..."

**This shows you think like a leader, not just a technician.**
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("user_impact")
    st.success("Section marked as completed!")
    st.balloons()
