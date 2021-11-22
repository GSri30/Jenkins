pipeline { 
    agent any
    stages {
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