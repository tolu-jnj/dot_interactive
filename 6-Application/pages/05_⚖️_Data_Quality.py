"""
Data Quality Standards and Risk Metrics
"""
import streamlit as st

st.set_page_config(page_title="Data Quality", page_icon="⚖️", layout="wide")

st.title("⚖️ Data Quality Standards & Risk Metrics")

st.markdown("""
Data quality isn't just about accuracy. It's about fitness for purpose and understanding 
what can go wrong when data quality fails.
""")

# Data Quality Dimensions
st.markdown("## 📊 Six Dimensions of Data Quality")

dimensions = [
    {
        "name": "Accuracy",
        "definition": "Data correctly represents what it measures",
        "gene_therapy": "Viral titer measurement matches reference standard (95-105% recovery)",
        "failure_impact": "Batch released with insufficient potency"
    },
    {
        "name": "Completeness",
        "definition": "All required data is captured, nothing missing",
        "gene_therapy": "All 15 required QC tests completed before batch release decision",
        "failure_impact": "Release decision made without critical information"
    },
    {
        "name": "Consistency",
        "definition": "Data matches across systems and time periods",
        "gene_therapy": "Batch yield = 95% in LIMS, ERP, and historical trending system",
        "failure_impact": "Different teams make decisions based on different 'truths'"
    },
    {
        "name": "Timeliness",
        "definition": "Data available when needed for decision-making",
        "gene_therapy": "QC results available within 2 hours of test completion",
        "failure_impact": "Delayed release decisions, inventory buildup"
    },
    {
        "name": "Validity",
        "definition": "Data conforms to required format and rules",
        "gene_therapy": "Batch ID follows format: [FACILITY]-[YEAR]-[SEQUENCE] (e.g., BR-2024-0127)",
        "failure_impact": "System errors, failed validations, regulatory non-compliance"
    },
    {
        "name": "Integrity",
        "definition": "Data relationships and lineage are preserved",
        "gene_therapy": "Can trace each vial back to source batch and forward to patient outcome",
        "failure_impact": "Product traceability broken in case of adverse event"
    }
]

for dim in dimensions:
    with st.expander(f"✓ {dim['name']}"):
        st.markdown(f"**Definition:** {dim['definition']}")
        st.markdown(f"**Gene Therapy Example:** {dim['gene_therapy']}")
        st.markdown(f"**Failure Impact:** 🚨 {dim['failure_impact']}")

st.markdown("---")

# Data Quality Risk Metrics
st.markdown("## ⚠️ Critical Data Quality Risks (Interview Gold)")

risks = [
    {
        "name": "Counter-Serendipity",
        "definition": "Loss of unexpected discoveries due to over-automation/measurement bias",
        "example": "Algorithm removes 'outliers' automatically, missing one that indicated new failure mode",
        "pharmaceutical_impact": "Safety signal missed because it didn't fit expected pattern",
        "mitigation": "Human review of exceptions; seed unexpected patterns into algorithm training"
    },
    {
        "name": "Perverse Feedback",
        "definition": "System optimizes for measured metric at expense of unmeasured value",
        "example": "Optimize for 'batch cycle time' but don't measure 'quality consistency' → faster but riskier",
        "pharmaceutical_impact": "Speed up manufacturing but increase defect rate (hidden until release)",
        "mitigation": "Balanced scorecard; measure trade-offs explicitly"
    },
    {
        "name": "Hyper-Focus",
        "definition": "Optimizing measured metrics while missing critical unmeasured factors",
        "example": "Maximize cell density but don't measure secretion efficiency of those cells",
        "pharmaceutical_impact": "High titer but low potency = failed batches despite 'good' numbers",
        "mitigation": "Regular review of unmeasured factors; cross-functional input on KPIs"
    },
    {
        "name": "Skill Erosion",
        "definition": "Loss of human expertise when process becomes fully automated",
        "example": "Manufacturing team loses ability to troubleshoot problems when system breaks down",
        "pharmaceutical_impact": "Extended downtime when software fails; no one understands manual process",
        "mitigation": "Maintain manual competency; regular training on underlying principles"
    },
    {
        "name": "Privacy Paradox",
        "definition": "More data sharing creates privacy risks beyond benefit",
        "example": "Share detailed patient outcome data to improve manufacturing without patient consent",
        "pharmaceutical_impact": "GDPR violations; regulatory warning; patient harm",
        "mitigation": "Data minimization; explicit governance on data usage; consent tracking"
    }
]

for i, risk in enumerate(risks, 1):
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown(f"### {i}. {risk['name']}")
        st.markdown(f"*{risk['definition']}*")
    
    with col2:
        with st.expander("Show Details"):
            st.markdown(f"**Example:** {risk['example']}")
            st.markdown(f"**Pharma Impact:** 🚨 {risk['pharmaceutical_impact']}")
            st.markdown(f"**Mitigation:** ✓ {risk['mitigation']}")

st.markdown("---")

# Measurement Framework
st.markdown("## 📈 How to Measure Data Quality")

st.info("""
**Practical Approach:**

1. **Accuracy Metrics**
   - % of records passing validation rules
   - Duplicate rate (same data entered twice)
   
2. **Completeness Metrics**
   - % of required fields populated
   - % of expected records received

3. **Timeliness Metrics**
   - Time from event to data capture
   - Time from data capture to availability

4. **Consistency Metrics**
   - Reconciliation variance between systems
   - Drift in definitions over time

5. **Impact Metrics**
   - # of decisions affected by poor data
   - Cost of correcting data issues
   - Delayed processes due to data gaps
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("quality")
    st.success("Section marked as completed!")
    st.balloons()
