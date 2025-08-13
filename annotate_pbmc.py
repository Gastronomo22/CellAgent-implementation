# --- Example usage (comment/uncomment as needed) ----------------------------
# Esempio di utilizzo semplice in Google Colab

# 1. Carico il dataset
filename = "pbmc.h5ad"
import scanpy as sc
adata = sc.read_h5ad(filename)
print(f"Dataset loaded: {adata.n_obs} cells, {adata.n_vars} genes.")

# 2. Configuro l'API OpenAI
from google.colab import userdata
from openai import OpenAI
api_key = userdata.get("API-KEY")
if not api_key:
    raise RuntimeError("API key mancante in Colab userdata")
client = OpenAI(api_key=api_key)

# 3. Definisco il task
user_task = "Annotate the cell types in the dataset."
dataset_description = "Human peripheral blood mononuclear cells (PBMC), single-cell RNA-seq."
available_tools = ["Scanpy", "CellTypist", "ScType"]

# 4. Eseguo la pipeline
from cellagent_core import run_cellagent_task  # Assicurati che sia nello stesso folder o nel PYTHONPATH

results = run_cellagent_task(
    user_task=user_task,
    dataset_description=dataset_description,
    available_tools=available_tools,
    steps_to_run=None,       # Esegue tutti gli step
    trials_per_step=2,       # Due tentativi per step
    user_goal="accurate result"
)

# 5. Stampo i risultati
print("\n\nFinal selected code per step:")
for r in results:
    print(f"\nStep {r.step}: {r.title}")
    print(r.code)
    print("Justification:", r.justification)
