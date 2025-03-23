from src.index import loadpdf_file, txt_split, download_hug_face_embeddings
from pinecone.grpc import PineConeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_APIKEY = os.environ.get('PINECONE_APIKEY')
os.environ['PINECONE_APIKEY']=PINECONE_APIKEY


extracted_data= loadpdf_file(data='Data/')
text_chunks= txt_split(extracted_data)
embeddings = download_hug_face_embeddings()

pc = Pinecone(api_key=PINECONE_APIKEY)

index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)


docsearch = PineconeVectorStore.from_documents(
    docs=text_chunks,
    index_name=index_name,
    embedding=embeddings,
    )


