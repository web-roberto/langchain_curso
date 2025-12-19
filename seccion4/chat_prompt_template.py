from langchain_core.prompts import ChatPromptTemplate
# testeo un SISTEM CONTEXT y una pregunta básica  de HUMANO en ChatPromptTemplate.from_messages() y .format_messages()
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor del español al inglés muy preciso."),
    ("human", "{texto}")
])
mensajes = chat_prompt.format_messages(texto="Hola mundo, ¿cómo estás?")
for m in mensajes:
    print(f"{type(m)}: {m.content}")