pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Build App'){
            agent {
                label 'k8s'
                }
            steps {
                ansiblePlaybook installation: 'ansible 2.9.17', inventory: 'k8s_hosts', playbook: 'my-python-app.yml'
            }
        }
        stage('Build FW'){
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
