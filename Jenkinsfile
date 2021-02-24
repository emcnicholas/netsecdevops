pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/emcnicholas/netsecdevops.git'
            }
        }
        stage('Deploy App') {
             steps {
                 script {
                     kubernetesDeploy configs: 'my-python-app-deployment.yml', kubeConfig: [path: ''], kubeconfigId: 'microk8s', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 }
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
