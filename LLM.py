import os
from dotenv import load_dotenv


def format_prompt_1(StudentAnswer,TeacherAnswer,TotalMarks):
    prompt = f"""
    Assume you are an examiner,
     
    Providing you Student Answer and Teacher's Answer below : 

    You Have to provide below details in brief : 
    1. Missing Points : The point by point (in formatted way each point in newline) which are missing in student answer , but present in teacher's answer
    2. Bluff Points : The point by point (in formatted way each point in newline) which are present in student answer, but not in teacher's answer   
    3. Student Marks : Highlight the Student's Marks based on rules given below.

    
    Mark Evaluation Rules : 
    a. Each Point in teacher's answer have equal weightage, call it weight_per_point = (Total Marks) / ( number of remarkable points in teacher's answer), for each missing point cut that weight_per_point/2,
    b. For each bluff point cut weight_per_point/4
    c. Round of ceiling of marks.

    StudentAnswer : "{StudentAnswer}"

    TeacherAnswer : "{TeacherAnswer}"

    TotalMarks : "{TotalMarks}"

    

    """
    
    return prompt


 
# loading env varaibles
load_dotenv()
# REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
hf_token=os.getenv('HF_TOKEN')

# querying
def query(payload):
    
    import requests

    # Replace API URL with your LLM API URL ( from hugging face. i.e. )
    # for example HF_LLM_INFERENCE_CHECKPOINT='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    # API_URL='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    API_URL="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    # API_URL = os.getenv('HF_LLM_INFERENCE_CHECKPOINT')

    headers = {"Authorization": "Bearer "+hf_token}
    
    # retriving response
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def prompt_format_2(StudentAnswer,TeacherAnswer,TotalMarks):
  formatted_prompt=format_prompt_1(StudentAnswer,TeacherAnswer,TotalMarks)
  prompt='<s>[INST] '+formatted_prompt+'\n [/INST] Model answer</s>'
  return prompt

def infer(StudentAnswer,TeacherAnswer,TotalMarks):
  try:
      print("going to infer")

      prompt=prompt_format_2(StudentAnswer,TeacherAnswer,TotalMarks)
      
      # print("generated prompt",prompt)
      output = query({
          "inputs": prompt,
          "parameters": 
        {
          "contentType": "application/json",
          "max_tokens": 20000,
          "max_new_tokens": 4000,
          "return_full_text": False
        }
      })

      return output[0]['generated_text']
  except Exception as e:
        print(f"An error occurred: {e}")
        return f"could not generate answer Due to Error, please try after some time ,{e} "  