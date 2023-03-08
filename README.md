# Currency-app

This is my first app made in Django.
For now it displays a set list of currecies and USD echgange rate for each of currencies.

to run the app locally use cmd command: app_dir/python manage.py runserver
(default port = 8000)

/home displays html table of every currency

/admin allows to acces the admin panel

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

