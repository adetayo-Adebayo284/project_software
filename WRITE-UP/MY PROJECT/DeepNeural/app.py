# import streamlit as st

# from config.globals import SPEAKER_TYPES, initial_prompt

# from services.model.generative_ai import StudentModelChat


# chat_conversation = StudentModelChat()

# # Set up the streamlit app
# st.set_page_config(
#   page_title="RECURRENT NEURAL NETWORK",
#   page_icon="🤖",
#   layout="wide",
#   initial_sidebar_state="expanded",
# )

# # Initialize a session state to hold the chat history
# if 'chat_history' not in st.session_state:
#   st.session_state.chat_history = [initial_prompt]

# def clear_chat_history():
#   st.session_state.chat_history = [initial_prompt]

# with st.sidebar:
#   st.title('RECURRENT NEURAL NETWORK FOR AUTOMATED CONTENT GENERATION FOR MEDIA')
#   st.write('Developed by HASSAN OLALEKAN')  
#   # st.sidebar.button('Clear Chat', on_click=clear_chat_history, type='secondary')
#   # st.sidebar.button('About', on_click=, type='green')

# # Get user input and generate response
# prompt = st.chat_input("Ask me any question...", key="user_input")

# # Show the welcome prompt
# with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
#   st.write(initial_prompt['content'])

# if prompt:
#   st.session_state['chat_history'].append({'role': SPEAKER_TYPES.USER, 'content': prompt})
  
#   # Display chat messages
#   for message in st.session_state.chat_history[1:]:
#     with st.chat_message(message["role"], avatar="👤" if message['role'] == SPEAKER_TYPES.USER else "🤖"):
#       st.write(message["content"])
  
#   response_stream = chat_conversation.get_response(prompt, stream=True)
#   response_text = ''
#   with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
#     placeholder = st.empty()
#     with st.spinner(text='Generating response...'):
#       for chunk in response_stream:
#         response_text += chunk.text
#         placeholder.markdown(response_text.replace("language model, trained by Google", "language model, trained by Yahweh Tech").replace("I am Gemini", "I am Gemini Yahweh Tech").replace("I am Gemini Yahweh Tech, a multimodal AI language model developed by Google.", "I am Yahweh Tech bot, a multimodal AI language model developed by Yahweh Tech."))
#       placeholder.markdown(response_text.replace("language model, trained by Google", "language model, trained by Yahweh Tech").replace("I am Gemini", "I am Gemini Yahweh Tech").replace("I am Gemini Yahweh Tech, a multimodal AI language model developed by Google.", "I am Yahweh Tech bot, a multimodal AI language model developed by Yahweh Tech."))
  
#   st.session_state['chat_history'].append({'role': SPEAKER_TYPES.BOT, 'content': response_text})

















































































































































































































import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

from config.globals import SPEAKER_TYPES, initial_prompt
from services.model.generative_ai import StudentModelChat

chat_conversation = StudentModelChat()

# Set up the streamlit app
st.set_page_config(
  page_title="Deep Neural Network",
  page_icon="🤖",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Initialize a session state to hold the chat history
if 'chat_history' not in st.session_state:
  st.session_state.chat_history = [initial_prompt]

# Define output array
output_array = []

def clear_chat_history():
  st.session_state.chat_history = [initial_prompt]

def display_home():
  st.title('Home')
  prompt = st.chat_input("Ask me any question...", key="user_input")

  # Show the welcome prompt
  with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
    st.write(initial_prompt['content'])

  if prompt:
    st.session_state['chat_history'].append({'role': SPEAKER_TYPES.USER, 'content': prompt})
    
    # Display chat messages
    for message in st.session_state.chat_history[1:]:
      with st.chat_message(message["role"], avatar="👤" if message['role'] == SPEAKER_TYPES.USER else "🤖"):
        st.write(message["content"])
    
    response_stream = chat_conversation.get_response(prompt, stream=True)
    response_text = ''
    with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
      placeholder = st.empty()
      with st.spinner(text='Generating response...'):
        for chunk in response_stream:
          response_text += chunk.text
          replaced_text = response_text.replace("language model, trained by Google", "language model, trained by Yahweh Tech").replace("I am Gemini", "I am Gemini Yahweh Tech").replace("I am Gemini Yahweh Tech, a multimodal AI language model developed by Google.", "I am Yahweh Tech bot, a multimodal AI language model developed by Yahweh Tech.")
          placeholder.markdown(f'<div class="animated-text">{replaced_text}</div>', unsafe_allow_html=True)
          output_array.append(replaced_text)
        placeholder.markdown(f'<div class="animated-text">{replaced_text}</div>', unsafe_allow_html=True)
    
    st.session_state['chat_history'].append({'role': SPEAKER_TYPES.BOT, 'content': response_text})

def display_about():
    st.title('About')
    st.write('This application is developed by ADEBAYO ADETAYO ABDULRASAKI AND IGWE PRECIOUS CHIAMAKA.')
    
    st.write("""
    **Adebayo Adetayo Abdulrasaki** is a dedicated student from Gateway ICT Polytechnic Saapade, located in Ogun State, Nigeria. He is currently pursuing a National Diploma (ND) in Computer Science, showcasing his commitment to understanding and excelling in the field of technology.
    
    **Igwe Precious Chiamaka** is a dedicated student from Gateway ICT Polytechnic Saapade, located in Ogun State, Nigeria. She is currently pursuing a National Diploma (ND) in Computer Science, showcasing her commitment to understanding and excelling in the field of technology.
             
    ### Educational Background
    Adebayo and Precious are enrolled in the Computer Science program at Gateway ICT Polytechnic, where they are gaining foundational knowledge and practical skills in various aspects of computing. Their coursework includes programming, software development, data structures, algorithms, and computer systems, among other subjects. This rigorous curriculum is designed to prepare students for careers in the fast-evolving tech industry.
    
    ### Skills and Interests
    Throughout their studies, they developed a strong interest in several key areas within computer science, including:
    
    - **Programming Languages**: They are proficient in programming languages such as Python, Java, C Language, which are essential for software development and algorithm implementation.
    - **Web Development**: They have explored web technologies, including HTML, CSS, JavaScript, and frameworks like React or Django and PHP, enabling them to create dynamic and responsive web applications.
    - **Data Analysis**: With a growing interest in data science, they learned to use tools like NumPy, Pandas, and Matplotlib to analyze and visualize data, providing valuable insights.
    - **Artificial Intelligence and Machine Learning**: They are fascinated by AI and ML technologies and has started to delve into these areas, understanding how they can be applied to solve real-world problems.
    
    ### Projects and Experience
    As part of their academic journey, they worked on various projects that highlight their skills and knowledge. These projects include:
    
    - **Chatbot Development**: Creating intelligent chatbots using natural language processing (NLP) techniques, enhancing user interaction and providing automated assistance.
    - **Web Applications****: Developing full-stack web applications that demonstrate their ability to integrate front-end and back-end technologies.
    - **Data Analysis Projects**: Conducting data analysis projects to extract meaningful patterns and trends from datasets, improving decision-making processes.
    
    ### Personal Attributes
    Adebayo and Precious are known for their:
    
    - **Dedication and Hard Work**: They are committed to their studies and consistently strives for excellence in all their academic endeavors.
    - **Curiosity and Eagerness to Learn**: Adebayo has a natural curiosity and a strong desire to learn new technologies and concepts, staying updated with the latest trends in computer science.
    - **Problem-Solving Skills**: They enjoys tackling complex problems and finding innovative solutions, a key trait for success in the tech industry.
    - **Teamwork and Collaboration**: They value teamwork and has experience working collaboratively on projects, understanding the importance of effective communication and cooperation.
    
    ### Future Aspirations
    Looking ahead, they aim to further their education and gain more experience in the tech industry. they aspire to become a software developer, contributing to the development of innovative technologies and solutions. Their long-term goal is to leverage their skills and knowledge to make a positive impact in the field of technology and society at large.
    """)

def display_chart_performance():
  st.title('Chat Performance')
  
  # Simulate some data for chart performance
  effectiveness_data = np.random.rand(10, 3)  # 10 data points, 3 dimensions
  fig, ax = plt.subplots()
  ax.plot(effectiveness_data)
  ax.set_title('User Chat Effectiveness')
  ax.set_xlabel('Interaction')
  ax.set_ylabel('Effectiveness')
  st.pyplot(fig)

def display_contact():
    st.title('Contact')
    st.write('For more information, contact:')
    st.write("""
    **Adebayo Adetayo Abdulrasaki**  
    **📞 +2347066253101**  
    **📧 adebayoadetayo284@gmail.com**
    """)
    st.write("""
    """)
    st.write("""
    **Igwe Precious Chiamaka**  
    **📞 +2348112489385**  
    **📧 chiamakap878@gmail.com**
    """)


# Custom CSS for sidebar and text animation
custom_css = """
<style>
  .sidebar .sidebar-content {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
  }
  .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
    color: #2e3b4e;
  }
  .sidebar .sidebar-content p {
    color: #5c677d;
  }
  .sidebar .sidebar-content .stButton>button {
    background-color: #2e3b4e;
    color: #ffffff;
  }
  .sidebar .sidebar-content .stRadio>div>div>div>div {
    background-color: #2e3b4e;
    color: #ffffff;
  }
  .animated-text {
    animation: fadeIn 2s ease-in-out;
  }
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
</style>
"""

# Inject the custom CSS
components.html(custom_css, height=0)

with st.sidebar:
  st.title('♊💬 Deep Neural Network to optimize Student Revision Classes')
  st.write('Developed by Adebayo Adetayo Abdulrasaki & Igwe Precious Chiamaka')
  st.sidebar.button('Clear Chat', on_click=clear_chat_history, type='secondary')
  
  choice = st.radio('Navigation', ['HOME', 'ABOUT', 'CHAT PERFORMANCE', 'CONTACT'])

# Display the chosen page
if choice == 'HOME':
  display_home()
elif choice == 'ABOUT':
  display_about()
elif choice == 'CHAT PERFORMANCE':
  display_chart_performance()
elif choice == 'CONTACT':
  display_contact()





























































































































# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import streamlit.components.v1 as components

# # Assuming you have these imports from your project structure
# from config.globals import SPEAKER_TYPES, initial_prompt
# from services.model.generative_ai import StudentModelChat

# # Initialize the chat conversation object
# chat_conversation = StudentModelChat()

# # Set page configuration
# st.set_page_config(
#     page_title="Deep Neural Network",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Initialize session state for chat history
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = [initial_prompt]

# # Define output array
# output_array = []

# # Function to clear chat history
# def clear_chat_history():
#     st.session_state.chat_history = [initial_prompt]

# # Function to display Home page
# def display_home():
#     st.title('Home')
#     prompt = st.text_input("Ask me any question...")

#     # Display initial prompt
#     with st.empty():
#         st.write(initial_prompt['content'])

#     if prompt:
#         st.session_state.chat_history.append({'role': SPEAKER_TYPES.USER, 'content': prompt})
        
#         # Display chat history
#         for message in st.session_state.chat_history[1:]:
#             with st.empty():
#                 st.write(message["role"], message["content"])

#         response_stream = chat_conversation.get_response(prompt, stream=True)
#         response_text = ''
#         with st.empty():
#             for chunk in response_stream:
#                 response_text += chunk.text

#         st.session_state.chat_history.append({'role': SPEAKER_TYPES.BOT, 'content': response_text})

# # Function to display About page
# def display_about():
#     st.title('About')
#     st.write('This application is developed by Adebayo Adetayo Abdulrasaki.')

#     # Insert the about content here
#     # ...

# # Function to display Chart Performance page
# def display_chart_performance():
#     st.title('Chart Performance')
    
#     # Simulate some data for chart performance
#     effectiveness_data = np.random.rand(10, 3)  # 10 data points, 3 dimensions
#     fig, ax = plt.subplots()
#     ax.plot(effectiveness_data)
#     ax.set_title('User Chat Effectiveness')
#     ax.set_xlabel('Interaction')
#     ax.set_ylabel('Effectiveness')
#     st.pyplot(fig)

# # Function to display Contact page
# def display_contact():
#     st.title('Contact')
#     st.write('For more information, contact:')
#     st.write("""
#     **Adebayo Adetayo Abdulrasaki**  
#     **📞 +2347066253101**  
#     **📧 adebayoadetayo284@gmail.com**
#     """)

# # Custom CSS for sidebar and text animation
# custom_css = """
# <style>
#   .sidebar .sidebar-content {
#     background-color: #f4f4f4;
#     padding: 20px;
#     border-radius: 10px;
#   }
#   .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
#     color: #2e3b4e;
#   }
#   .sidebar .sidebar-content p {
#     color: #5c677d;
#   }
#   .sidebar .sidebar-content .stButton>button {
#     background-color: #2e3b4e;
#     color: #ffffff;
#   }
#   .sidebar .sidebar-content .stRadio>div>div>div>div {
#     background-color: #2e3b4e;
#     color: #ffffff;
#   }
#   .animated-text {
#     animation: fadeIn 2s ease-in-out;
#   }
#   @keyframes fadeIn {
#     0% { opacity: 0; }
#     100% { opacity: 1; }
#   }
# </style>
# """

# # Inject the custom CSS
# components.html(custom_css, height=0)

# # Sidebar navigation
# with st.sidebar:
#     st.title('♊💬 Deep Neural Network to optimize Student Revision Classes')
#     st.write('Developed by Adebayo Adetayo Abdulrasaki')
#     st.sidebar.button('Clear Chat', on_click=clear_chat_history, type='secondary')
    
#     choice = st.radio('Navigation', ['HOME', 'ABOUT', 'CHART PERFORMANCE', 'CONTACT'])

# # Display the selected page
# if choice == 'HOME':
#     display_home()
# elif choice == 'ABOUT':
#     display_about()
# elif choice == 'CHART PERFORMANCE':
#     display_chart_performance()
# elif choice == 'CONTACT':
#     display_contact()
