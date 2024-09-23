#Kevin Sun
#Data Science 217
#09/21/2024

#1.GIT 

#Clone your forked repository to your local machine

#git clone https://github.com/UCSF-DataSci/ds-217-02-git-Kevinkidsss.git
#Create and switch to a new branch
#git checkout -b newbranch

#Create a `readme.md` file in the new branch
#echo "# This is the README file for the newbranch" > readme.md

#Add a copy of your python file from assignment 1 to the repo
#git add readme.md

#Stage and commit the files with a commit message
#git commit -m "Add Assignment 1.py and create readme.md"


#Merge your new branch back with the `main` branch
#git checkout main
#git merge newbranch

#Push your changes to GitHub
#git push origin newbranch


#2. Markdown
	#- Fill in your `readme.md` with the requested information from assignment 1

	#- Use formatting to separate sections using `# Header`'s

	#- Add a link to the official Python website (https://www.python.org)

#3. Python environments & packages
	#- Create a virtual environment
    #python -m venv myproject_env

	#- Activate the virtual environment
    #source myproject_env/bin/activate

	#- Add the directory of the virtual environment to `.gitignore` (commit to repo)
    #myproject_env/
    #git add .gitignore
    #git commit -m "Add virtual environment directory to .gitignore"

	#- Use `pip install` or `python -m pip install` to install a package (okay to use the example from lecture)
    #pip install requests

	#- Take a screenshot of the installation

	#- Add the screenshot to your assignment repository

#4. Markdown
	#- Add the screenshot image to your readme.md
    #![pip installation](C:\Users\kevin\OneDrive\Desktop\UCSF Fall 2024\Datasci 217\Intro to Python\hw\pip request.png "pip installation")
    #git add images/pip_request.png readme.md
    #git commit -m "Add pip request screenshot to readme.md"
    #git push origin main

	#- Add a meme you like from the internet to readme.md
    #![Meme](https://i0.wp.com/copyhackers.com/wp-content/uploads/2020/06/img_20200130_0253004222178807860404007.jpg?w=890&ssl=1)

	#- Commit and push changes back to GitHub

#5. Check your work on GitHub, you should now have:
	#- A single branch, `main`
	#- Python file from assignment 1
	#- `.gitignore` with at least one entry for the virtual environment folder
	#- `readme.md` with assignment 1 content, plus images
