# labs-ML-Human-Activity-Recognition
AWS Machine Learning using cell phone sensor data for Human Activity Recording

Requires:
- AWS SDK for python (boto3) installation
- local copy of "./record.csv" file (local to where you run ml.py python script from)

Script modifications (for individual student environment includes)
- Substitution in Script for their actual values:
- AWS_ACCESS_KEY_ID 
- AWS_SECRET_ACCESS_KEY
- MODEL_ID
- us-east-1 (confirm region is set to us-east-1, ML is not supported in the "normal" us-west-2 or many other regions for that matter)

Make sure
- Grab the correct model ID (easy to grab an evaluation ID)
- The real-time endpoint is enabled for your model (done w/in the ML console, actual endpoint is fetched via the SDK API call)
