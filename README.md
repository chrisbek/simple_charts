# Calliper example take-home task

This is an example of a task which has some bugs in it.

## Running locally

### Back-end

#### Prerequisites

1. Install python [3.10+](https://www.python.org/downloads/release/python-3106/)
2. Install pipenv `pip3 install --user pipenv`, make sure pip3 points to freshly installed verion python, otherwise use a specific binary
3. Open terminal in the `backend` directory - pipenv should get initialised
4. Install dependencies `pipenv install`

#### Running

`python main.py`

#### Running tests

`python -m pytest`

### Front-end

#### Prerequisites

1. Install node 16 either through [website](https://nodejs.org/download/release/latest-v16.x/) or [nvm](https://github.com/nvm-sh/nvm)
2. Open terminal in the `frontend` directory
3. Install dependencies `yarn`

#### Running

`yarn start` - open https://localhost:3000 to view the app

## Domain Model

Bar chart is used for the test task. Countries are on the X axis, Features are on the Y axis.

**Chart Domain**

- `ChartDataPoint` represents single point on the plot
- `ChartDataFeature` is an enum with all available features
- `Country` is an enum with all available features

**Comment Domain**

- `CommentThread` represents a single thread attached to chart
- `Comment` represents an entry within a thread

## Project structure

`backend` folder hosts FastAPI backend.

- `test_main.py` has integration tests
- `services/test_comments_service.py` has unit tests for thes comments service
- locks are used to prevent race conditions, e.g. multiple comment threads attached to the same chart data point or overwriting the comments

`frontend` folder hosts React/Typescript frontend.

- Jotai atoms are used to manage state.
- Nvio is used for a beautiful, however sometimes laggy, UI
