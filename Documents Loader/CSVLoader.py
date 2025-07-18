from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r'C:\Users\alisa\OneDrive\Desktop\RAG\restaurants.csv')

docs = loader.load()

print(len(docs))
print(docs[1]) # for 2nd row