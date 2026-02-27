// pipeline {
//     agent any

//     stages {

//         stage('Print Student Info') {
//             steps {
//                 sh '''
//                 echo "======================================"
//                 echo "Name: RALLAPALLI V S B HARSHITH"
//                 echo "Roll No: 2022BCS0042"
//                 echo "======================================"
//                 '''
//             }
//         }

//         stage('Create Virtual Environment') {
//             steps {
//                 sh 'python3 -m venv venv'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 sh '''
//                 ./venv/bin/pip install --upgrade pip
//                 ./venv/bin/pip install -r requirements.txt
//                 '''
//             }
//         }

//         stage('Run Training Script') {
//             steps {
//                 sh '''
//                 ./venv/bin/python train.py
//                 '''
//             }
//         }

//         stage('Print Completion Message') {
//             steps {
//                 sh '''
//                 echo "======================================"
//                 echo "Model training completed successfully!"
//                 echo "Name: RALLAPALLI V S B HARSHITH"
//                 echo "Roll No: 2022BCS0042"
//                 echo "======================================"
//                 '''
//             }
//         }
//     }
// }



pipeline {
    agent any

    environment {
        IMAGE_NAME = "harsh994/ml-model:latest"
        CONTAINER_NAME = "ml-test-container"
        PORT = "8000"
    }

    stages {

        stage('Print Student Info') {
            steps {
                sh '''
                echo "======================================"
                echo "Name: RALLAPALLI V S B HARSHITH"
                echo "Roll No: 2022BCS0042"
                echo "======================================"
                '''
            }
        }

        stage('Pull Docker Image') {
            steps {
                sh "docker pull ${IMAGE_NAME}"
            }
        }

        stage('Run Container') {
            steps {
                sh """
                docker run -d -p ${PORT}:8000 \
                --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }

        stage('Wait for API Readiness') {
            steps {
                script {
                    timeout(time: 60, unit: 'SECONDS') {
                        waitUntil {
                            def status = sh(
                                script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:${PORT}/health",
                                returnStdout: true
                            ).trim()
                            return (status == "200")
                        }
                    }
                }
            }
        }

        stage('Send Valid Inference Request') {
            steps {
                script {
                    def response = sh(
                        script: "curl -s -X POST http://localhost:${PORT}/predict -H 'Content-Type: application/json' -d @valid_input.json",
                        returnStdout: true
                    ).trim()

                    echo "Valid API Response: ${response}"

                    if (!response.contains("prediction")) {
                        error("Prediction field missing in valid response!")
                    }
                }
            }
        }

        stage('Send Invalid Request') {
            steps {
                script {
                    def status = sh(
                        script: "curl -s -o /dev/null -w '%{http_code}' -X POST http://localhost:${PORT}/predict -H 'Content-Type: application/json' -d @invalid_input.json",
                        returnStdout: true
                    ).trim()

                    echo "Invalid Request Status Code: ${status}"

                    if (status == "200") {
                        error("Invalid input incorrectly returned 200!")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Final Result') {
            steps {
                echo "All validations passed successfully!"
            }
        }
    }

    post {
        always {
            sh "docker stop ${CONTAINER_NAME} || true"
            sh "docker rm ${CONTAINER_NAME} || true"
        }

        success {
            echo "======================================"
            echo "PIPELINE PASSED"
            echo "======================================"
        }

        failure {
            echo "======================================"
            echo "PIPELINE FAILED"
            echo "======================================"
        }
    }
}
