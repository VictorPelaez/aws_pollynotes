# AWS API Gateway
Concepto de recurso y dentro de metodos (get, post...)
- RESOURCES
- STAGES & stages variables: ex. DEV or PROD 
- METHODS: ex. GET, PUT, etc

# Create API Gateway in AWS Console
![image](lab5/Agw_1.JPG)

# Create resource called /notes
![image](lab5/Agw_2.JPG)

# Create GET method and mapping
![image](lab5/Agw_3.JPG)

Method execution with:

![image](lab5/Agw_4.JPG)

![image](lab5/Agw_5.JPG)


# Update the GET Method

![image](lab5/Agw_6.JPG)

![image](lab5/Agw_7.JPG)

with:

```json
#set($inputRoot = $input.path('$'))
[
    #foreach($elem in $inputRoot)
    {
    "NoteId" : "$elem.NoteId",
    "Note" : "$elem.Note"
    } 
    #if($foreach.hasNext),#end
    #end
]
```

## Create POST method
![image](lab5/Agw_8.JPG)

# Enforce Schema
![image](lab5/Agw_9.JPG)

with:

```json
{
    "title": "Note",
    "type": "object",
    "properties": {
        "UserId": {"type": "string"},
        "NoteId": {"type": "integer"},
        "Note": {"type": "string"}
    },
    "required": ["UserId", "NoteId", "Note"]
}
```


## Test POST method
![image](lab5/Agw_10.JPG)


## test request validator

in test, method execution:
![image](lab5/Agw_11.JPG)

## Deploy the API with CORS configuration
![image](lab5/Agw_12.JPG)

## Deploy the API
![image](lab5/Agw_13.JPG)