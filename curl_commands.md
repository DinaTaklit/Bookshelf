
# Curl cmds used to GET/PATCH/DELETE/POST a quest

> Those commond were modified to work proprely in anaconda envirement within windows 

## GET 
```
curl.exe http://127.0.0.1:5000/books 
```

## PATCH
=> add backslash for json data to avoid this type of error => `Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)`

```
curl.exe http://127.0.0.1:5000/books/8 -X PATCH -H "Content-Type: application/json" -d '{\"rating\":\"2\"}' 
```


## DELETE 
```
curl.exe http://127.0.0.1:5000/books/8 -X DELETE 
```


## POST 

```
curl.exe -X POST -H "Content-Type:application/json" -d '{\"title\":\"CIRCE\", \"author\":\"Madeline Miller\", \"rating\":\"5\"}' http://127.0.0.1:5000/books
```
```
curl.exe -X POST -H "Content-Type:application/json" -d '{\"title\":\"Neverwhere\", \"author\":\"Neil Gaiman\", \"rating\":\"5\"}' http://127.0.0.1:5000/books
```

> PS: we use curl.exe to avoid issues of type: 
```
Invoke-WebRequest : Cannot bind parameter 'Headers'. Cannot convert the "Content-Type: application/json" value of type
"System.String" to type "System.Collections.IDictionary".
At line:1 char:48
+ ... 0.1:5000/books/8 -X PATCH -H "Content-Type: application/json" -d '{\" ...
+                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Invoke-WebRequest], ParameterBindingException
    + FullyQualifiedErrorId : CannotConvertArgumentNoMessage,Microsoft.PowerShell.Commands.InvokeWebRequestCommand 
```
