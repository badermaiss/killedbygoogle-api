# Killed by Google API - Demo project
### Introduction
This is a REST API written in Python with Flask and the Flask-RESTful extension.
The data is taken from the original <a href="https://github.com/codyogden/killedbygoogle" target="_blank">KilledByGoogle</a> project.

### Installation Guide
* Clone this repository `git clone https://github.com/badermaiss/killedbygoogle-api.git`
* Load the `graveyard.csv` file into a database, with the table named "Graveyard" and the columns matching the first line of the file.
* Fill in your database information in the `api.py` file.
* Install dependencies `pip install -r requirements.txt`
* Run the python server `python api.py`

> Note: this is a demo project for demonstration purposes.
It is not to be considered a finished application.
It can be tested by making requests to https://killedbygoogle.badermaiss.com (self-hosted running in a Docker container).
### Documentation - API Endpoints
| HTTP Method | Endpoints | Action |
| --- | --- | --- |
| GET | /api/services | Get a list of all services |
| GET | /api/services/:id | Get service by ID |
| GET | /api/open_date/:date?operator=:operator&order_by:order | Get services by the date they were opened |
| GET | /api/close_date/:date?operator=:operator&order_by:order | Get services by the date they were closed |
| GET | /api/type/:type | Retrieve services by type |
| GET | /api/name/:name | Retrieve services by name |

All the endpoints output data in JSON format following this semantic:
```
{
    "data": [
        {
            "dateClose": "{YYYY-MM-DD}",
            "dateOpen": "{YYYY-MM-DD",
            "description": "{string",
            "id": {int},
            "link": "{string}",
            "name": "{string}",
            "type": "{string}"
        },
        {
            ...
        }
    ]
}
```
## /api/services
Get a list of all services.
No parameter required.
**On success code:** `200`
#### Success response example: /api/services <a href="https://killedbygoogle.badermaiss.com/api/services" target="_blank">Try it</a>
```
"data": [
    {
        "dateClose": "2022-11-01",
        "dateOpen": "2012-03-29",
        "description": "Google Surveys was a business product by Google aimed at facilitating customized market research.",
        "id": 1,
        "link": "https://www.searchenginejournal.com/google-surveys-is-shutting-down/465287/",
        "name": "Google Surveys",
        "type": "service"
    },

    ...
]
```

## /api/services/:id
**URL Parameters:**
* `id=[int]` required, where `id` is the unique identifier of the service

**On success code:** `200`
**On error code:** `404` 
#### Success response example: /api/services/84 <a href="https://killedbygoogle.badermaiss.com/api/services/84" target="_blank">Try it</a>
**Code:** `200`
```
"data": [
    {
        "dateClose": "2015-04-20",
        "dateOpen": "2013-11-15",
        "description": "Google Helpouts was an online collaboration service where users could share their expertise through live video.",
        "id": 84,
        "link": "https://en.wikipedia.org/wiki/Google_Helpouts",
        "name": "Google Helpouts",
        "type": "service"
    }
]
```

## /api/open_date/:date?operator=:operator&order_by:order
Filter services by the date they were opened.

**URL Parameters:** 
* `date=[date]` required. Can be in any of these formats: `YYYY-MM-DD`, `YYYY-MM`, `YYYY`.
* `operator=[string]` optional. Determines whether to look for services with a date greater or lower than the one given. 
Can be set to `greater_than` or `less_than`. Default is ***less_than***.
* `order_by=[string]` optional. The order in which the dates are listed.
Can be `desc` for descending order or `asc` for ascending order. Default is ***asc***.

**On success code:** `200`
**On error code:** `404` 
#### Success response example: /api/open_date/2020?operator=greater_than <a href="https://killedbygoogle.badermaiss.com/api/open_date/2020?operator=greater_than" target="_blank">Try it</a>
**Code:** `200`
```
"data": [
    {
        "dateClose": "2020-06-30",
        "dateOpen": "2020-02-01",
        "description": "Google Photos Print was a subscription service that automatically selected the best ten photos from the last thirty days which were mailed to user's homes.",
        "id": 31,
        "link": "https://www.forbes.com/sites/paulmonckton/2020/06/20/google-photos-featue-cancellation-auto-print-selection/#19631af66294",
        "name": "Google Photos Print",
        "type": "service"
    },
    {
        "dateClose": "2022-12-19",
        "dateOpen": "2021-03-18",
        "description": "Threadit was a tool for recording and sharing short videos.",
        "id": 277,
        "link": "https://9to5google.com/2022/10/19/google-workspace-threadit/",
        "name": "Threadit",
        "type": "app"
    }
]
```

## /api/close_date/:date?operator=:operator&order_by:order
Filter services by the date they were closed.

**URL Parameters:** 
* `date=[date]` required. Can be any of these formats: `YYYY-MM-DD`, `YYYY-MM`, `YYYY`.
* `operator=[string]` optional. Determines whether to look for services with a date greater or lower than the one given. 
Can be set to `greater_than` or `less_than`. Default is ***less_than***.
* `order_by=[string]` optional. The order in which the dates are listed.
Can be `desc` for descending order or `asc` for ascending order. Default is ***asc***.

**On success code:** `200`
**On error code:** `404` 
#### Success response example: /api/close_date/2023-08?operator=greater_than&order_by=desc <a href="https://killedbygoogle.badermaiss.com/api/close_date/2023-08?operator=greater_than&order_by=desc" target="_blank">Try it</a>
**Code:** `200`
```
"data": [
    {
        "dateClose": "2023-09-30",
        "dateOpen": "2012-06-01",
        "description": "Google Optimize was a web analytics and testing tool that allowed users to run experiments aimed at increasing visitor conversion rates and overall satisfaction.",
        "id": 281,
        "link": "https://support.google.com/optimize/answer/12979939",
        "name": "Google Optimize",
        "type": "service"
    },
    {
        "dateClose": "2023-08-16",
        "dateOpen": "2018-02-21",
        "description": "Google Cloud IoT Core was a managed service designed to let customers securely connect, manage, and ingest data from globally dispersed devices.",
        "id": 276,
        "link": "https://www.iotworldtoday.com/2022/08/23/google-cloud-to-shut-down-iot-core-service/",
        "name": "Google Cloud IoT Core",
        "type": "service"
    }
]
```

## /api/type/:type
Filter by type of the service.
**URL Parameters:** 
* `type=[string]` required. Allowed: `app`, `service` and `hardware`.

**On success code:** `200`
**On error code:** `400`

#### Success response example: /api/type/hardware <a href="https://killedbygoogle.badermaiss.com/api/type/hardware" target="_blank">Try it</a>
**Code:** `200`

```
"data": [
    {
        "dateClose": "2023-01-11",
        "dateOpen": "2015-08-31",
        "description": "Google OnHub was a series of residential wireless routers manufactured by Asus and TP-Link that were powered by Google software, managed by Google apps, and offered enhanced special features like Google Assistant.",
        "id": 12,
        "link": "https://en.wikipedia.org/wiki/Google_OnHub",
        "name": "Google OnHub",
        "type": "hardware"
    },

    ...
]
```

## /api/name/:name
Filter by name of the service.
**URL Parameters:** 
* `name=[string]` required

**On success code:** `200`
**On error code:** `404`

#### Success response example: /api/name/youtube <a href="https://killedbygoogle.badermaiss.com/api/name/youtube" target="_blank">Try it</a>
**Code:** `200`

```
"data": [
    {
        "dateClose": "2022-08-09",
        "dateOpen": "2017-02-15",
        "description": "YouTube Go was an app aimed at making YouTube easier to access on mobile devices in emerging markets through special features like downloading video on wifi for viewing later.",
        "id": 7,
        "link": "https://9to5google.com/2022/05/03/youtube-go-shutting-down/",
        "name": "YouTube Go",
        "type": "app"
    },
    {
        "dateClose": "2020-12-10",
        "dateOpen": "2017-12-14",
        "description": "YouTube VR allowed you to easily find and watch 360 videos and virtual reality content with SteamVR-compatible headsets.",
        "id": 24,
        "link": "https://steamdb.info/app/755770/history/",
        "name": "YouTube VR (SteamVR)",
        "type": "app"
    },
    {
        "dateClose": "2010-02-28",
        "dateOpen": "2006-12-01",
        "description": "YouTube Streams allowed users to watch a YouTube video together while chatting about the video in real-time.",
        "id": 29,
        "link": "https://mashable.com/archive/youtube-test-tube",
        "name": "YouTube Streams",
        "type": "service"
    },

    ...
]
```

### Docker
It's possible to run the server in a Docker container.
To build the image type the following command inside the project's folder:
`
docker build -t killedbygoogle-api .
`

To run the image and create the container type:
`
docker run -d --name killedbygoogle -p 5000:5000 killedbygoogle-api
`
The port on the host can be changed by modifying the first part of the parameter `-p xxxx:5000`.