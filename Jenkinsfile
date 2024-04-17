pipeline {
    agent any

    tools {
        dockerTool 'Docker' // Use the Docker tool configured in Jenkins
    }

    environment {
        DOCKER_IMAGE = 'sanj27/user-srv:latest'
        DOCKER_CONTAINER_NAME = 'user-srv-container'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    docker.build DOCKER_IMAGE
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run Docker container
                    docker.run("--name ${DOCKER_CONTAINER_NAME} -p 8080:8080 ${DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests (replace this with actual test commands)
                    echo 'Running tests...'
                  
                }
            }
        }

      
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
