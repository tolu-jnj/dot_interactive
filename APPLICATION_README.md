# Data Operating Theory Mastery Tool

Interactive Streamlit application for learning data operating theory concepts applied to gene therapy manufacturing operations.

## Features

- **8 Core Principles**: Learn the foundational principles of data operating theory with pharma examples
- **Data Architecture**: Understand 4 types of data capture (State, Event, Atomic, Structure)
- **Maturity Models**: Explore Data Aware, Data Informed, and Data Driven decision-making
- **Lean Integration**: Map 8 lean manufacturing wastes to data problems and solutions
- **Data Quality Standards**: Understand 6 dimensions of quality and critical risk metrics
- **Interactive Quiz**: 10 questions with immediate feedback and scoring
- **DAMA Framework**: Learn 11 knowledge areas of data management
- **Taxonomy & Ontology**: Understand data classification and semantic relationships
- **User Impact Alignment**: Three levels of design for business transformation
- **Business Optimization**: Connect data projects to revenue, expense, quality, and speed
- **Interview Practice**: 6 realistic interview questions with structured answers

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Locally

```bash
cd 6-Application
streamlit run app.py
```

Or use the launch script:
```bash
chmod +x 6-Application/app.sh
./6-Application/app.sh
```

The app will be available at `http://localhost:8501`

## Project Structure

```
dot_interactive/
├── 1-Governance/              # Governance documentation
│   ├── README.md
│   └── requirements.txt
├── 2-Generation/              # Source data files
│   └── data/
│       ├── principles.json    # 8 principles definitions
│       └── quiz_questions.json # 10 quiz questions
├── 6-Application/             # Streamlit application
│   ├── app.py                # Main app entry point
│   ├── app.sh                # Launch script
│   └── pages/                # Multi-page structure
│       ├── 01_📋_Principles.py
│       ├── 02_🏗️_Data_Architecture.py
│       ├── 03_📈_Maturity_Models.py
│       ├── 04_🔗_Lean_Integration.py
│       ├── 05_⚖️_Data_Quality.py
│       ├── 06_✅_Quiz.py
│       ├── 07_📚_DAMA_Framework.py
│       ├── 08_🗂️_Taxonomy_Ontology.py
│       ├── 09_🎯_User_Impact.py
│       ├── 10_💰_Business_Optimization.py
│       └── 11_💼_Interview_Practice.py
└── requirements.txt
```

## Pages Overview

| Page | Purpose | Topics |
|------|---------|--------|
| Home | Welcome & overview | Platform introduction |
| Principles | Core concepts | 8 principles with lean connections |
| Data Architecture | Design patterns | State, Event, Atomic, Structure capture |
| Maturity Models | Decision frameworks | Data Aware, Informed, Driven levels |
| Lean Integration | Business value | 8 lean wastes mapped to data solutions |
| Data Quality | Standards & risks | 6 quality dimensions, 5 risk metrics |
| Quiz | Assessment | 10 questions with immediate feedback |
| DAMA Framework | Enterprise view | 11 knowledge areas of data management |
| Taxonomy & Ontology | Data classification | Hierarchical vs. semantic structures |
| User Impact | Business alignment | 3 levels of design framework |
| Optimization | ROI calculations | Revenue, expense, quality, speed trade-offs |
| Interview Practice | Preparation | 6 realistic questions with structure |

## Features

- **Progress Tracking**: Track completed sections in the sidebar
- **Quiz Scoring**: Automatic scoring with topic-level performance breakdown
- **Session State**: Progress persists during your session
- **Responsive Design**: Works on desktop and tablet
- **Color-Coded Content**: Visual hierarchy with custom CSS styling

## Learning Path

1. Start with **Principles** to understand core concepts
2. Learn **Data Architecture** patterns
3. Explore **Maturity Models** for decision contexts
4. Connect concepts with **Lean Integration**
5. Understand **Data Quality** standards
6. Test knowledge with **Quiz**
7. Deepen understanding with **DAMA Framework**, **Taxonomy & Ontology**, and **User Impact**
8. See business applications in **Business Optimization**
9. Practice with **Interview Questions**

## Target Audience

- Data professionals in pharmaceutical/gene therapy operations
- Lean practitioners transitioning to data roles
- Candidates preparing for technical interviews
- Teams learning data operating theory frameworks

## Requirements

- Python 3.8+
- Streamlit 1.28.0+
- pandas, numpy, plotly
- streamlit-extras, streamlit-option-menu
- pillow

## About

This tool was created to provide a comprehensive, self-paced learning platform for data operating theory mastery. It reduces preparation time from hours to minutes and serves as a quick reference for technical discussions.

The content applies specifically to gene therapy manufacturing operations but principles are broadly applicable to any regulated or complex manufacturing environment.
