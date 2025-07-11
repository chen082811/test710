node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}

pipeline {
    agent any
    tools {
        sonar 'SonarScanner-4.8' // 对应 Global Tool Configuration 中的 Name
    }
    stages {
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube-Local') { // 对应 Configure System 中配置的 SonarQube 实例
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
