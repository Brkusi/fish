import streamlit as st
import os
import joblib
from PIL import Image
import base64
from io import BytesIO

# Set the working directory
os.chdir("C:\\Users\\elkus\\OneDrive\\Desktop\\fish")

# Load the model
spam_clf = joblib.load(open('models/my_phishing_model.pkl', 'rb'))

# Load the vectorizer
vectorizer = joblib.load(open('vectors/my_vectorizer.pickle', 'rb'))

def get_image_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

### MAIN FUNCTION ###
def main(title="EMAIL PHISHING IDENTIFIER".upper()):
    # Add custom CSS for styling, including font loading
    st.markdown("""
        <style>
            @font-face {
                font-family: 'RamadhanMubarok';
                src: url('C:/Users/elkus/OneDrive/Desktop/fish/fonts/RamadhanMubarok-Regular.woff') format('truetype');
            }
            body {
                background-color: #1f282c;
            }
            .reportview-container {
                background: #ffffff;
                padding: 20px;
                border-radius: 10px;
                color: #333;
            }
            .stButton button {
                background-color: #d3d3d3; /* Gray color */
                color: black;
                padding: 10px 24px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #c0c0c0; /* Slightly darker gray */
            }
            .stTextInput, .stTextInput input {
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            .header-title {
                font-family: 'RamadhanMubarok', sans-serif;
                text-align: center;
                font-size: 50px;
                color: #FF0000;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Shadow effect */
                margin-bottom: 80px; /* Adjust this value to reduce spacing */
            }
            .center-image {
                display: flex;
                justify-content: center;
                margin-top: -548px; /* Adjusted margin-top to reduce spacing */
            }
            .center-image img {
                max-width: 200%;
                height: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    # Page Title with improved styling
    st.markdown("<h1 class='header-title'>{}</h1>".format(title), unsafe_allow_html=True)

    # Load and display the image with a larger size
    img = Image.open("C:\\Users\\elkus\\OneDrive\\Desktop\\fish\\images\\phishing.png")
    img_base64 = get_image_base64(img)
    st.markdown(
        f"""
        <div class='center-image'>
            <img src='data:image/png;base64,{img_base64}' width='1600' />
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add a section for the email input
    with st.expander("🔍 **Check Your Email**"):
        st.markdown("<p style='font-family:Calibri; font-size: 18px;'>Enter the email contents below to check if it’s a phishing attempt:</p>", 
                    unsafe_allow_html=True)
        
        Email = st.text_area("Email Content", height=150, placeholder="Copy and paste the email content here...")

        if st.button("Predict"):
            prediction = spam_clf.predict(vectorizer.transform([Email]))

            if prediction[0] == 0:
                st.success('🎉 This email is likely safe: **NOT PHISHING**')
            else:
                st.error('⚠️ Warning: This email could be **PHISHING**')

    # Add a footer
    st.markdown("<hr style='border:1px solid #c0c0c0;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #c0c0c0; font-size: 14px;'>Created by Brian Kusi | Stay Alert: Don't Get Hooked!</p>", 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()
