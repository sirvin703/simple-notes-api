pipeline {
	agent any

	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
		
		stage('Setup Environment') {
            		steps {
                		bat '''
                		python -m venv venv
                		venv\\Scripts\\activate
                		pip install --upgrade pip
               			pip install -r requirements.txt
               			'''
            		}
        	}

		stage('Code Quality') {
            		steps {
                		bat '''
                		venv\\Scripts\\activate
                		flake8 app.py tests/
                		'''
            		}
       		}

        	stage('Test') {
            		steps {
                		bat '''
                		venv\\Scripts\\activate
                		pytest --cov=app --cov-report=xml
                		'''
            		}
        	}

        	stage('Check Coverage') {
            		steps {
                		bat '''
                		venv\\Scripts\\activate
                		coverage report --fail-under=80
                		'''
            		}
        	}

        	stage('Formatting Check') {
            		steps {
                		bat '''
                		venv\\Scripts\\activate
                		black --check .
                		'''
            		}
        	}

        	stage('Build') {
            		steps {
                		bat '''
                		venv\\Scripts\\activate
                		python app.py
                		'''
            		}
        	}
	}
}