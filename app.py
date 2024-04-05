import streamlit as st
import streamlit.components.v1 as components
from LLM import infer
from util import write_answer
from trans import speak

max_line_length = 80

def main():
    
    st.set_page_config(
        page_title="Parikshak AI Examiner",
        page_icon="✨",
        # layout="wide",
    )
    
if __name__ == "__main__":
    main()

st.title("AI Examiner - The Parikshak🌟")

st.write("Let's AI analyze the answers!")

st.markdown("#### Step 1 : Upload Student Anwer Photo")
components.html(
    """
    <iframe
        src="https://merve-llava-next.hf.space"
        frameborder="0"
        width="100%"
        height="70%"
    ></iframe>
    """
)
st.markdown("#### Step 2 : Enter Student Answer text extracted from Step 1")
student_answer = st.text_area("Enter student answer extracted text here")

st.markdown("#### Step 3 : Enter Teacher's Answer")
teacher_answer = st.text_area("Enter teacher's answer here")

st.markdown("#### Step 4 : Total Marks of question")
total_marks = st.text_area("Enter total marks of question")


if st.button('Examine Result', key='submit_button', help='Click to submit your input.'):
    placeholder = st.empty()
    placeholder.image("testing.gif")
    Evaluation=infer(student_answer,teacher_answer,total_marks)
    placeholder.empty()

    write_answer(Evaluation,max_line_length)

    speak(Evaluation)
