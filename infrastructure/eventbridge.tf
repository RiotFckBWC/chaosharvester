resource "aws_cloudwatch_event_rule" "chaos_trigger" {
  name                = "chaosharvester_schedule"
  schedule_expression = "rate(5 minutes)"
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.live_run.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.chaos_trigger.arn
}

resource "aws_cloudwatch_event_target" "trigger_lambda" {
  rule      = aws_cloudwatch_event_rule.chaos_trigger.name
  target_id = "LiveRunTrigger"
  arn       = aws_lambda_function.live_run.arn
}