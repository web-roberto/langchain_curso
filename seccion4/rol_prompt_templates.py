# PLANTILLAS BASADAS EN ROL GENÉRICO {rol} es una variable
#
# ChatPromptTemplate (especial para Chats) en lugar de PromptTemplate (más general)
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
# testeo un SISTEM CONTEXT y una pregunta básica en ChatPromptTemplate.from_messages() y .format_messages()

plantilla_sistema = SystemMessagePromptTemplate.from_template( # rol de SISTEMA (crea el contexto)
    "Eres un {rol} especializado en {especialidad}. Responde de manera {tono}"
)
plantilla_humano = HumanMessagePromptTemplate.from_template( # rol de usuario: una pregunta
    "Mi pregunta sobre {tema} es: {pregunta}"
)
chat_prompt = ChatPromptTemplate.from_messages([ #crea un chat con los roles de sistema y user
    plantilla_sistema,
    plantilla_humano
])
mensajes = chat_prompt.format_messages( # aquí paso variables a las plantillas.
    rol="nutricionista",
    especialidad="dietas veganas",
    tono="profesional pero accesible",
    tema="proteínas vegetales",
    pregunta="¿Cuáles son las mejores fuentes de proteína vegana para un atleta profesional?"
)
for m in mensajes:
    print(m.content)