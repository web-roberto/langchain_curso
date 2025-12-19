# MÉTDO ANTIGUO se usar Pydantic en LLM
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    activo: bool = True
data = {"id": "123", "nombre": "Ana"}
usuario = Usuario(**data)
print(usuario.model_dump_json())  # dump_json() convierte de json a string para pintar