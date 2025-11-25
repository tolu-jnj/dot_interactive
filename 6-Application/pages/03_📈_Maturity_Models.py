"""
Data Maturity Models
"""
import streamlit as st

st.set_page_config(page_title="Maturity Models", page_icon="📈", layout="wide")

st.title("📈 Data Maturity Models")

st.markdown("""
The 4-level maturity model shows progression in how an organization uses data for decision-making.
In pharma/gene therapy, the right level depends on the decision type.
""")

tab1, tab2, tab3, tab4 = st.tabs(["Data Aware", "Data Informed", "Data Driven", "Comparison"])

with tab1:
    st.markdown("### 1️⃣ Data Aware")
    st.markdown("""
    **Definition:** Leadership understands data exists and its potential value.
    
    **Decision Process:**
    - Decisions based primarily on domain expertise and experience
    - Data recognized but not systematically used
    - No established analytics capability
    
    **Gene Therapy Example:**
    - QA Manager knows historical batch failures exist but relies on memory and anecdotes
    - No formal system to query patterns
    
    **Strengths:**
    - Fast decisions
    - Uses expert judgment
    
    **Weaknesses:**
    - Misses patterns visible in data
    - Scalability issues as operations grow
    - High reliance on key individuals
    
    **When Appropriate:**
    - Early-stage operations
    - Well-understood, stable processes
    """)

with tab2:
    st.markdown("### 2️⃣ Data Informed")
    st.markdown("""
    **Definition:** Multiple data sources inform decisions alongside expert judgment.
    
    **Decision Process:**
    - Data and analytics support decision-making
    - Domain experts still provide critical context
    - Some governance around data access
    - Analytics capability developing
    
    **Gene Therapy Example:**
    - Batch release decision integrates:
      - Historical data on similar lots
      - Current QC test results
      - Equipment performance metrics
      - Expert assessment of risk
    
    **Strengths:**
    - Balances data with expert judgment
    - Handles uncertainty well
    - Appropriate for regulated industries
    
    **Weaknesses:**
    - Slower decisions (need consensus)
    - Still subject to confirmation bias
    
    **When Appropriate:**
    - Regulated environments (pharma, gene therapy)
    - High-stakes decisions requiring human oversight
    - Complex manufacturing with many variables
    """)

with tab3:
    st.markdown("### 3️⃣ Data Driven")
    st.markdown("""
    **Definition:** Data and algorithms are the primary basis for decisions.
    
    **Decision Process:**
    - Automated decision systems with human oversight
    - Algorithms define thresholds and actions
    - Expert judgment applies only to exceptions
    - Enterprise analytics infrastructure
    
    **Gene Therapy Example:**
    - Automated alert: "Bioreactor temperature deviation detected"
    - System recommends: "Hold step, investigate cooling system"
    - Operator approves action based on data recommendation
    
    **Strengths:**
    - Consistency and scalability
    - Captures complex relationships
    - Speed and automation
    
    **Weaknesses:**
    - Requires extensive historical data
    - Risk of algorithm bias
    - May miss novel situations
    - Regulatory concerns in pharma
    
    **When Appropriate:**
    - Stable, well-understood processes
    - Sufficient historical data available
    - Lower safety/regulatory risk
    """)

with tab4:
    st.markdown("### 🔄 Comparison Matrix")
    
    comparison_data = {
        "Dimension": ["Decision Speed", "Scalability", "Regulatory Fit", "Data Requirement", "Expert Judgment", "Cost", "Risk of Errors"],
        "Data Aware": ["Fast", "Low", "High", "Low", "High", "Low", "High"],
        "Data Informed": ["Medium", "Medium", "High", "Medium", "High", "Medium", "Medium"],
        "Data Driven": ["Fast", "High", "Medium", "High", "Low", "High", "Medium"]
    }
    
    import pandas as pd
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("""
    ### Key Insight for Gene Therapy
    
    **Most pharma operations should target "Data Informed" maturity** because:
    1. Regulatory environment values human judgment and documented reasoning
    2. Safety-critical decisions benefit from expert review
    3. Rare/novel situations require domain expertise
    4. Audit trails must show human accountability
    
    **Data Driven is reserved for:**
    - Process monitoring and alerts (where human response is expected)
    - Resource optimization (where risk is contained)
    - Trend analysis and reporting (informing human decisions)
    """)

st.markdown("---")

st.warning("""
⚠️ **Critical Interview Point:** Being "Data Driven" is NOT always better than being "Data Informed."
In regulated industries, premature automation can create compliance risks and hide decision rationale.
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("maturity")
    st.success("Section marked as completed!")
    st.balloons()
