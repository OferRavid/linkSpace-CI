pipeline {
    agent any
    stages {
        // stage('checkout') {
        //     steps {
        //         deleteDir()
        //         checkout scm
        //     }
        // }
        stage('docker-build') {
            steps {
                sh '''
                export DOCKER_HOST=127.0.0.1:8080
                cd application
                docker-compose build
                '''
            }
        }
        stage('e2e-test') {
            steps {
                sh "./scripts/e2e-test.sh"
            }
        }
        stage('tag') {
            steps {
                sh "exit 1"
            }
        }
        // stage('publish') {
        //     steps {
        //         sh "./scripts/publish2ecr.sh"
        //     }
        // }
        // stage('deploy') {
        //     steps {}
        // }
    }
    post{
        cleanup{
            sh "./scripts/cleanUp.sh"
        }
        always{
            echo "Job $env.JOB_NAME has finished."
        }
        success{
            echo "Build $env.BUILD_NUMBER was successful."
        }
        failure{
            echo "Build $env.BUILD_NUMBER has failed."
            // mail bcc: '', cc: '', from: 'no-reply@jenkins', replyTo: '',  
            //      body: """ Tests input in the atteched file.\nFor more information, check console output at 
            //      <a href="${env.BUILD_URL}">${env.JOB_NAME}</a>""",  subject: "Status of  ${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} ", 
            //      to: 'ofer.rvd@gmail.com'
            // emailext body: 'Check console output at $BUILD_URL to view the results. /n/n ${CHANGES} /n/n -------------------------------------------------- /n${BUILD_LOG, maxLines=100, escapeHtml=false}', 
            //         to: "ofer.rvd@gmail.com", 
            //         subject: 'Build failed in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER'
        }
    }
}