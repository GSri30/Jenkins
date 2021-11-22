pipeline { 
    agent any
    stages {
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 program.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}