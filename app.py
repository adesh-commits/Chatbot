import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import cassio
from typing_extensions import Concatenate



# Sidebar contents
with st.sidebar:
    st.title('LLM-PDF QA SEARCH ENGINE🔍')
    st.markdown('''
    ## About
    This app is an LLM-powered PDF chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    - [Astra DB](https://docs.datastax.com/en/astra/astra-db-vector/index.html)
    
    LLM-PDF-Chatbot is a technical solution utilizing LangChain and OpenAI's LLM model for extracting insights and answering questions from PDF documents. It leverages Streamlit for the user interface and integrates with Cassandra for storing and indexing text data. The purpose of this project is to provide users with an interactive platform to ask questions and receive relevant answers based on the content of uploaded PDF documents, powered by advanced language processing capabilities.

    ''')
    add_vertical_space(4)
    st.write('Made with ❤️ by [Adesh](https://www.linkedin.com/in/adesh-sabari-loganathan-765770223/)')


ASTRA_DB_APPLICATION_TOKEN = st.text_input('Enter your ASTRA_DB_APPLICATION_TOKEN👇🏻') # enter the "AstraCS:..." string found in in your Token JSON file
ASTRA_DB_ID = st.text_input('Enter your ASTRA_DB_ID👇🏻')# enter your Database ID

OPENAI_API_KEY =  st.text_input('Enter your OpenAI API key👇🏻')
def main():
    st.header("Chat with your PDF  ")


    st.write('If your PDF exceeds the limit then 👉🏻 [use this](https://www.ilovepdf.com/compress_pdf)')

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')


    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        raw_text = ''
        for i, page in enumerate(pdf_reader.pages):
            content = page.extract_text()
            if content:
                raw_text += content

        # st.write(text)
        cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)
        llm = OpenAI(openai_api_key=OPENAI_API_KEY)
        embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        astra_vector_store = Cassandra(
            embedding=embedding,
            table_name="qa_mini_demo",
            session=None,
            keyspace=None,
        )

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

        #st.write(texts)

        astra_vector_store.add_texts(texts[:50])
        astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

        first_question = True
        while True:
            if first_question:
                query_text = st.text_input("Ask questions about your PDF file:").strip()
            else:
                query_text = st.text_input("What's your next question (or type 'quit' to exit): ").strip()
            if query_text.lower() == "quit":
                break
            if query_text == "":
                continue

            first_question = False
            st.write("\nQUESTION: \"%s\"" % query_text)
            answer = astra_vector_index.query(query_text, llm=llm).strip()
            st.write("ANSWER: \"%s\"\n" % answer)

            st.write("FIRST DOCUMENTS BY RELEVANCE:")
            for doc, score in astra_vector_store.similarity_search_with_score(query_text, k=4):
                st.write("    [%0.4f] \"%s ...\"" % (score, doc.page_content[:84]))







if __name__ == '__main__':
    main()
