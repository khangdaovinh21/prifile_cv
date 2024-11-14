import streamlit as st

# Thiết lập trang
st.set_page_config(page_title="Dao Vinh Khang - AI Engineer", page_icon=":rocket:", layout="centered")

# CSS tùy chỉnh
st.markdown("""
    <style>
        body {
            color: white;
        }
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #3498db;
        }
        .subtitle {
            font-size: 1.5em;
            color: white; /* Đặt màu chữ trắng cho "AI Engineer" */
        }
        .section-title {
            font-size: 1.8em;
            margin-top: 20px;
            color: #3498db;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .highlight {
            font-size: 1.2em;
            font-weight: bold;
            color: #e67e22;
        }
        .contact-info, .education-info, .skills-info, .project-links {
            font-size: 1.1em;
            color: white; /* Đặt màu chữ trắng cho tất cả các mục */
        }
        .project-links a {
            color: #3498db;
            text-decoration: none;
        }
        .project-links a:hover {
            color: #e74c3c;
        }
        .footer {
            font-size: 0.9em;
            color: #7f8c8d;
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Table of Contents
st.sidebar.title("Table of Contents")
st.sidebar.markdown("[Summary](#summary)", unsafe_allow_html=True)
st.sidebar.markdown("[Skills & Abilities](#skills-abilities)", unsafe_allow_html=True)
st.sidebar.markdown("[Experience](#experience)", unsafe_allow_html=True)
st.sidebar.markdown("[Personal Projects](#personal-projects)", unsafe_allow_html=True)
st.sidebar.markdown("[Education](#education)", unsafe_allow_html=True)

# Tiêu đề và thông tin cá nhân
st.markdown("<div class='main-title'>DAO VINH KHANG</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI Engineer</div>", unsafe_allow_html=True)
st.write("📍 Tan Binh, TP Ho Chi Minh")
st.write("📞 +84 834684568 | 📧 DAOVINHKHANG0834@GMAIL.COM")

# Tóm tắt
st.markdown("<a id='summary'></a>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Summary</div>", unsafe_allow_html=True)
st.write("""
As an AI Engineer, I gained foundational experience in AI during my internship at FPT IS, where I worked in mobile development but had opportunities to explore AI projects. This experience ignited my passion for AI, particularly in stock prediction and sentiment analysis. Through a personal project using LSTM-GRU and FinBERT models, I further developed my skills in integrating AI models into mobile and backend systems, blending my technical expertise with a strong drive for innovation in AI.
""")

# Kỹ năng
st.markdown("<a id='skills-abilities'></a>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Skills & Abilities</div>", unsafe_allow_html=True)
st.markdown("""
<ul class='skills-info'>
    <li><strong>AI & Machine Learning, Deep Learning:</strong> LSTM, GRU, BERT, TensorFlow, scikit-learn, Keras, TF-IDF, Natural Language Processing (spaCy).</li>
    <li><strong>Data Processing & Engineering:</strong> Experience with data collection, pre-processing, and integration using APIs and real-time data streams.</li>
    <li><strong>Languages:</strong> Proficient in Python, TypeScript, JavaScript, Kotlin.</li>
    <li><strong>Mobile Development:</strong> Experienced with React Native, Android Studio, Firebase, SQLite, Redux, Axios.</li>
    <li><strong>Backend Development:</strong> Node.js, Express, MongoDB, Firebase.</li>
    <li><strong>Communication:</strong> Strong teamwork, with experience in report writing.</li>
    <li><strong>English:</strong> B1 Vstep</li>
</ul>
""", unsafe_allow_html=True)

# Kinh nghiệm làm việc
st.markdown("<a id='experience'></a>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Experience</div>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>Intern Mobile & AI Developer at FPT IS (July 2023 - Sep 2024)</div>", unsafe_allow_html=True)
st.write("""
- **Data Preprocessing & Feature Extraction**: Processed user queries into feature matrices using CountVectorizer and NLP techniques.
- **Model Development**: Built and trained a Naive Bayes (MultinomialNB) model to classify queries into response categories.
- **Model Evaluation & Optimization**: Evaluated model accuracy and applied parameter tuning for better classification.
- **Deployment & Integration**: Integrated the model into a React Native app via Axios for real-time query processing.
- **UI Design with React Native**: Developed user-friendly chatbot interfaces.
- **Redux for State Management**: Managed state with Redux for smooth API interactions and real-time updates.
""")

# Dự án cá nhân
st.markdown("<a id='personal-projects'></a>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Personal Projects</div>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>Stock Prediction and Sentiment Analysis Mobile App (May 2024 - Ongoing)</div>", unsafe_allow_html=True)
st.write("""
- **Stock Prediction Model**: Developed a hybrid LSTM-GRU model integrated with financial indicators for stock price prediction.
- **News Sentiment and Event Analysis**: Built a FinBERT-based system for news sentiment analysis and event impact detection.
- **Feature Engineering**: Integrated technical indicators to enhance predictive capabilities.
- **Model Training**: Optimized model performance with early stopping and regularization.
- **Flask Stock Prediction API**: Developed RESTful APIs with Flask for real-time stock predictions using LSTM and FinBERT.
- **Mobile Application**: Designed a React Native app for visualizing stock predictions and news impact analysis.
""")

# Liên kết đến các mô hình và video demo
st.markdown("<div class='project-links'><strong>Project Links:</strong></div>", unsafe_allow_html=True)
st.write("[Stock Sentiment Analysis Model](https://sentimentanalyststock0.streamlit.app/)")
st.write("[Stock Price Prediction Model](https://predictionstockprice0.streamlit.app/)")
st.write("[Video & Project Folder](https://drive.google.com/drive/folders/1Ll4YDw-egHEWIwNWtTYS6eT5MPCT88RU?usp=sharing)")
st.write("[Other Projects](https://drive.google.com/drive/folders/1JRDeqdpCSuxKTuz5xNmfTftQeVfqnui4?usp=sharing)")

# Học vấn
st.markdown("<a id='education'></a>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
st.write("""
- **Greenwich University (2020 - 2024)**: BSc (Hons) in Computing (First Class Honours, Equivalent to Excellent)
- GPA 3.7/4.0
- **Awards**: Certificate of Merit (RVR), Best Student in Final Project (Spring 2024), Front End Development Libraries Certification – freeCodeCamp.
""")
st.write("[Certificates & Awards](https://drive.google.com/drive/folders/1K45jB8o5n3tYXjOtUzf_SVYLCdaXgWX3?usp=sharing)")

# Chân trang
st.markdown("<div class='footer'>Connect with me on LinkedIn | GitHub | Twitter</div>", unsafe_allow_html=True)
