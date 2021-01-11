# MTAANI
This web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

[Live Demo](https://mtaaniii.herokuapp.com/)

## Author
[Koskey Patience](https://github.com/p-koskey)

## User Stories
User would like to:

- Sign in with the application to start using.
- Set up a profile, a general location ,neighborhood name.
- Find a list of different businesses in  neighborhood.
- Find Contact Information for the health department and Police authorities near Neighborhood.
- Create Posts that will be visible to everyone in neighborhood.
- Change Neighborhood when moving out.
- Only view details of a single neighborhood.

## Installation and Usage Guide:
- Python 3.8

- Pip

- Django

- Virtual enviroment

- Cloudinary

### Clone the application 
    $ git clone https://github.com/p-koskey/mtaani.git
    $ cd mtaani

### Run the application
- Install virtual environment using 

      $ python3 -m venv venv

- Activate virtual environment using 

      $ . venv/bin/activate

- Install all the dependencies from the requirements.txt file by running 

      $python3 pip install -r requirements.txt

- Create a database and edit the database configurations in settings.py to your own credentials.

- Make migrations

      $ python manage.py makemigrations app=hood
      $ python manage.py migrate 
    
- To run the application, in your terminal

      $ python manage.py runserver

## License
This project is licensed under the MIT License.
MIT License
Copyright(2020) Patience Koskey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


