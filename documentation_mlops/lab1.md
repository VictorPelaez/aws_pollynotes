task 1. update the step functions state machine

f1.png with graph about state machine definition

In cloud 9 the repository od State Machine

clone git clone https://git-codecommit.us-west-2.amazonaws.com/v1/repos/stateMachineCode-e541729fa11d4f2bafa7fa20da053868

Modify the manager py
```python
# Create a step that invokes an AWS Lambda function that tests if the endpoint is InService
endpoint_wait_step = steps.LambdaStep(
    "Test endpoint in service", # Step name
    parameters={
        "FunctionName": endpoint_wait_lambda, # Lambda function variable, defined ~ line 40
        "Payload":{
            "Input.$":"$" # Pass all the state machine data to Lambda event
        }
    },
    result_path='$.endpoint_wait_step_result' # Pass results to output
)
```

and 
# Create a retry configuration for the endpoint_wait_step
endpoint_wait_step_retry = stepfunctions.steps.states.Retry(
    error_equals=['NotInService'], # Error defined by Lambda function
    interval_seconds=15, # Time to wait between attempts
    max_attempts=30, # Max times to try
    backoff_rate=1.25 # How much to increase time between attempts on fail
)
# Add a retry configuration to the endpoint_wait_step
endpoint_wait_step.add_retry(endpoint_wait_step_retry)

## definition workflow

# Chain the steps together to generate a full AWS Step Functions
workflow_definition = steps.Chain([
    training_step,
    model_step,
    register_artifact_step,
    endpoint_config_step,
    endpoint_step,
    endpoint_wait_step, # Add the endpoint wait step
    model_test_step # Add the model test step
])
