import streamlit as st

# Define the training_page function
def training_page():
    st.title("Training Management 🏋️‍♂️")

    # Display Percentage
    if "percentage" in st.session_state:
        percentage = st.session_state["percentage"]
        st.subheader(f"Your Quiz Score: {percentage:.2f}%")
        
        if percentage > 60:
            st.success("Congratulations! You scored above 60%. No training required.")
            return
        else:
            st.warning("You scored 60% or below. Training is required.")
    else:
        st.error("Quiz score not available. Please complete the quiz first.")
        return

    # Department Selection for Training
    st.subheader("Select Department for Training")
    department = st.selectbox(
        "Choose a department",
        ["Finance", "Operations", "HR", "IT"]
    )

    # Display Training Plan Based on Department
    st.subheader("Training Plan")
    if department == "Finance":
        st.write("""
        **Finance Training Plan:**
        - Module 1: Basics of Accounting
        - Module 2: Financial Risk Management
        - Module 3: Budgeting and Forecasting
        """)
    elif department == "Operations":
        st.write("""
        **Operations Training Plan:**
        - Module 1: Process Optimization
        - Module 2: Supply Chain Management
        - Module 3: Quality Assurance
        """)
    elif department == "HR":
        st.write("""
        **HR Training Plan:**
        - Module 1: Recruitment Strategies
        - Module 2: Employee Engagement
        - Module 3: Conflict Resolution
        """)
    elif department == "IT":
        st.write("""
        **IT Training Plan:**
        - Module 1: Cybersecurity Basics
        - Module 2: Cloud Computing
        - Module 3: Software Development Life Cycle
        """)

    # Assign Training Confirmation
    if st.button("Confirm Training"):
        st.success(f"Training modules for the {department} department have been assigned successfully!")

# Call the function
if __name__ == "__main__":
    training_page()
