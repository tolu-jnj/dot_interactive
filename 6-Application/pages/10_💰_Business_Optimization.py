"""
Data-Driven Business Optimization Examples
"""
import streamlit as st

st.set_page_config(page_title="Business Optimization", page_icon="💰", layout="wide")

st.title("💰 Data-Driven Business Optimization")

st.markdown("""
Understanding how data operating theory translates to business results is critical
for demonstrating value in technical discussions.
""")

st.markdown("## 📈 Revenue, Expense, Quality, and Speed Trade-offs")

optimizations = [
    {
        "metric": "Batch Cycle Time",
        "improvement": "Reduce from 30 days → 21 days (-30%)",
        "primary_impact": "Expenses ↓",
        "secondary": "Quality (maintain), Revenue ↑ (more batches/year)",
        "data_strategy": "Real-time monitoring → reduce waiting waste",
        "example": "QC results in 2 hours instead of 8 hours; reduces 'on-hold' batches"
    },
    {
        "metric": "Batch Failure Rate",
        "improvement": "Reduce from 15% → 8% (-47%)",
        "primary_impact": "Expenses ↓",
        "secondary": "Quality ↑, Revenue ↑ (less waste)",
        "data_strategy": "Early detection through trending → prevent failures before release",
        "example": "Temperature deviation alert triggers review before irreversible damage"
    },
    {
        "metric": "First-Pass Yield",
        "improvement": "Increase from 70% → 85% (+21%)",
        "primary_impact": "Expenses ↓, Revenue ↑",
        "secondary": "Quality ↑",
        "data_strategy": "Root cause analysis of rejections → design changes",
        "example": "Analysis shows 60% of failures in purification step → equipment upgrade ROI calculated"
    },
    {
        "metric": "Product Release Decision Time",
        "improvement": "Reduce from 5 days → 1 day (-80%)",
        "primary_impact": "Revenue ↑",
        "secondary": "Expenses ↓ (working capital), Quality (maintain)",
        "data_strategy": "Accessible architecture → data available at point of decision",
        "example": "QA dashboards show all tests complete; no waiting for batches of reports"
    },
    {
        "metric": "Manufacturing Planning Accuracy",
        "improvement": "Reduce forecast error from ±25% → ±8%",
        "primary_impact": "Expenses ↓",
        "secondary": "Revenue ↑ (better inventory), Quality (stable production)",
        "data_strategy": "Predictive analytics from historical data + demand signals",
        "example": "Demand forecast + current pipeline = accurate staffing plan"
    },
    {
        "metric": "Regulatory Compliance Time",
        "improvement": "Reduce audit response from 3 weeks → 3 days (-85%)",
        "primary_impact": "Expenses ↓",
        "secondary": "Quality ↑ (better traceability)",
        "data_strategy": "Governed data + Structure capture → automated traceability",
        "example": "Audit: 'show me all batches from equipment X'; automated report in minutes"
    }
]

for opt in optimizations:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"### {opt['metric']}")
        st.markdown(f"**Target:** {opt['improvement']}")
        
    with col2:
        with st.expander("Show Details"):
            st.markdown(f"**Primary Impact:** {opt['primary_impact']}")
            st.markdown(f"**Secondary Impact:** {opt['secondary']}")
            st.markdown(f"**Data Strategy:** {opt['data_strategy']}")
            st.markdown(f"**Example:** {opt['example']}")
    
    st.divider()

st.markdown("---")

st.markdown("## 💼 ROI Framework")

st.info("""
**When presenting a data project, calculate:**

1. **Current State Metrics**
   - Cycle time: 30 days
   - Failure rate: 15%
   - Decision time: 5 days

2. **Data Project Investment**
   - Technology: $150K (systems, tools)
   - People: $200K (annual analysts, engineers)
   - Training: $50K
   - Total Year 1: $400K

3. **Projected Benefits**
   - Cycle time reduction → produces 3 extra batches/year → $500K revenue
   - Failure rate reduction → saves 2 batches/year from loss → $800K savings
   - Decision time → inventory reduction → $300K working capital freed
   - Labor efficiency → 1 FTE saved → $100K savings
   - Total Year 1: $1.7M

4. **ROI Calculation**
   - Net benefit: $1.7M - $400K = $1.3M
   - ROI: 325%
   - Payback: 2.8 months

**This is how you position data projects as business investments, not IT expenses.**
""")

st.markdown("---")

st.markdown("## 🎯 Interview Talking Points")

st.success("""
1. **"I focus on business outcomes, not technical elegance"**
   - Not: "We'll build a real-time data lake"
   - Yes: "This will reduce batch cycle time by 5 days, producing 3 extra batches/year worth $500K"

2. **"I measure what matters"**
   - Not: "System uptime is 99.9%"
   - Yes: "Decision time improved from 5 days to 1 day; audits now take 3 days instead of 3 weeks"

3. **"I understand trade-offs"**
   - Not: "We built everything they asked for"
   - Yes: "We focused on the 20% of data that drives 80% of decisions; this lets us move fast while meeting standards"

4. **"I connect strategy to execution"**
   - Not: "We built a dashboard"
   - Yes: "We aligned strategy (reduce cycle time), standards (2-hour QC turnaround), and technology (real-time dashboard) to achieve business goals"
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("optimization")
    st.success("Section marked as completed!")
    st.balloons()
