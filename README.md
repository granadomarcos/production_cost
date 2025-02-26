### Overview

This application fetch data from the https://pentahoportaldeinformacoes.conab.gov.br/pentaho/api/repos/:home:SIAGRO:CustoProducao.wcdf/generatedContent?userid=pentaho&password=password

Instead of using a web scrapping libraries, it leverage the power of REST API. This implementation wind up beaing more eficiently than a web scrapping implementation. 

After fetching the data from the dashboard, it is developed an ETL pipeline.

So far, the data are saved in csv format.

Improvements may be done in future in order to save the data in a database and then create advanced analytics studies upon them.

### RUN the Aplication

### Activate a virtualenv

Not implemented yet

2. Install the requirements

RUN -> pip install -r requirements.txt


### Run the Application

```sh
$ python main.py or CTRL+F5
```


### Testing

Not implemented yet


### Dockerfile

Not implemented yet

