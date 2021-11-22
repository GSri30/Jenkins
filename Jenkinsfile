pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/GSri30/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x program.py"
                sh "./program.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}