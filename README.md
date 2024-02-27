#LLM-PDF QA Search Engine

Project Description:

This project leverages the power of LangChain and OpenAI's large language model (LLM) to create an interactive chatbot that extracts valuable insights and answers complex questions from uploaded PDF documents. The user interface is built using Streamlit for a seamless user experience. Data is stored and indexed within Astra DB's vector store for efficient retrieval.

Key Features:

Chat Interface: Engage in a natural conversation-like interaction with your PDF content.
PDF Support: Upload PDF files of various sizes (with potential compression for larger files).
Advanced LLM-powered Search: Formulate intricate questions to gain deeper understanding from your documents.
Astra DB Integration: Utilize Astra DB's NoSQL capabilities for effective data storage and indexing.
Installation:

Prerequisites:
Python 3.7 or later (https://www.python.org/downloads/)
pip package manager (https://bootstrap.pypa.io/pip/2.7/get-pip.py)
An Astra DB account and a database (https://www.datastax.com/products/datastax-astra)
An OpenAI API key (https://openai.com/blog/openai-api)
Clone the Repository:
Bash
git clone https://github.com/your-username/llm-pdf-qa-search-engine.git
cd llm-pdf-qa-search-engine
Use code with caution.
Create a Virtual Environment (Recommended):
Bash
python -m venv venv
source venv/bin/activate
Use code with caution.
Install Required Packages:
Bash
pip install streamlit langchain openai cassio
Use code with caution.
Configuration:

Astra DB Credentials:
Replace 'YOUR_ASTRA_DB_APPLICATION_TOKEN' and 'YOUR_ASTRA_DB_ID' in the code (lines 14 and 15) with your Astra DB application token and database ID, respectively. You can find these values in your Astra DB account dashboard.
OpenAI API Key:
Set the OPENAI_API_KEY environment variable (line 12) to your OpenAI API key obtained from the OpenAI platform.
Usage:

Run the Application:
Bash
streamlit run app.py
Use code with caution.
Upload a PDF:
In the Streamlit app, click the "Upload your PDF" button and select the desired PDF file.
Ask Questions:
Type your questions in the "Ask questions about your PDF file" text input field and press Enter.
Engage in Conversation:
Follow up with additional questions as needed, or type "quit" to exit the chat.
Additional Notes:

For larger PDF files, consider using a service like https://www.ilovepdf.com/compress_pdf to reduce their size before uploading.
Ensure your Astra DB database is configured to enable the "Search (Vector)" capability.
Feel free to customize the application further according to your specific needs and preferences.
