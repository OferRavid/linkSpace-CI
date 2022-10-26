pipeline {
    agent any
    stages {
        stage('docker-build') {
            steps {
                sh '''
                cd application
                docker-compose build
                '''
            }
        }
        stage('e2e-test') {
            steps {
                echo "============== - E2E test on the application - ====================="  
                sh '''
                cd application
                docker-compose up -d
                ../scripts/wait4containers.sh 60
                #../scripts/e2e-test.sh
                '''
            }
        }
        stage('tag') {
            steps {
                script {
                    sh "git fetch --tags || true"
                    tags = sh(script: "git tag", returnStdout: true).trim()
                    if (tags.length() > 1) {
                        tag_tail = sh(script: "git describe  --abbrev=0  --tags", returnStdout: true).trim()
                        NEW_TAG=tag_tail.split('\\.')
                        NEW_TAG[2]=NEW_TAG[2].toInteger()+1
                        NEW_TAG=NEW_TAG.join('.')
                    }
                    else {
                        NEW_TAG='1.0.0'
                    }
                    
                }
                sh "./scripts/add_tag.sh ${NEW_TAG}"
            }
        }
        stage('publish') {
            steps {
                sh "./scripts/publish2ecr.sh ${NEW_TAG}"
            }
        }
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