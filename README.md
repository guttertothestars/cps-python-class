
🎓 CPS Python Class Workspace
This repository is configured for a two-semester Python course, utilizing a central GitHub repository (cps-python-class) and a linked utility library (walkertools).

🚀 Daily Workflow: Sit Down & Code
Run these every time you start working on a "new" computer or one you haven't used in a few days.
1. Sync the Code

# Get the latest class assignments
git pull

# Get the latest version of your utility tools
git submodule update --remote --merge


2. Environment Check
If you see (.venv) in your terminal prompt, skip this. If not:
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate



💻 New Computer Initial Setup
Run these only once per computer to "build" the local environment.

# 1. Clone the repo and the tools at once
git clone --recursive https://github.com/guttertothestars/cps-python-class.git

# 2. Move into the directory
cd cps-python-class

# 3. Create the 'bubble' (Virtual Environment)
python -m venv .venv

# 4. Install the 'Blueprint' (Libraries)
# (Ensure environment is activated first - see Daily Workflow above)
pip install -r requirements.txt



🛠 Managing 'walkertools' Updates
Follow this sequence if you edit code inside the walkertools folder.
Step A: Push changes to the Library Repo

cd walkertools
git add .
git commit -m "Update utility tools"
git push origin main
cd ..


Step B: Update the Class Repo Pointer
Bash


git add walkertools
git commit -m "Sync class repo with latest walkertools"
git push origin main



💾 Saving Your Progress
Run these before you leave the computer to ensure your work is in the cloud.
# 1. Update the library 'blueprint' (only if you installed new pip packages)
pip freeze > requirements.txt

# 2. Stage all changes
git add .

# 3. Save and Send
git commit -m "Brief description of work completed"
git push origin main



🔍 Troubleshooting Tips
"Is the environment active?": Look for (.venv) at the start of your command line prompt.
"Submodule folder is empty": Run git submodule update --init --recursive.
"Git error: modified content": If you edited walkertools files, you must commit inside that folder before Git will let you commit in the main folder.


