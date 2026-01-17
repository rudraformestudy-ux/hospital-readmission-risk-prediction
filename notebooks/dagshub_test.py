import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/RitamRixx/hospital-readmission-risk-prediction.mlflow")

dagshub.init(repo_owner='RitamRixx', repo_name='hospital-readmission-risk-prediction', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
