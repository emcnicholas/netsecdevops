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
                    args '-v $(pwd):/ftd-ansible/playbooks -v $(pwd)/hosts.yml:/etc/ansible/hosts playbooks/netsec-ngfw-config.yml'
                }
            }
        stage('Test URL'){
            steps{
                httpRequest ignoreSslErrors: true, responseHandle: 'NONE', url: 'http://54.237.88.112:30677', wrapAsMultipart: false
            }
        }
    }
}
