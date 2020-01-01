pipeline {
agent any
    stages {
        stage('Init') {
            steps {
                bat label: '', script: 'cat /dev/null > Scores.txt' }
                    }
        stage('Build&Run') {
            steps { 
                bat label: '', script: 'cmd docker-run-command.txt'
                            }
            }
        stage('Test') {
            steps { 
                bat label: '', script: 'python C:\\Users\\nb\\PycharmProjects\\WorldOfGames\\test\\e2e.py' }
            }    
        stage('Finalize') {
            steps {
                bat label: '', script: 'docker container stop worldofgames_web_1' }
                } }
      }
      






pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/conshay/worldofgames/Kp25przd!.git' }
                    }   
        stage('build') {
            steps {
                bat label: 'Run', script: '''cd C:\\Users\\nb\\PycharmProjects\\WorldOfGames }
                    }
        stage('Run') {
            steps { 
                bat label: 'DockerUp', script: 'docker-compose up' }
            }
        stage('Test') {
            steps { 
                bat label: 'cdTestDir', script: '''cd C:\\Users\\nb\\PycharmProjects\\WorldOfGames\\test
                bat label: 'RunTest', script: 'python e2e.py' }
       
     }    
      }
    }



