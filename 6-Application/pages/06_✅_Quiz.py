"""
Interactive Quiz with Immediate Feedback
"""
import streamlit as st
from utils.data_loader import load_quiz

st.set_page_config(page_title="Quiz", page_icon="✅", layout="wide")

st.title("✅ Data Operating Theory Mastery Quiz")

st.markdown("""
Test your understanding with 10 questions covering all aspects of data operating theory.
You'll receive immediate feedback on each answer.
""")

# Initialize session state
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

quiz_data = load_quiz()
questions = quiz_data['questions']

# Display quiz
for i, q in enumerate(questions, 1):
    st.markdown(f"### Question {i}")
    st.markdown(f"**{q['question']}**")
    
    # Radio button for answer selection
    answer_key = f"q{i}"
    selected = st.radio(
        "Select your answer:",
        options=q['options'],
        key=answer_key,
        index=None
    )
    
    # Check answer button
    if st.button(f"Check Answer {i}", key=f"check{i}"):
        if selected is None:
            st.warning("Please select an answer first!")
        else:
            selected_index = q['options'].index(selected)
            st.session_state.quiz_answers[i] = selected_index
            
            if selected_index == q['correct_index']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Incorrect. The correct answer is: **{q['options'][q['correct_index']]}**")
                st.info(f"📚 Explanation: {q['explanation']}")
    
    st.markdown("---")

# Submit quiz button
if st.button("🎯 Submit Quiz and See Final Score", type="primary"):
    if len(st.session_state.quiz_answers) < len(questions):
        st.warning(f"You've only answered {len(st.session_state.quiz_answers)} out of {len(questions)} questions.")
    else:
        # Calculate score
        correct = sum(1 for i, q in enumerate(questions, 1) 
                     if st.session_state.quiz_answers.get(i) == q['correct_index'])
        
        st.session_state.quiz_score = correct
        st.session_state.quiz_submitted = True
        
        # Display results
        st.balloons()
        
        score_percent = (correct / len(questions)) * 100
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Correct Answers", f"{correct}/{len(questions)}")
        with col2:
            st.metric("Score", f"{score_percent:.0f}%")
        with col3:
            if score_percent >= 80:
                st.metric("Result", "🌟 Excellent!")
            elif score_percent >= 60:
                st.metric("Result", "👍 Good")
            else:
                st.metric("Result", "📚 Keep Learning")
        
        # Performance feedback
        st.markdown("### 📊 Performance Analysis")
        
        if score_percent >= 80:
            st.success("""
            **Excellent Work!** You demonstrate strong mastery of data operating theory concepts.
            You're ready to articulate these frameworks in technical discussions and interviews.
            """)
        elif score_percent >= 60:
            st.info("""
            **Good Foundation!** You understand core concepts but could strengthen your knowledge.
            Review the sections where you missed questions and try the quiz again.
            """)
        else:
            st.warning("""
            **Keep Learning!** Data operating theory requires deep understanding of multiple concepts.
            We recommend reviewing all modules again before the interview. Focus on understanding 
            the 'why' behind each principle, not just memorizing definitions.
            """)
        
        # Topic breakdown
        topic_performance = {}
        for i, q in enumerate(questions, 1):
            topic = q['topic']
            if topic not in topic_performance:
                topic_performance[topic] = {'correct': 0, 'total': 0}
            topic_performance[topic]['total'] += 1
            if st.session_state.quiz_answers.get(i) == q['correct_index']:
                topic_performance[topic]['correct'] += 1
        
        st.markdown("### 📈 Performance by Topic")
        for topic, stats in topic_performance.items():
            percent = (stats['correct'] / stats['total']) * 100
            st.progress(percent / 100)
            st.caption(f"{topic.replace('_', ' ').title()}: {stats['correct']}/{stats['total']} correct")

if st.button("🔄 Reset Quiz"):
    st.session_state.quiz_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.quiz_score = None
    st.rerun()

if st.button("✅ Mark Section as Completed"):
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()
    st.session_state.completed_sections.add("quiz")
    st.success("Section marked as completed!")
    st.balloons()
