"""
Data Architecture: 4 Types of Data Capture
"""
import streamlit as st

st.set_page_config(page_title="Data Architecture", page_icon="🏗️", layout="wide")

st.title("🏗️ Data Architecture: Types of Data Capture")

st.markdown("""
Understanding HOW data is captured is critical for designing effective data systems.
There are 4 fundamental types of data capture:
""")

tab1, tab2, tab3, tab4 = st.tabs(["State Capture", "Event Capture", "Atomic Capture", "Structure Capture"])

with tab1:
    st.markdown("### 📸 State Capture")
    st.markdown("""
    **Definition:** Capturing the current status or condition of something at a point in time.
    
    **Example in Gene Therapy:**
    - Cell viability = 85% (state at time of measurement)
    - Bioreactor temperature = 37.0°C (current state)
    - Batch status = "In Progress" (current state)
    
    **Characteristics:**
    - Snapshot in time
    - Overwrites previous values
    - Tells you WHERE things are
    
    **Lean Connection:** Like visual management boards showing current status of work cells
    
    **When to Use:** When you need to know current condition for decision-making.
    """)
    
    st.info("💡 **Interview Tip:** State capture is often combined with event capture to understand both current state and how you got there.")

with tab2:
    st.markdown("### ⏱️ Event Capture")
    st.markdown("""
    **Definition:** Recording that something happened at a specific time.
    
    **Example in Gene Therapy:**
    - Batch started at 2024-11-19 08:00:00
    - Temperature alarm triggered at 10:45:32
    - QC sample collected at 14:30:00
    
    **Characteristics:**
    - Immutable (events don't change)
    - Time-stamped
    - Tells you WHAT happened and WHEN
    
    **Lean Connection:** Andon cord pulls (event) that stop the line - captured for root cause analysis
    
    **When to Use:** When you need to reconstruct history or perform root cause analysis.
    """)

with tab3:
    st.markdown("### 🔬 Atomic Capture")
    st.markdown("""
    **Definition:** Capturing individual, indivisible data points that cannot be broken down.
    
    **Example in Gene Therapy:**
    - Single cell count measurement: 2.5 × 10⁶ cells/mL
    - Individual pH reading: 7.2
    - One temperature reading: 36.8°C
    
    **Characteristics:**
    - Smallest meaningful unit
    - Cannot be subdivided
    - Foundation for aggregation
    
    **Lean Connection:** Single piece flow - process one item at a time for quality.
    
    **When to Use:** When you need granularity for detailed analysis or aggregation.
    """)

with tab4:
    st.markdown("### 🕸️ Structure Capture")
    st.markdown("""
    **Definition:** Capturing relationships and hierarchies between data elements.
    
    **Example in Gene Therapy:**
    - Batch → Lots → Vials (hierarchical structure)
    - Patient → Trial → Site → Batch (relational structure)
    - Process Step → Equipment → Operator (network structure)
    
    **Characteristics:**
    - Defines relationships
    - Creates context
    - Enables navigation and traceability
    
    **Lean Connection:** Value stream mapping showing relationships between process steps
    
    **When to Use:** When you need to understand context, dependencies, or lineage.
    """)

st.markdown("---")

st.markdown("### 🎯 Combining Capture Types")

st.success("""
**Real-World Example: Batch Manufacturing**

A single manufacturing batch uses ALL FOUR capture types:
1. **State:** Current batch status = "In Purification Step"
2. **Event:** Harvest completed at 2024-11-19 10:30:00
3. **Atomic:** Titer = 1.2 × 10¹² vg/mL (individual measurement)
4. **Structure:** Batch BR-2024-1119 → Lot L-001 → 150 vials (hierarchy)

Understanding which type you're capturing helps design better data systems and avoid common mistakes.
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("architecture")
    st.success("Section marked as completed!")
    st.balloons()
