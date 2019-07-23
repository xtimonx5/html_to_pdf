Application accepts link or file via API endpoints described below and returns link to file. 

To run application:
1. clone this repo
2. make `docker-compose build`
3. make `docker-compose up` (default env variables will run django runserver)
4. Enjoy


Allowed endpoints:

1. `/gen_pdf/link_to_pdf/` - generate pdf from link 
 
2. `/gen_pdf/file_to_pdf/` - generate pdf from file 




Make commands (execute from base dir of project)
1. `make test` - run unit tests
