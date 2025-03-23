# End-to-End Medical ChatBot 

# How to run?
### STEPS:

*Create and Clone the GitHub Repository*

```bash
git clone <https://github.com/iamrudro/MediBot.git>
```

#### STEP 1 - Check for Anaconda installation on local machine and then Create a Conda environment after opening the Repo

```bash
conda create -n medibot python=3.10 -y
```

```bash
source activate base
```

```bash
conda activate medibot
```

### STEP 2 - Install the requirements
```bash
pip install -r requires.txt
```
```
pip list
```

### STEP 3 -  Project Folder Structure - ```template.py```

This *template* Python file helps in creating folder or files automatically and reduces hassle

```bash
python template.py
```

### STEP 3 -  Setting up Local Package
1. Create ```setup.py``` file
2. ```-e .``` add this command to requires.txt
3. Again install the 'requires'
4. ```bash pip install -r requires.txt```
5. .egg-info folder is created 
6. Now the project has been setup has the local Package


### STEP 4 - Jyputer Notebook Implementation
1. Select Kernel -> medibot
2. Extract Data from Pdf
3. Create Chunks
4. Downloading an Embedding model from Hugging Face
    - [MODEL: all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
    - This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.
    - Using this model becomes easy when you have sentence-transformers installed: ```pip install -U sentence-transformers```
5. Testing if the Model can convert the sentence into Vector Embedding
6. Initialize PineCone Vector Database
    - Create an API Key
    - Paste the API in the .env file
7. Create Index for PineCone Database
8. 
9. 

### Basic Git Commands
- git add .
- git commit -m "message"
- git push origin main
- git log
- git status