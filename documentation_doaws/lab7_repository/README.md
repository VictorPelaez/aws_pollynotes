# Polly Notes API

## Methods

### /notes

#### GET - Runs the lambda list-function

- Expected API input

  - Authorization Header

- Function test event

```json
{
"requestContext": {
  "authorizer": {
    "claims": {
      "cognito:username": "student"}
      }
    }
}
```

- Output returned to client

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "[{\"UserId\": \"student\", \"Note\": \"My note to myself\", \"NoteId\": \"001\"}, {\"UserId\": \"student\", \"Note\": \"My new note to myself\", \"NoteId\": \"002\"}]",
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
}
```

#### POST - Runs the lambda createUpdate-function

- Expected API input

  - Authorization header
  - Request Body with json object string containing a NoteId and note text

- Function test event

```json
{
"requestContext": {
  "authorizer": {
    "claims": {
      "cognito:username": "student"}
      }
    },
"body": "{\"NoteId\":\"999\",\"Note\":\"lambda test note\"}"
}
```
  
- Output returned to client

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "999",
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
}
```

### /notes/search

#### GET - Runs the lambda search-function

- Expected API input

  - Authorization Header
  - A "text" query string parameter with the search tearm

- Function test event

```json
{
"requestContext": {
  "authorizer": {
    "claims": {
      "cognito:username": "student"}
      }
    },
"queryStringParameters": {"text": "new note"}
}
```

- Output returned to client

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "[{\"UserId\": \"student\", \"Note\": \"My new note to myself\", \"NoteId\": \"002\"}]",
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
}

```

### /notes/{id}

#### DELETE - Runs the lambda delete-function

- Expected API input

  - Authorization header
  - Note ID in the request path to delete

- Function test event

```json
{
"requestContext": {
  "authorizer": {
    "claims": {
      "cognito:username": "student"}
      }
    },
"pathParameters": {"id": "999"}
}
```
  
- Output returned to client

```json
Response
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "999",
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
}


```

#### POST - Runs the lambda dictate-function

- Expected API input

  - Authorization header
  - Note ID in the request path to dictate
  - Request Body with json object string containing the polly voice to use

- Function test event

```json
{
"requestContext": {
  "authorizer": {
    "claims": {
      "cognito:username": "student"}
      }
    },
"pathParameters": {"id": "999"},
"body": "{\"voice\":\"Joey\"}"
}
```
  
- Output returned to client

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "\"https://lab-7-pollynotesmp3-1rpbmkboij9mz.s3.amazonaws.com/student/999.mp3?AWSAccessKeyId=ASIAX5E52QZYVKY7JMM2&Signature=7l%2FZC7Flq2p0tGN%2B6jY%2FlCtxHb4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIEo5z%2F9XjKAhEO32MC%2BEzGP6yOlL49Ex7FlOImXdMNlbAiAaFgVjTYYdvfoHodM74TOoIQ3YipgGnbS5l7ElgKjtjyr0AQiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAIaDDU0MzY0NDM1NDE2MSIM0HGwy1ByEfPBG6wjKsgBsmntDn4%2ByVWJ8SwaFfcPzSntdt4ANi%2BVBxDszeBlaqED6aRVjcIA9KnHPJ67dnoy37KZv5yfV7UWXyk0Av07vWSDpUChkvtB2ofrpcRlMPR6MGFRFA56N79ITLgbGoa8fiuyLKBs72f2WFgWGWyu239J%2Bk1Wx9CLIfEnS4Vz2yxdbdVRQtK7O7j9jHy8cd97pjpANgxgKfaVTHuTXqvETgTv1Ea90aEEuJ72OAJ4R5e6Hb1v6WaXRUV%2FZsaJJwRXcsdI%2BSu7MKIwuIWxhAY64QH4VX%2BBgFE9a02jmfoG%2Bb0BYBtzYMpke4H%2BUY42t4hYSL%2BqqDtEaJX5QjE7b5rIJDz2Ousjex4%2FuDDWQgmi7fj7CBB9qVS%2BB4SROyURnN7%2BJUEYGkCKt1%2BPuyjArMbleFIkfSn%2BXYi8MYhB5suWQtwWeg7pfy9LMC5x2tmzO7%2FgzqGCsJL4QdlWWAtniFyJgsKuVUznaMXOLqCg1AZE7hliwvXhEbriWxp2GZl1BV8Kw1RcTsnClvdw4S8J4h42DZjLf1RQSpvyD8wiwt%2FUCOtllgnQEmJ%2BTib0JtcBSi6783A%3D&Expires=1619808459\"",
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
}

```
