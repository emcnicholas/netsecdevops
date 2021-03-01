pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Build NGFW') {
            agent {
                docker {
                    image 'ciscodevnet/ftd-ansible'
                }
            }
        stage('Test URL'){
            steps{
                httpRequest ignoreSslErrors: true, responseHandle: 'NONE', url: 'http://54.237.88.112:30677', wrapAsMultipart: false
            }
        }
    }
}
