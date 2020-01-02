pipeline {
agent any
    stages {
        stage('Build&Run') {
            steps { 
                bat label: '', script: 'docker-compose -f C:\\Users\\nb\\PycharmProjects\\WorldOfGames\\docker-compose.yml up -d'
                            }
            }
        stage('Test') {
            steps { 
                bat label: '', script: 'python C:\\Users\\nb\\PycharmProjects\\WorldOfGames\\test\\e2e.py' }
            }    
        stage('Finalize') {
            steps {
                bat label: '', script: 'docker container stop worldofgames_web_1' }
                }
      }