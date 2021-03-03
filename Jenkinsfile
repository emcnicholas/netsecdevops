pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Build Dev NGFW') {
            steps{
                sh 'docker run -v $(pwd):/ftd-ansible/playbooks -v $(pwd)/hosts.yml:/etc/ansible/hosts ciscodevnet/ftd-ansible playbooks/netsec-ngfw-config.yml'
            }
        }
        stage('Test URL'){
            steps{
                httpRequest ignoreSslErrors: true, responseHandle: 'NONE', url: 'http://54.237.88.112:30677', wrapAsMultipart: false
            }
        }
        stage('Build Prod NGFW') {
            steps{
                sh 'docker run -v $(pwd):/ftd-ansible/playbooks -v $(pwd)/prod_hosts.yml:/etc/ansible/hosts ciscodevnet/ftd-ansible playbooks/netsec-ngfw-config.yml'
            }
        }
    }
}
