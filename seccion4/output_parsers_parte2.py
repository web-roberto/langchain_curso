# MÉTODO MODERNO se usar Pydantic en LLM
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Resumen breve del texto.") ## la descripción es para que el LLM sepa de que trata el campo
    sentimiento: str = Field(description="Sentimiento del texto (Positivo, neutro o negativo)")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)
# La salida del LLM es el modelo pydantic que yo le digo en el programa y hace falta decírselo
# el usuario durante el diálogo
structured_llm = llm.with_structured_output(AnalisisTexto)
texto_prueba = "Me encantó la nueva película de acción, tiene muchos efectos especiales y emoción."
resultado = structured_llm.invoke(f"Analiza el siguiente texto: {texto_prueba}")
print(resultado.model_dump_json()) # dump_json() convierte de json a string para pintar