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
                		call venv\\Scripts\\activate && pip install -r requirements.txt
               			'''
            		}
        	}

		stage('Code Quality') {
            		steps {
                		bat '''
                		call venv\\Scripts\\activate && flake8 app.py test_app.py || exit 1
                		'''
            		}
       		}

        	stage('Test') {
            		steps {
                		bat '''
                		call venv\\Scripts\\activate && pytest test_app.py --cov=app --cov-report=xml || exit 1
                		'''
            		}
        	}

        	stage('Check Coverage') {
            		steps {
                		bat '''
                		call venv\\Scripts\\activate && coverage report --fail-under=80 || exit 1
                		'''
            		}
        	}

        	stage('Formatting Check') {
            		steps {
                		bat '''
                		call venv\\Scripts\\activate && black --check . || exit 1
                		'''
            		}
        	}
       	}
}