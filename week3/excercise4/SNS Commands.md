### Creating SNS Topic 
```
aws sns create-topic --name <TOPIC NAME>
```

### Adding email to topic
```
aws sns subscribe --topic-arn <SNS TOPIC ARN> \
--protocol email --notification-endpoint <YOUR EMAIL ADDRESS>
```

### Create CloudWatch alarm
```
aws cloudwatch put-metric-alarm --alarm-name DDB-UserErrors \
--alarm-description "Alarm when UserErrors in DynamoDB exceeds 0" \
--namespace AWS/DynamoDB --metric-name UserErrors --statistic Sum \
--period 60 --evaluation-periods 1 --threshold 0 \
--comparison-operator GreaterThanThreshold --unit Count \
--alarm-actions <SNS TOPIC ARN>
```


### Update lambda
```
aws lambda update-function-code --function-name DragonSearch \
--zip-file fileb://resources/steve-code.zip
```