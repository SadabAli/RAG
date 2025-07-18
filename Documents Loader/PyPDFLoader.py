from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader(r'C:\Users\alisa\OneDrive\Desktop\RAG\test.pdf')

docs = loader.load()
print(len(docs))

print(docs[10].page_content)
print(docs[1].metadata)