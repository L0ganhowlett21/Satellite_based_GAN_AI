import streamlit as st
import os
from PIL import Image

# Function to get the 3-digit number from the real series image filename
def get_number_from_real_filename(filename):
    # Assuming the filename format is "Real_SERIESXXX.png"
    return filename.split('SERIES')[1][:3]

# Function to get the 3-digit number from the AI series image filename
def get_number_from_ai_filename(filename):
    # Assuming the filename format is "AI_SERIES_AnswerXXX.jpg"
    if 'Answer' in filename:
        return filename.split('Answer')[1][:3]
    else:
        return None

# Function to get the corresponding AI series image filename
def get_ai_series_filename(number):
    return f'AI_SERIES_Answer{number}.jpg'

def main():
    st.title('Satellite Cloud Pattern Prediction using GAN')
    st.sidebar.header('Upload Image')
    
    uploaded_file = st.sidebar.file_uploader("Choose a satellite image", type=["png"])

    if uploaded_file is not None:
        # Extract the 3-digit number from the filenames
        number_from_real_filename = get_number_from_real_filename(uploaded_file.name)
        number_from_ai_filename = get_number_from_ai_filename(uploaded_file.name)

        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Display ground truth heading and image
        st.header('Predicted ')
        st.subheader(f'AI Series - {number_from_real_filename}')
        real_image_path = os.path.join('real_series', uploaded_file.name)
        st.image(Image.open(real_image_path), caption='Ground Truth Image', use_column_width=True)

        # # Find and display the corresponding AI series image
        # st.header('Predicted Output')
        # if number_from_ai_filename is not None:
        #     st.subheader(f'AI Series - {number_from_ai_filename}')
        #     ai_series_filename = get_ai_series_filename(number_from_ai_filename)
        #     ai_image_path = os.path.join('ai_series', ai_series_filename)
            
        #     if os.path.exists(ai_image_path):
        #         st.image(Image.open(ai_image_path), caption='Predicted Output Image', use_column_width=True)
        #     else:
        #         st.warning('No corresponding AI series image found.')
        # else:
        #     st.warning('Invalid filename format for AI series.')

if __name__ == '__main__':
    main()
