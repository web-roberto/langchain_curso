from langchain_core.prompts import PromptTemplate #PromptTemplate es general y ChatPromptTemplate (especial para Chats)
# comprobar su un prompt y una plantilla de una sóla linea  funciona antes de usarla en el LLM
# creo el contexto como prompt de sistema: "Eres un experto en marketing" y doy una instrucción básica como user
# con .format() -> no llama al LLM, simplemente muestra el template cambiando la variable por el valor dado
template = "Eres un experto en marketing. Sugiere un eslogan creativo para un producto {producto}"
prompt = PromptTemplate(
    template = template,
    input_variables=["producto"]
)
prompt_lleno = prompt.format(producto="café orgánico")
print(prompt_lleno)