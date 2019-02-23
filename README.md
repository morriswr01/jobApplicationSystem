# secret_Cool_Project

## Packages Required to Run Application

Install pipenv.

Launch python environment with `pipenv shell`.

Run `pipenv install` to install necessary packages.

This is for linux.

---

If you are on windows you have to install mysqlclient manually so do the above to install all other dependencies and then manually run `pipenv install` on the relevant version of mysqlclient downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient. Put the downloaded file in the project directory and run `pipenv install mysqlclient-1.4.2-cp27-cp27m-win_amd64.whl` or whatever the name of the file you downloaded is.

---

To start server run `pipenv shell` to launch a python environment and then `python manage.py runserver` from inside the jobApplicationProject folder.

---

.Scss files contain all the css for the project. Can just use normal css if you don't know what sass is.
