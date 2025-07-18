import streamlit as st
import json

def load_questions():
    """Load quiz questions from a JSON file."""
    with open("constant//question.json", "r") as f:
        return json.load(f)["questions"]

def quiz_page():
    st.title("Quiz Time 📝")
    st.write("Test your knowledge by answering the questions below!")

    # Load questions
    questions = load_questions()

    # Initialize session state for score and quiz tracking
    if "score" not in st.session_state:
        st.session_state["score"] = 0
    if "answered" not in st.session_state:
        st.session_state["answered"] = [False] * len(questions)  # To track if a question is answered
    if "quiz_finished" not in st.session_state:
        st.session_state["quiz_finished"] = False
    if "percentage" not in st.session_state:
        st.session_state["percentage"] = 0

    # Display each question and options
    for idx, q in enumerate(questions):
        st.subheader(f"Q{idx+1}. ({q['category']}) {q['question']}")
        user_answer = st.radio(
            f"Select an option for Q{idx+1}",
            q["options"],
            key=f"q{idx}"
        )

        # Check answer only if "Submit" is pressed and question isn't already answered
        if st.button(f"Submit Q{idx+1}", key=f"submit{idx}"):
            if not st.session_state["answered"][idx]:
                if user_answer == q["answer"]:
                    st.success("Correct!")
                    st.session_state["score"] += 1
                else:
                    st.error(f"Wrong! The correct answer was: {q['answer']}")
                st.session_state["answered"][idx] = True
            else:
                st.warning("You have already answered this question.")

    # Final Score and Percentage Calculation
    if st.button("Finish Quiz"):
        total_questions = len(questions)
        st.session_state["percentage"] = (st.session_state["score"] / total_questions) * 100
        st.info(f"Your final score is: {st.session_state['score']}/{total_questions}")
        st.info(f"Your percentage is: {st.session_state['percentage']:.2f}%")
        st.session_state["quiz_finished"] = True
        st.balloons()

        # Check if user needs to go through training
        if st.session_state["percentage"] <= 60:
            st.warning("You scored 60% or below. You will need to go through training.")
        else:
            st.success("Great job! You scored above 60%. No additional training needed.")

# Run the page
if __name__ == "__main__":
    quiz_page()
