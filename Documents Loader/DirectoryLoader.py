"""
DirectoryLoader is a document loader that reads multiple files from a folder (directory) and loads them all at once into Document format for LLM processing.
"""

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path= r'C:\Users\alisa\OneDrive\Desktop\RAG\books',
    glob= '*.pdf',
    loader_cls= PyPDFLoader
)

# docs= loader.load()

# # print(len(docs))

# print(docs[10].page_content)
# print(docs[10].metadata)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)