import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from template import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

load_dotenv()


def get_pdf_text(docs):
    text = ""
    for doc in docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(raw_text):
    text_chunks = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chuncks = text_chunks.split_text(raw_text)
    return chuncks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = OpenAI(temperature=0.2)
    memo = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memo
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True
            )


def main():
    st.set_page_config(page_title="PDF Reader", page_icon="📚")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        # st.session_state.conversation = st.empty()
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("PDF Reader 📚")
    user_question = st.text_input("Ask me anything regarding your file")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader(
            "Upload your PDF file and click on 'Analyze'", accept_multiple_files=True
        )
        if st.button("Analyze"):
            with st.spinner("Analyzing your file..."):
                # Get pdf text
                raw_text = get_pdf_text(docs)
                # st.write(raw_text)

                # Get pdf metadata/chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                # Creater vector store
                vectorstore = get_vectorstore(text_chunks)

                # Conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)


main()
