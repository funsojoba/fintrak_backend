# FinTrak

Welcome to Fintrak. Fintrak is a web app that helps you track your income and expenses for a month, you also can create a budget for the month, at the end of the month, you can see how you've perfromed by comparing your income and expenses and also see if you were able to stick with your budget. Kind of nice right? ☺️


## For Developers
Getting started with this software is quite easy, the entire code base runs on Docker which makes it easy to get started.
- Make sure you have [Docker](https://www.docker.com/products/docker-desktop) installed on your machine
___
### Run the following commands
```
git clone https://github.com/funsojoba/fintrak_backend.git

cd fintrak_backend

touch .env

make build - (this is to build docker engine)

make up - (this is to start docker-compose)
```

- you will find example environment variables in the `.env-example`
- you can look through the `Makefile` file for more docker command
- your code should be running on `127.0.0.1:8000`

Happy hacking 
