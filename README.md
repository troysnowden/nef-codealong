# nef-codealong

## Set up Project:

Run the following in the terminal:

* ```pip install flask```
* ```pip install flask_session```
* ```pip install pytest```

In order to run the application, run the following in the terminal:
```flask run```

Ctrl Click on the link in the terminal to open the app in another tab:

* Running on http://127.0.0.1:5000

## Git workflow (trunk-based development):

* ```git checkout main```

* ```git pull```

* ```git checkout -b ticket-no-team-name```

* Some dev work.

* ```git add .```

* ```git commit -m "Enter short and clear message of what the commit does"```

* ```git push```

* Try to commit and push often (the above three commands)

* When finished with the ticket, create a Pull Request. Review it with team. If happy, merge into mainline.

* Rinse and repeat for a new ticket

(There are other git commands available for more specific scenarios - use resources as and when needed)

