"""
DAMA Knowledge Areas Framework
"""
import streamlit as st

st.set_page_config(page_title="DAMA Framework", page_icon="📚", layout="wide")

st.title("📚 DAMA Knowledge Areas")

st.markdown("""
DAMA (Data Management Association) identifies 11 core knowledge areas for data management.
Understanding how these connect to gene therapy operations strengthens interview positioning.
""")

dama_areas = [
    {
        "number": 1,
        "name": "Data Governance",
        "definition": "Establish controls, policies, and procedures",
        "pharma_example": "RACI for data ownership: Manufacturing owns batch data generation; Quality owns test result criteria"
    },
    {
        "number": 2,
        "name": "Data Architecture",
        "definition": "Design systems and data flows",
        "pharma_example": "Design that captures State (current status), Event (what happened), and Structure (batch → lot → vial)"
    },
    {
        "number": 3,
        "name": "Data Modeling & Design",
        "definition": "Create logical representations of data",
        "pharma_example": "Batch entity with attributes: ID, start_date, status; related to Lots and QC results"
    },
    {
        "number": 4,
        "name": "Database Management",
        "definition": "Build and maintain data repositories",
        "pharma_example": "SQL Server maintaining batch history with indexing for rapid queries"
    },
    {
        "number": 5,
        "name": "Data Security",
        "definition": "Protect data from unauthorized access",
        "pharma_example": "Role-based access: operators see their batch data; QA sees all batch data; executives see KPIs"
    },
    {
        "number": 6,
        "name": "Data Quality Management",
        "definition": "Establish standards and monitor quality",
        "pharma_example": "Monitor: titer accuracy ±10%, completeness of QC data, consistency across systems"
    },
    {
        "number": 7,
        "name": "Master Data Management",
        "definition": "Maintain single source of truth for key entities",
        "pharma_example": "One Equipment master list used across LIMS, ERP, and QMS"
    },
    {
        "number": 8,
        "name": "Reference Data Management",
        "definition": "Control coded values and lookups",
        "pharma_example": "Standard batch statuses: Setup, In Progress, On Hold, Complete, Released, Failed"
    },
    {
        "number": 9,
        "name": "Data Warehousing & Business Intelligence",
        "definition": "Aggregate data for analytics and reporting",
        "pharma_example": "Data mart that trends batch yield, cycle time, and quality metrics over 24 months"
    },
    {
        "number": 10,
        "name": "Data Integration & Interoperability",
        "definition": "Enable systems to exchange data seamlessly",
        "pharma_example": "MES → QMS → ERP automated data flows eliminate manual entry"
    },
    {
        "number": 11,
        "name": "Data Lifecycle Management",
        "definition": "Manage data from creation through archival",
        "pharma_example": "Batch records retained 5 years after last product expiration per regulation"
    }
]

for area in dama_areas:
    with st.expander(f"{area['number']}. {area['name']}"):
        st.markdown(f"**Definition:** {area['definition']}")
        st.markdown(f"**Pharma Example:** {area['pharma_example']}")

st.markdown("---")

st.markdown("## 🔄 DAMA in Gene Therapy Operations")

st.success("""
**When interviewers ask about "data architecture" or "data governance," they often expect 
DAMA framework awareness.**

Example Answer Structure:
*"We approach data management through the DAMA framework. We've established governance 
by defining who owns each data type. We've standardized our architecture to capture State, 
Event, and Structure data. We maintain master data for Equipment and Reference data for 
batch statuses. We monitor quality through 6 key metrics..."*

This demonstrates enterprise-level thinking, not just "build a database."
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("dama")
    st.success("Section marked as completed!")
    st.balloons()
