"""
Utility module for loading data files with cloud deployment support
"""
import json
from pathlib import Path
import streamlit as st


def get_project_root():
    """Get the project root directory, supporting both local and cloud deployment."""
    # The script is at: 6-Application/utils/data_loader.py
    # Project root is 3 levels up
    return Path(__file__).parent.parent.parent


def get_data_path(filename):
    """Get the full path to a data file."""
    root = get_project_root()
    return root / "2-Generation" / "data" / filename


@st.cache_data
def load_principles():
    """Load principles.json with error handling."""
    try:
        file_path = get_data_path("principles.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"❌ Could not find principles.json at {file_path}")
        st.info("Make sure the file exists in the 2-Generation/data/ directory")
        return {"principles": []}
    except json.JSONDecodeError:
        st.error("❌ Error parsing principles.json - file may be corrupted")
        return {"principles": []}


@st.cache_data
def load_quiz():
    """Load quiz_questions.json with error handling."""
    try:
        file_path = get_data_path("quiz_questions.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"❌ Could not find quiz_questions.json at {file_path}")
        st.info("Make sure the file exists in the 2-Generation/data/ directory")
        return {"questions": []}
    except json.JSONDecodeError:
        st.error("❌ Error parsing quiz_questions.json - file may be corrupted")
        return {"questions": []}
