from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://techmind.ac/") #carga la parte estática de una web, no la parte dinámica
docs = loader.load()
print(docs)