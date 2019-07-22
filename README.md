Application accepts link or file via API endpoints described below and returns link to file. 

To run application:
1. clone this repo
2. make `docker-compose build`
3. make `docker-compose up` (default env variables will run django runserver)
4. Enjoy


Allowed endpoints:

1. `/gen_pdf/link_to_pdf/` - generate link to pdf file
 
2. `/gen_pdf/file_to_pdf/` - To find who is on N place and also it's "neighbors" 




Make commands (execute from base dir or project)
1. `make test` - run unit tests
