[![Build Status](https://travis-ci.org/ridibooks/lightweight-rest-tester.svg?branch=master)](https://travis-ci.org/ridibooks/lightweight-rest-tester)
[![Coverage Status](https://coveralls.io/repos/github/ridibooks/lightweight-rest-tester/badge.svg?branch=HEAD)](https://coveralls.io/github/ridibooks/lightweight-rest-tester?branch=HEAD)

# lightweight-rest-tester
A lightweight REST API testing framework written in Python (working with 2.7 ~ 3.6). It reads [JSON Schema](http://json-schema.org) test-cases from JSON files and then generates and executes unittest of Python. 

## 1. Getting Started
Write your test cases into JSON files and pass their locations (directory) as the argument:
```
python rest_tester/main.py ${JSON_FILE_DIRECTORY}
```

If your Python cannot identify the `rest_tester` module, then set the Python path:
```
export PYTHONPATH=.
```

### JSON File Format
Specify your **api** and how you **test** it. In the `api` part, you can set the target REST API by URL (`url`) with method (`method`). It supports five HTTP methods, **GET**, **POST**, **PUT**, **PATCH** and **DELETE**. You can also set the parameters (`params`). In the `tests` part, you can add three types of test cases, timeout (`timeout`) in seconds, HTTP status code (`statusCode`) and [JSON Schema](http://json-schema.org) (`jsonSchema`).

The following example makes **GET** (`get`) API call to `http://json-server:3000/comments` with the `postId=1` parameter. When receiving the response, it checks the follows:

- if the response is received within `10` seconds.
- if the status code is `200`.
- if the returned JSON satisfies JSON Schema.

```json
{
  "api": {
    "url": "http://json-server:3000/comments",
    "method": "get",
    "params": {
      "postId": 1
    }
  },

  "tests": {
    "timeout" : 10,
    "statusCode": 200,
    "jsonSchema": {
      "Write your JSON Schema in here."
    }
  }
}
```

You can find some samples in [here](/samples) and [there](/test/function/resources). For the details, please read the below.

## 2. API

The `api` part consists of `method`, `url`, `params` and `data`. `method` and `url` are essential, but `params` and `data` are optional.

#### params
When parameter values are given as an array, multiple test cases with all possible parameter-sets are generated. They will show which parameter-set fails a test if exists (please see [5. Test Case Name](#5-test-case-name)). For example, the following parameters generate 9 different parameter sets. One of them could be `{"p1": 1, "p2": "abc", "p3": "def"}`.
```json
"params": {
  "p1": [1, 2, 3],
  "p2": "abc",
  "p3": ["def", "efg", "hij"]
}
```

#### data
When you make **POST**, **PUT** and **PATCH** calls, you can send JSON format data using `data`. You can find an example in [here](/test/function/resources/test_function_single_post.json).

## 3. Tests

The `tests` part validates the responses of API calls. It checks if the response is received within `timeout`. It also checks the received status code (`statusCode`) and JSON (`jsonSchema`). Either `statusCode` or `jsonSchema` should be provided.

#### timeout
Request's timeout in seconds. Its default value is 10 (seconds).

#### statusCode
The expected status code. When an array of status codes is given, the test checks if one of these codes is received. For example, the following `statusCode` checks if the received status code is either `200` or `201`:
```json
"statusCode": [200, 201]
```

#### jsonSchema
This framework uses [jsonschema](https://github.com/Julian/jsonschema) to validate the received JSON. `jsonschema` fully supports the [Draft 3](https://github.com/json-schema-org/JSON-Schema-Test-Suite) and [Draft 4](https://github.com/json-schema-org/JSON-Schema-Test-Suite) of JSON Schema.

## 4. Write-and-Read Test

Sometimes, it is necessary to check if modifications on a database work correctly. We call such test scenario as **Write-and-Read** test that has a particular test-execution-order like **PUT-and-GET**. This framework supports this feature. To use it, just put two `api`/`tests` pairs in a list when writing JSON file:

```json
[
  {
    "api": {
      "url": "http://json-server:3000/posts",
      "method": "post",
      "data": {
        "title": "foo",
        "body": "bar",
        "userId": 1
      }
    },
    "tests": {
      "statusCode": 201
    }
  },
  {
    "api": {
      "url": "http://json-server:3000/posts",
      "method": "get",
      "params": {
        "userId": 1
      }
    },
    "tests": {
      "statusCode": 200
    }
  }
]
```

You can find more examples in [here](/test/function/resources).

Unlike the single-method test, **Write-and-Read** test builds always one test case to preserve test-execution order. Even when arrays of parameter values are given, this framework executes all the test cases belonging to first `api`/`tests` pair and then runs the test cases of the rest pair.

## 5. Test Case Name

This framework uses [URL query string format](https://en.wikipedia.org/wiki/Query_string) to make test case name. However, it starts with JSON file name instead of `url`. It helps you understand which parameter-set fails a test if exists. For example, `json_file.json?postId=1&id=2` is the name of the following test case:

```json
{
  "url": "http://json-server:3000/comments",
  "method": "get",
  "params": {
    "postId": 1,
    "id": 2
  },
  "timeout" : 10
}
```

Unlike the single-method test, **Write-and-Read** test uses only JSON file name for its name.

## 6. Contributions to This Project

Please feel free to leave your suggestions or make PRs.
