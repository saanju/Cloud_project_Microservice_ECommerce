pipeline {
    agent any

    stages {
        stage('Setup Docker Network') {
            steps {
                script {
                    echo 'Setting up Docker network...'
                    sh 'docker network create micro_network'
                }
            }
        }
        stage('Build and Run Frontend Service') {
            steps {
                script {
                    dir('frontend') {
                        echo 'Building frontend service...'
                        sh 'docker build -t frontend-srv .'
                        echo 'Running frontend service...'
                        sh 'docker run -p 5000:5000 --detach --name frontend-service --net=micro_network frontend-srv'
                    }
                }
            }
        }
        stage('Build and Run Order Service') {
            steps {
                script {
                    dir('order-service') {
                        echo 'Building order service...'
                        sh 'docker build -t order-srv .'
                        echo 'Running order service...'
                        sh 'docker run -p 5003:5003 --detach --name order-service --net=micro_network order-srv'
                    }
                }
            }
        }
        stage('Build and Run Product Service') {
            steps {
                script {
                    dir('product-service') {
                        echo 'Building product service...'
                        sh 'docker build -t product-srv .'
                        echo 'Running product service...'
                        sh 'docker run -p 5002:5002 --detach --name product-service --net=micro_network product-srv'
                    }
                }
            }
        }
        stage('Build and Run User Service') {
            steps {
                script {
                    dir('user-service') {
                        echo 'Building user service...'
                        sh 'docker build -t user-srv .'
                        echo 'Running user service...'
                        sh 'docker run -p 5001:5001 --detach --name user-service --net=micro_network user-srv'
                    }
                }
            }
        }
        stage('Deploy Frontend') {
            steps {
                script {
                    dir('frontend') {
                        echo 'Building frontend...'
                        sh 'docker-compose -f docker-compose.deploy.yml build'
                        echo 'Deploying frontend...'
                        sh 'docker-compose -f docker-compose.deploy.yml up -d'
                    }
                }
            }
        }
        stage('Database Setup') {
            steps {
                script {
                    echo 'Setting up databases...'
                    sh '''
                        docker exec -it corder-service flask db init
                        docker exec -it corder-service flask db migrate
                        docker exec -it corder-service flask db upgrade
                        docker exec -it cproduct-service flask db init
                        docker exec -it cproduct-service flask db migrate
                        docker exec -it cproduct-service flask db upgrade
                        docker exec -it cuser-service flask db init
                        docker exec -it cuser-service flask db migrate
                        docker exec -it cuser-service flask db upgrade
                    '''
                }
            }
        }
        stage('Final Steps') {
            steps {
                script {
                    echo 'Performing final steps...'
                    sh '''
                        curl -i -d "name=cleansers&slug=cleansers&image=product4.jpg&price=100" -X POST localhost:5002/api/product/create
                        curl -i -d "name=perfume&slug=perfume&image=product5.jpg&price=200" -X POST localhost:5002/api/product/create
                        mysql --host=127.0.0.1 --port=32000 --user=ccproject --password=pfm_2020 -e "show databases; use user; show tables; select * from user; exit"
                        mysql --host=127.0.0.1 --port=32002 --user=ccproject --password=pfm_2020 -e "show databases; use order; show tables; select * from order.order; select * from order.order_item; exit"
                    '''
                }
            }
        }
    }
}
