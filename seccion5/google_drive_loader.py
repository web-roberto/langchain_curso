#  pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
# accede a mi cuenta de Google Drive
# voy a google cloud console, creo un proyecto, API & Services. busco 'google drive'. Enable -> la habilita
# para este proyecto. Credentials. create credentials.oauth client.. Create Client OAuth.
# Desktop app -> Client ID, secret. Download json y lo bajo a mi carpeta. Tests. añado un usuario

from langchain_community.document_loaders import GoogleDriveLoader

#el fichero .json con las credenciales descargadas desde google drive
credentials_path = "C:\\Users\\santiago\\curso_langchain\\Tema 3\\credentials.json"
#ruta donde quiero que se guarde el token y nombre del fichero donde se guardará
token_path = "C:\\Users\\santiago\\curso_langchain\\Tema 3\\token.json"

loader = GoogleDriveLoader(
    folder_id="17DDwGPRjhjZhR6NRpegkFEmA4Wo6M_l3", ## en la url de una carpeta de mi drive está este id
    credentials_path=credentials_path,
    token_path=token_path,
    recursive=True
)

documents = loader.load()

print(f"Metadatos: {documents[0].metadata}")
print(f"Contenido: {documents[0].page_content}")