pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Build NGFW') {
            steeps{
                sh 'docker run -v $(pwd)/projects/ftd-anisble:/ftd-ansible/playbooks -v $(pwd)/projects/ftd-anisble/hosts.yml:/etc/ansible/hosts ciscodevnet/ftd-ansible playbooks/netsec-ngfw-config.yml'
            }
        }
        stage('Test URL'){
            steps{
                httpRequest ignoreSslErrors: true, responseHandle: 'NONE', url: 'http://54.237.88.112:30677', wrapAsMultipart: false
            }
        }
    }
}
