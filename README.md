LLM-PDF QA Search Engine 🔍
LLM-PDF QA Search Engine is a powerful tool designed to extract insights and answer questions from PDF documents using advanced language processing capabilities. Leveraging the LangChain library and OpenAI's LLM (Large Language Model), this application provides users with an interactive platform to interact with PDF content seamlessly. Users can upload their PDF files, ask questions, and receive relevant answers, making it an invaluable tool for document analysis and information retrieval tasks.

Features
PDF Upload: Users can upload PDF files directly to the application.
Natural Language Queries: Users can ask questions about the content of the uploaded PDF documents using natural language queries.
Interactive Interface: The application provides an intuitive and user-friendly interface powered by Streamlit, allowing users to interact with the PDF content effortlessly.
Language Model Integration: The application utilizes OpenAI's LLM model to process and understand natural language queries effectively.
Text Extraction: PDF content is extracted using PyPDF2, enabling the application to analyze and search through the text within the documents.
Cassandra Integration: The application integrates with Cassandra for storing and indexing text data, enabling efficient retrieval of information based on user queries.
Installation
To run the LLM-PDF QA Search Engine locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your_username/llm-pdf-qa-search-engine.git
Navigate to the project directory:

bash
Copy code
cd llm-pdf-qa-search-engine
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run the Streamlit application:

arduino
Copy code
streamlit run app.py
Access the application in your web browser at http://localhost:8501.

Configuration
Before running the application, ensure you have the following configuration set up:

ASTRA_DB_APPLICATION_TOKEN: Enter your Astra DB application token.
ASTRA_DB_ID: Enter your Astra DB database ID.
OPENAI_API_KEY: Enter your OpenAI API key.
About
This project is developed by Adesh Sabari Loganathan as a demonstration of utilizing language models and advanced language processing techniques for PDF document analysis. For any inquiries or contributions, feel free to reach out to the developer via LinkedIn.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Made with ❤️ by Adesh
