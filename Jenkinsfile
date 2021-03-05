pipeline {
  environment {
  IBM_CLOUD_REGION = 'us-south'
  IKS_CLUSTER = 'c0uvrhfd0v1b3bd432lg'
  registry = "srirammk18/flask-k8s"
  registryCredential = 'dockerhub_id'
  dockerImage = ''
  }
  agent any 
  stages {
    stage('Authenticate with IBM Cloud CLI') {
      steps {
        sh '''
            ibmcloud login --apikey ${IBM_API_KEY} -r "${IBM_CLOUD_REGION}" -g Default
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            '''
      }
    }
    stage('Deploy to IKS') {
      steps {
        sh '''
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            kubectl config current-context
            export BUILD_NUMBER=$BUILD_NUMBER
            kubectl apply -f service.yml
            kubectl apply -f ingress.yml
            kubectl apply -f db-deploy.yml
            kubectl apply -f db-service.yml
            kubectl apply -f persistentvolume.yml
            kubectl apply -f pvc.yml
            kubectl apply -f py-service.yml
            kubectl apply -f deployment.yml
            '''
      }
    }
  }
}
