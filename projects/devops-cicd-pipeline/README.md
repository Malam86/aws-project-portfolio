# DevOps CI/CD Pipeline

**Purpose:** Automate build, test, and deployment of applications to AWS environments.

**Services Used:**
- AWS CodePipeline
- AWS CodeBuild
- AWS CodeDeploy
- CloudFormation
- S3 (Artifact storage)
- Lambda (Custom hooks)

**Implementation Steps:**
1. Configure source stage using GitHub or CodeCommit.
2. Set up CodeBuild projects for compiling and testing code.
3. Deploy applications using CodeDeploy.
4. Use CloudFormation templates to provision environments.
5. Automate notifications with SNS.

**Programmatic Elements:**
- YAML/JSON CloudFormation templates
- CodeBuild and CodePipeline scripts
- Lambda hooks for custom deployment logic
