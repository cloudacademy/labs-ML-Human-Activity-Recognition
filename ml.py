import boto3

from boto3.session import Session

session = Session(aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY')

machinelearning = session.client('machinelearning', region_name='us-east-1')

model_id = 'MODEL_ID'

labels = {'1': 'walking', '2': 'walking upstairs', '3': 'walking downstairs', '4': 'sitting', '5': 'standing', '6': 'laying'}

try:

    model = machinelearning.get_ml_model(MLModelId=model_id)

    prediction_endpoint = model.get('EndpointInfo').get('EndpointUrl')

    with open('record.csv') as f:

        record_str = f.readline()

    record = {}

    for index,val in enumerate(record_str.split(',')):

        record['Var%03d' % (index+1)] = val

    response = machinelearning.predict(MLModelId=model_id, Record=record, PredictEndpoint=prediction_endpoint)

    label = response.get('Prediction').get('predictedLabel')

    print("You are currently %s." % labels[label])

except Exception as e:

    print(e)
