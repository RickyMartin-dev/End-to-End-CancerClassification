# End-to-End-CancerClassification
With MLFlow and DVC, Deployed

## Workflows
1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config 
6. Update the componenents
7. Update the pipleine 
8. Update the main.py
9. Update the dvc.yaml

### Model
Using VGG16 (more info: https://keras.io/api/applications/)

### MLFlow Integration
MLFlow for tracking model version during different iterations/hyperparameter settings.

## DVC Integration
Git + DVC assists in tracking pipeline and ensure work does not have to be repeated.