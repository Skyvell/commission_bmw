from aws_cdk import (
    aws_lambda,
    aws_sqs,
    Stack,
    aws_rds
)
from aws_cdk.aws_lambda_event_sources import SqsEventSource
from constructs import Construct


class CalculationStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        # Initialise sqs queue for incomming data.
        sqs = aws_sqs.Queue(self, "sqs")

        # Initialise calculation lambda.
        lambda_ = aws_lambda.Function(
            scope = self, 
            id = "calculations-handler", 
            code = aws_lambda.Code.from_asset("resources/lambda"),
            handler = "calculations.handler",
            runtime = aws_lambda.Runtime.PYTHON_3_11
        )

        # Add sqs queue as eventsource for my calculations lambda.
        lambda_.add_event_source(SqsEventSource(sqs))