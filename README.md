# Currency-app

This is my first app made in Django.
For now it displays a set list of currecies and USD exchange rate for each of the currencies.

to run the app locally use the command: app_dir/python manage.py runserver

/home displays html table of every currency

/admin allows to access the admin panel

  superuser login: arek password: admin

API

/currency allows:

to GET a list of all the currencys

to POST currency in JSON format, for example: 

}

  "name": "currency X",
  
  "symbol": "XYZ",
  
  "exchange_rate": 12.345
  
}

/currency/{id} allows:

to PUT, DELETE and GET of certain {id} (id/primary key) for example: /currency/1

