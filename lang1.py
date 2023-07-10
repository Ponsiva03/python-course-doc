import faiss
import pickle
import pandas as pd
import os
from langchain.chains import VectorDBQAWithSourcesChain
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

chain = VectorDBQAWithSourcesChain.from_llm(llm=None, vectorstore=store)

folder_name = input("Enter the folder name (where your test files reside): ")

file_names = os.listdir(folder_name)

df = pd.DataFrame(columns=["File Name", "Answer", "Grantor", "Grantee"])

for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, encoding="utf8") as file:
        contents = file.read()

    result = chain({"question": contents})
    answer = result['answer']
    grantor = ""  # Replace with your logic to extract grantor name
    grantee = ""  # Replace with your logic to extract grantee name

    df = df.append({"File Name": file_name, "Answer": answer, "Grantor": grantor, "Grantee": grantee},
                   ignore_index=True)

csv_file = "output.csv"
df.to_csv(csv_file, index=False)

print(f"Results saved to {csv_file}")
