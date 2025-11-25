"""
Lean Manufacturing Integration with Data Operating Theory
"""
import streamlit as st

st.set_page_config(page_title="Lean Integration", page_icon="🔗", layout="wide")

st.title("🔗 Lean Manufacturing Integration")

st.markdown("""
Lean manufacturing identifies 8 types of waste. Understanding how data operating theory 
addresses each waste is critical for demonstrating business impact.
""")

# Lean Waste Mapping
wastes = [
    {
        "number": 1,
        "name": "Defects",
        "definition": "Poor quality products requiring rework or scrap",
        "data_problem": "Lack of real-time quality data preventing early detection",
        "data_solution": "Event capture of QC failures + State capture of process parameters → correlate root causes",
        "gene_therapy": "Early detection of viral titer failures through real-time monitoring",
        "kpi": "% of batches caught in process vs. at release"
    },
    {
        "number": 2,
        "name": "Overproduction",
        "definition": "Making more than customer needs or can absorb",
        "data_problem": "Collecting data without clear business purpose",
        "data_solution": "Define analytical asks first → collect only necessary data (Reusable principle)",
        "gene_therapy": "Not collecting every possible parameter; focus on 'golden parameters' with proven impact",
        "kpi": "Data points collected per batch vs. business questions answered"
    },
    {
        "number": 3,
        "name": "Waiting",
        "definition": "Idle time while waiting for information or people",
        "data_problem": "Data not accessible when needed; stored in wrong systems",
        "data_solution": "Accessible principle - data at point of decision without motion waste",
        "gene_therapy": "QA doesn't wait 2 days for batch reports; data available in real-time dashboard",
        "kpi": "Time from batch completion to release decision (should be hours, not days)"
    },
    {
        "number": 4,
        "name": "Motion",
        "definition": "Unnecessary movement by people or equipment",
        "data_problem": "Analysts spend time searching multiple systems for one data element",
        "data_solution": "Interoperable systems + Structure capture showing data lineage",
        "gene_therapy": "Single sign-on to all systems; batch history accessible from one screen",
        "kpi": "% of analyst time spent on data gathering vs. analysis"
    },
    {
        "number": 5,
        "name": "Transportation",
        "definition": "Unnecessary movement of materials or data",
        "data_problem": "Manual data entry, copying between systems, no integration",
        "data_solution": "Automated data flows + Governed principle (clear ownership prevents duplication)",
        "gene_therapy": "MES → QMS → Analytics pipeline automated; eliminate manual entry",
        "kpi": "% data entered manually vs. automated"
    },
    {
        "number": 6,
        "name": "Extra Processing",
        "definition": "Work that doesn't add customer value",
        "data_problem": "Creating multiple versions of 'truth'; inconsistent definitions",
        "data_solution": "Consistent principle - single source of truth with standard definitions",
        "gene_therapy": "Viral titer measured once (vg/mL) and used by all teams, not recalculated differently by each group",
        "kpi": "Number of different 'batch status' definitions across organization"
    },
    {
        "number": 7,
        "name": "Inventory",
        "definition": "Excess stock waiting to be used",
        "data_problem": "Accumulating data 'just in case' without business model",
        "data_solution": "Available + Reusable principles - data accessible when needed, collected with intent",
        "gene_therapy": "Real-time trending analysis replaces months of historical data archiving",
        "kpi": "Data storage costs vs. business questions answered from archived data"
    },
    {
        "number": 8,
        "name": "Talent",
        "definition": "Underutilizing people's skills and creativity",
        "data_problem": "Analysts stuck preparing data instead of solving problems",
        "data_solution": "Scalable architecture + Automated data pipelines = time for strategic work",
        "gene_therapy": "Data engineers build pipeline; analysts focus on forecasting and optimization",
        "kpi": "% of senior analyst time spent on strategic vs. operational tasks"
    }
]

# Display each waste
for waste in wastes:
    st.markdown(f"""
    ### {waste['number']}. {waste['name']}
    
    **Lean Definition:** {waste['definition']}
    
    **Data Problem:** {waste['data_problem']}
    
    **Data Solution:** {waste['data_solution']}
    
    **Gene Therapy Example:** {waste['gene_therapy']}
    
    **Measurable KPI:** {waste['kpi']}
    """)
    
    st.divider()

st.markdown("---")

st.markdown("## 💡 The Connection Pattern")

st.success("""
**Template for explaining Lean + Data Operating Theory:**

*"[Lean Waste] occurs when [data problem]. We address this through [data solution] which implements 
the [principle] of data operating theory. Specifically, we measure [KPI] to track impact."*

**Example:**
*"Waiting waste occurs when QA staff can't access batch data quickly. We address this through an 
accessible data architecture which implements the Accessible principle. Specifically, we measure 
'time from batch completion to release decision' - our target is 4 hours vs. current 2 days."*
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("lean")
    st.success("Section marked as completed!")
    st.balloons()
