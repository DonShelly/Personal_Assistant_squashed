# Personal Assistant

## Foreword
This project began as a passion project to help vulnerable adults who need assistance with daily organisation.
Since the inception it has become a playground for myself to learn new ways of coding.

## Structure
Currently, there is one POST endpoint, get_all_events() will initially request the users permission to access their google calendar via google callendar API.

## High Level Architecture
This API is built using Flask and deployed on AWS Lambda. The API is served using AWS API Gateway. Eventually this
pattern will integrate events from Cloudwatch (cron jobs) and SQS (message queue) for asynchronous processing, for more complex side-tasks.

Triggers for events are stored in the `aws_triggers` directory. The definition of these triggers is stored
in the `zappa_settings.json` file.

## Deployment
The API is deployed using Zappa. The deployment script is stored in the makefile. To deploy the API, run
the following command:

1. ```shell
   make deploy-<stage-name>
   ```


If you've already deployed the app you will need to use the `make update-<stage>` command

The URL for the API will be displayed in the terminal. It can also be found within the AWS console under
API Gateway.

Be sure to update the environment variables within the Lambda function to match the `config.py` file.

## Makefile
The makefile contains the following commands (run by typing `make <command>`):

- `deploy`: Deploys the API using Zappa
- `remove-cache`: Removes Python cache files
- `tail`: Tails the logs of the deployed API
- `refresh-venv`: Refreshes the virtual environment 
- `copy-vim-config`: Copies the vim configuration file to the home directory
- `docker`: Builds the Docker container for local development
- `docker-run`: Runs the Docker container for local development
- `test`: Runs the unit tests (none implemented yet)
- `docker-test`: Runs the unit tests in the Docker container
- `docker-exec`: Executes a command in the Docker container
- `docker-shell`: Opens a shell in the Docker container
