pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Get User Info'){
            steps{
                sh '''whoami
                pwd'''
            }
        stage('Execute Ansible'){
            steps{
                ansiblePlaybook become: true, becomeUser: 'ubuntu', colorized: true, disableHostKeyChecking: true, installation: 'ansible 2.9.17', inventory: 'hosts.yml', playbook: 'netsec-ngfw-config.yml'
            }
        }
    }
}
