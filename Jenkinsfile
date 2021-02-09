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
                ansiblePlaybook disableHostKeyChecking: true, installation: 'ansible 2.9.17', inventory: '/var/lib/jenkins/workspace/test/hosts.yml', playbook: '/var/lib/jenkins/workspace/test/netsec-ngfw-config.yml'
            }
        }
    }
}
