import os
# from langchain_openai import AzureChatOpenAI
# import langchain
from dotenv import load_dotenv
load_dotenv()
import pickle
from fastapi.middleware.cors import CORSMiddleware
# -------PDF UPLOAD ISTARTS---------
# from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

# # -----PDF IMPORTS STARTS--------
# from langchain_openai import AzureOpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain.chains import VectorDBQA
# from langchain_openai import AzureOpenAI
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# # -----PDF IMPORTS END--------
# openai_apiverson=os.environ["AZURE_OPENAI_VERSION"] 
# openai_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"] 
# openai_apikey=os.environ["AZURE_OPENAI_API_KEY"] 
# openai_model_name=os.environ["MODEL_DEPLOY_NAME"]
# embed_model=os.environ["EMBED_MODEL_NAME"]
# embed_deploy_name=os.environ["EMBED_DEPLOY_MODEL_NAME"]
# embed_endpoint=os.environ["EMBED_ENDPOINT"]

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"]
)


# model=AzureChatOpenAI(
#     openai_api_version=openai_apiverson,
#     azure_deployment=openai_model_name,
#     )
@app.get("/")
async def basic():
    return({"Hello"})
    
# @app.get("/ask")
# async def ask(prompt=""):
#     result=model.invoke([prompt])
#     return({"response":result["content"]})


# UPLOADED_FILE_NAME=""
# file_path=os.getenv("file_path")
# # UPLOAD YOUR FILE AND USE IT
# @app.post("/uploadfile")
# async def upload(file: UploadFile = File(...)):
#     try:
#         # Read the content of the file
#         contents = await file.read()
#         # Save the file to disk
#         with open(file.filename, 'wb') as f:
#             f.write(contents)
#             UPLOADED_FILE_NAME=file.filename
#             with open(file_path, 'wb') as file:
#                 # Serialize and write the variable to the file
#                 pickle.dump(UPLOADED_FILE_NAME, file)

#     except Exception as e:
#         # More specific error reporting
#         return JSONResponse(status_code=500, content={"message": f"There was an error uploading the file: {str(e)}"})
#     finally:
#         # Ensure the file is always closed after operations
#         await file.close()
#     return {"message": f"Successfully uploaded {file.filename}"}

# loaded_data = ""
# @app.get("/rag")
# async def rag(query=""):
#             # # loading--------------
#             # Open the file in binary mode
#             with open(os.getenv("file_path"), 'rb') as file:
#                 # Deserialize and retrieve the variable from the file
#                 loaded_data = pickle.load(file)
#             print(loaded_data)
#             fileloader=PyPDFLoader("./"+loaded_data)
#             documents=fileloader.load() 
#             # # chunking ---------
#             text_splitter=CharacterTextSplitter(chunk_size=800,chunk_overlap=20)
#             texts=text_splitter.split_documents(documents) 
#             # embeddings-------------
#             embeddings= AzureOpenAIEmbeddings(
#             model=embed_model,
#             azure_deployment=embed_deploy_name,
#             azure_endpoint=embed_endpoint,
#             openai_api_key=openai_apikey,
#             openai_api_version=openai_apiverson
#             )
#             db=Chroma.from_documents(texts,embeddings)
#             docs = db.similarity_search(query,k=1)
#             # print(docs)
#             # text generation------------------------
#             result=model.invoke([docs[0].page_content])
#             return({"response":result["content"]})
