# teamgrid_py

A simple python package for making API calls to Teamgrid API. It builds upon the requests package.
https://de.teamgridapp.com/

*Note: I am not professional programmer. Install at your own risk. Useful tips are welcome :-).*


## Basic usage
```python
from teamgrid_py import TeamGridPy

api_key = 'your api key'
tgpy = TeamGridPy(api_key, verbose=True)

user = tg.users().where(email='someone@example.com').get()

user_tasks = tg.tasks().where(userId=result.data[0]['userId'])

tasks = user_tasks.get(limit=10)
tasks.data

all_user_tasks = user_tasks.all()
len(all_user_tasks)
```

## Response
The response is parsed into a simple object with fields as object attributes. Additionaly it contains the requests response as '._response'.
```python
> user.data
[{'contactId': 'xxx',
  'costRate': 30,
  'emails': ['someone@example.com'],
  'name': 'someone',
  'roleId': 'default',
  'userId': 'xxx'}]
```


API limit
=========
The API have a rate limit of 100 requests per minute on every API token and url path.