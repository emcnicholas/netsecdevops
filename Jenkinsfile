pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Execute Ansible'){
            steps{
                ansiblePlaybook disableHostKeyChecking: true, installation: 'ansible 2.9.17', inventory: 'hosts.yml', playbook: 'netsec-ngfw-config.yml'
            }
        }
        stage('Test URL'){
            steps{
                httpRequest ignoreSslErrors: true, responseHandle: 'NONE', url: 'http://54.237.88.112:30677', wrapAsMultipart: false
            }
        }
    }
}
