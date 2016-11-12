project0:
	jupyter notebook  projects/titanic_survival_exploration/Titanic_Survival_Exploration.ipynb

project1:
	jupyter notebook projects/boston_housing/boston_housing.ipynb

project2:
	jupyter notebook projects/student_intervention/student_intervention.ipynb

install:
	brew install python
	brew install homebrew/python/scipy
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
