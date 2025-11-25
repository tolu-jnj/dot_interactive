"""
Data Operating Theory Practice Interview Questions
"""
import streamlit as st

st.set_page_config(page_title="Interview Practice", page_icon="💼", layout="wide")

st.title("💼 Practice Interview Questions")

st.markdown("""
These are real questions you might encounter in technical discussions about data 
operating theory. Practice your answers!
""")

questions = [
    {
        "q": "Walk me through how you'd design a data system for a gene therapy manufacturing batch release process.",
        "context": "This tests your ability to apply all frameworks together",
        "structure": [
            "Start with conceptual: What's the goal? (Fast decisions, quality assurance, compliance)",
            "Then business: What data is needed? (Process params, QC results, equipment status)",
            "Then technical: What architecture? (Event capture from MES, state snapshots for current status, structure for traceability)",
            "Finish with impact: How do we measure success? (Decision time, accuracy, audit efficiency)"
        ],
        "red_flags": [
            "❌ Starting with technology (\"We'll use Kafka...\")",
            "❌ Not mentioning governance",
            "❌ Ignoring quality/compliance requirements",
            "❌ No mention of traceability"
        ]
    },
    {
        "q": "How would you explain the difference between 'Data Informed' and 'Data Driven' to a manufacturing executive?",
        "context": "Tests understanding of maturity models and business context",
        "structure": [
            "Explain maturity levels simply",
            "Give pharmaceutical context",
            "Explain why 'Data Informed' is usually better for gene therapy",
            "Discuss trade-offs"
        ],
        "red_flags": [
            "❌ Saying 'Data Driven is better'",
            "❌ Not understanding regulatory/safety context",
            "❌ Technical answer instead of business answer",
            "❌ Not mentioning human judgment/accountability"
        ]
    },
    {
        "q": "We collect 150 process parameters from our bioreactors but analysts only use 8 of them. How would you address this?",
        "context": "Tests understanding of lean waste and ROI",
        "structure": [
            "Identify the problem: Overproduction waste",
            "Ask clarifying questions: Why collect 150? Which 8 matter? Why not the others?",
            "Propose solution: Define analytical asks first, then collect data",
            "Calculate impact: Reduce data pipeline complexity, improve analyst productivity, lower storage costs"
        ],
        "red_flags": [
            "❌ 'Delete the extra parameters' (might lose important data)",
            "❌ No business context",
            "❌ 'Just build a better analytics tool'",
            "❌ Missing the lean principle"
        ]
    },
    {
        "q": "How would you connect a batch manufacturing issue to lean waste to data requirements?",
        "context": "Tests integration of lean + data + business",
        "structure": [
            "Pick a real problem: 'Batches wait 3 days for QC results'",
            "Map to lean: This is 'Waiting' waste",
            "Map to data: Problem is data not Accessible at point of decision",
            "Propose data solution: Real-time dashboard, automated result upload",
            "Calculate business impact: Reduce working capital, improve inventory turns"
        ],
        "red_flags": [
            "❌ Only technical solution",
            "❌ Doesn't mention business impact",
            "❌ Ignores governance/process",
            "❌ No metrics"
        ]
    },
    {
        "q": "How do you handle data quality risk when you don't know what you don't measure?",
        "context": "Tests understanding of Counter-Serendipity and measurement bias",
        "structure": [
            "Name the risk: Counter-Serendipity / Hyper-Focus",
            "Give example: Automating viability measurement but missing potency",
            "Propose mitigation: Human review of exceptions, cross-functional input on KPIs",
            "Mention governance: Regular review of unmeasured factors"
        ],
        "red_flags": [
            "❌ 'We just measure everything'",
            "❌ Not acknowledging the risk",
            "❌ Pure technical answer (automation)",
            "❌ Missing human element"
        ]
    },
    {
        "q": "Your company spent $2M on a data warehouse no one used. Why did it fail and how would you prevent it?",
        "context": "Tests understanding of Three Levels of Design alignment",
        "structure": [
            "Root cause: Likely misalignment - started with technology, not strategy",
            "Explain Three Levels: Conceptual → Business → Technical",
            "Propose different approach: Align on business outcomes first",
            "Give example: What problem are we solving? Who needs what data? What ROI?"
        ],
        "red_flags": [
            "❌ 'We needed better marketing'",
            "❌ Pure technical answer",
            "❌ Blaming the tools",
            "❌ Missing the alignment concept"
        ]
    }
]

for i, q in enumerate(questions, 1):
    with st.expander(f"**Question {i}:** {q['q'][:60]}..."):
        st.markdown(f"**Full Question:** {q['q']}")
        st.markdown(f"**Context:** {q['context']}")
        
        st.markdown("### 💭 How to Structure Your Answer")
        for step in q['structure']:
            st.markdown(f"- {step}")
        
        st.markdown("### ❌ Red Flags to Avoid")
        for flag in q['red_flags']:
            st.markdown(f"{flag}")
        
        st.markdown("---")

st.markdown("---")

st.markdown("## 🎤 Delivery Tips")

st.info("""
1. **Pause and clarify first**
   - "Let me make sure I understand... You're asking about [X]?"
   - This shows thoughtfulness and prevents rambling

2. **Lead with business, support with technology**
   - Start: "The main goal is..."
   - Then: "To achieve that, we need..."
   - Finally: "Technically, we'd implement..."

3. **Use the STAR method**
   - **Situation:** "We had batches waiting 3 days for QC"
   - **Task:** "I needed to reduce decision time"
   - **Action:** "We implemented real-time dashboard for test results"
   - **Result:** "Decision time reduced to 8 hours; $500K inventory freed"

4. **Show you understand constraints**
   - Manufacturing: "Within regulatory requirements..."
   - Budget: "With limited IT resources..."
   - Data: "Without perfect historical data..."

5. **End with a question**
   - "Does this align with your environment?"
   - "Are you more concerned with speed or accuracy?"
   - This shows you're problem-solving, not just reciting
""")

st.markdown("---")

st.markdown("## 📝 Practice Format")

st.success("""
Use this format to practice:

1. **Read the question** (2 minutes)
2. **Pause and clarify** (30 seconds)
3. **Answer out loud** (3-4 minutes) - pretend someone's listening
4. **Review your response** - did you hit the key structure points?
5. **Adjust and repeat** until it feels natural

**Pro Tip:** Record yourself! Hearing how you sound is invaluable. 
You'll notice:
- Do you ramble?
- Do you use filler words ("um", "like")?
- Do you lead with business or technology?
- Are you confident?
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("interview")
    st.success("Section marked as completed!")
    st.balloons()
