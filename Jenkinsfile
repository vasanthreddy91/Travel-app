pipeline {
    agent any

    stages {
        stage('checkout code') {
            steps {
               git branch: 'main', url: 'https://github.com/vasanthreddy91/Travel-app.git'
            }
        }

        stage('Build backend image') {
            steps {
                 dir('backend') {
                    sh 'docker build -t travel-backend .'
                }
            }    
        }

        stage('build frontend image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t travel-frontend .'
                }
            }
        }

        stage('run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}