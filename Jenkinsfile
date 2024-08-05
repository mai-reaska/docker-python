pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building....'
                sh '''
                    cd app
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing....'
                sh '''
                    cd app
                    python3 app.py
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment'
                sh '''
                echo "system will be deploy!"
                '''
            }
        }
    }
}
