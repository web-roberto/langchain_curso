# aqui no llamo al LLM simplemente aprendo a crear un historial para condicionar la respuesta ante una pregunta.
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil que mantiene el contexto de la conversación."),
    MessagesPlaceholder(variable_name="historial"), #(1) METO AQUI EL HISTORIAL DE MENSAJES pasado en la variable 'historial'
    ("human", "Usuario: {pregunta_actual}") # pregunta pasado en la variable 'pregunta_actual'
])
# Simulamos un historial de conversación para determinar el resto de la conversacíon
historial_conversacion = [
    HumanMessage(content="Usuario: ¿Cuál es la capital de Francia?"),
    AIMessage(content="IA: La capital de Francia es París."),
    HumanMessage(content="Usuario: ¿Y cuántos habitantes tiene?"),
    AIMessage(content="IA: París tiene aproximadamente 2.2 millones de habitantes en la ciudad propiamente dicha.")
]
mensajes = chat_prompt.format_messages(
    historial=historial_conversacion, #(1) LE PASO EL HISTORIAL DE MENSAJES para determinar la pregunta siguiente:
    pregunta_actual="¿Puedes decirme algo interesante de su arquitectura?"
)
for m in mensajes:
    print(m.content)