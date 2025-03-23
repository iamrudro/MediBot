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


### Basic Git Commands
- git add .
- git commit -m "message"
- git push origin main
- git log
- git status