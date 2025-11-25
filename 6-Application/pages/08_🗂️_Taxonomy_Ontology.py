"""
Taxonomy and Ontology for Data Classification
"""
import streamlit as st

st.set_page_config(page_title="Taxonomy & Ontology", page_icon="🗂️", layout="wide")

st.title("🗂️ Taxonomy & Ontology")

st.markdown("""
In data operating theory, these terms describe HOW we organize and define data relationships.
Often confused but fundamentally different.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("## 📋 Taxonomy")
    st.markdown("""
    **Definition:** Hierarchical classification system for naming and organizing things.
    
    **Structure:**
    - Parent-child relationships
    - Mutually exclusive categories
    - Single path from top to bottom
    
    **Example in Gene Therapy:**
    ```
    Data
    ├── Clinical
    │   ├── Patient Demographics
    │   └── Trial Outcomes
    ├── Manufacturing
    │   ├── Process Data
    │   └── Quality Data
    └── Regulatory
        ├── Batch Records
        └── Compliance Data
    ```
    
    **Use Case:** Organizing data catalog, structuring folders/databases
    
    **Interview Tip:** "A taxonomy helps teams find data quickly and avoid duplicates."
    """)

with col2:
    st.markdown("## 🕸️ Ontology")
    st.markdown("""
    **Definition:** Formal representation of knowledge defining concepts and relationships.
    
    **Structure:**
    - Properties and attributes of entities
    - Relationships between entities (is-a, has-a, part-of)
    - Rules and constraints
    
    **Example in Gene Therapy:**
    ```
    Batch
    ├── has properties: ID, start_date, status
    ├── belongs_to: Product
    ├── produces: Lots
    └── constraints: status must be one of [Setup, In Progress, Complete]
    
    Lot
    ├── has properties: ID, quantity, purity
    ├── part_of: Batch
    └── contains: Vials
    ```
    
    **Use Case:** Semantic understanding, AI/ML training, system design
    
    **Interview Tip:** "Ontologies enable machines to understand data meaning, not just structure."
    """)

st.markdown("---")

st.markdown("## 🔄 Visual Comparison")

comparison_df = {
    "Aspect": ["Purpose", "Structure", "Relationships", "Complexity", "Use When..."],
    "Taxonomy": [
        "Organize and categorize",
        "Hierarchical tree",
        "Parent → Child (one path)",
        "Simpler",
        "Need clear navigation and naming"
    ],
    "Ontology": [
        "Define meaning and knowledge",
        "Graph with multiple relationships",
        "Any relationships (many paths possible)",
        "More complex",
        "Need semantic understanding and AI integration"
    ]
}

import pandas as pd
df = pd.DataFrame(comparison_df)
st.dataframe(df, use_container_width=True)

st.markdown("---")

st.markdown("## 💼 Gene Therapy Example: Batch Data")

st.info("""
### Taxonomy View (How to organize)
```
Batch Records
├── Process Parameters
│   ├── Temperature
│   ├── pH
│   └── Pressure
├── Quality Results
│   ├── Titer
│   ├── Purity
│   └── Viability
└── Regulatory Documentation
```

### Ontology View (What it means)
```
Process Parameter (concept)
- Has properties: measurement, unit, timestamp
- Affects: Product Quality
- Related to: Equipment

Quality Result (concept)
- Has properties: test_method, result_value, specification_limit
- Determines: Batch Acceptance
- Created by: QA Analyst
- Used in: Release Decision
```

**The Key Difference:**
- **Taxonomy** tells you WHERE to find batch temperature data (in "Process Parameters" folder)
- **Ontology** tells you WHAT batch temperature means (affects product quality, determined by equipment type, compared against spec limit)
""")

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("taxonomy")
    st.success("Section marked as completed!")
    st.balloons()
