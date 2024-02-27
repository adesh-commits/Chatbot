LLM-PDF QA SEARCH ENGINE🔍
This app is an LLM-powered PDF chatbot that can answer questions based on the content of uploaded PDF documents. It uses Streamlit for the user interface, LangChain for text processing and indexing, OpenAI for language modeling and embeddings, and Astra DB for data storage and retrieval.

Installation
To run this app, you need to have Python 3.6 or higher installed on your system. You also need to install the following packages and libraries:

streamlit
streamlit_extras
PyPDF2
langchain
langchain_openai
langchain_vectorstores
langchain_indexes
langchain_llms
langchain_embeddings
cassio
typing_extensions
You can install them using pip:

pip install -r requirements.txt

You also need to have an account on OpenAI and Astra DB, and obtain the API keys and tokens for accessing their services. You need to enter these credentials in the app when prompted.

Usage
To launch the app, run the following command in your terminal:

streamlit run app.py

This will open a web browser window where you can interact with the app. You can upload a PDF file of your choice, and then ask questions about its content. The app will use the LLM model to generate relevant answers, and also show you the most similar documents from the PDF file based on your query.

You can also adjust some settings in the sidebar, such as the title, the description, and the author of the app.

Output
Here is an example of the output of the app when uploading a PDF file about Python programming and asking some questions about it:

!Output

Contributing
If you want to contribute to this project, you are welcome to do so. You can report issues, request features, or submit pull requests on the GitHub repository.

Please follow the code of conduct and the license of this project.

Acknowledgements
This project was inspired by the PDF Search Engine project by Abhinav Jain.

This project also uses the following resources and tools:

Streamlit - The fastest way to build and share data apps
LangChain - A Python library for natural language processing and indexing
OpenAI - A powerful language model for text generation and embeddings
Astra DB - A scalable and secure cloud database service
Streamlit Extras - A collection of useful components and utilities for Streamlit
PyPDF2 - A Python library to manipulate PDF files
Cassio - A Python library to interact with Astra DB
