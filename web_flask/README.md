## Web Flask
A FlasK Framework Project

* All scripts start a Flask web application: listening on `0.0.0.0`, port `5000`
* Requirement: use the option `strict_slashes=False` in the route definition

### 0-hello_route.py
* Routes:
   * `/`: display “Hello HBNB!”


### 1-hbnb_route.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”


### 2-c_route.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable


### 3-python_route.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”


### 4-number_route.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer


### 5-number_template.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer
   * `/number_template/<n>`: display a HTML page only if `n` is an integer:
      * `H1` tag: “Number: `n`” inside the tag `BODY`


### 6-number_odd_or_even.py
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer
   * `/number_template/<n>`: display a HTML page only if `n` is an integer:
      * `H1` tag: “Number: `n`” inside the tag `BODY`
   * `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
        * `H1` tag: “Number: `n` is even|odd” inside the tag BODY


### 7-states_list.py
* You must use `storage` for fetching data from the storage engine
(`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* After each request you must remove the current SQLAlchemy Session
  * Declare a method to handle `@app.teardown_appcontext`
  * Call in this method `storage.close()`
* Routes:
  * `/states_list`: display a HTML page: (inside the tag`BODY`)
    * H1 tag: “States”
    * UL tag: with the list of all State objects present in DBStorage sorted by name


### 8-cities_by_states.py
* You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
* To load all cities of a State:
  * If your storage engine is DBStorage, you must use cities relationship
  * Otherwise, use the public getter method cities
* After each request you must remove the current SQLAlchemy Session:
  * Declare a method to handle @app.teardown_appcontext
  * Call in this method storage.close()
* Routes:
  * `/cities_by_states`: display a HTML page: (inside the tag BODY)


### 9. Cities by states

*  You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all(...)
*  To load all cities of a State:
*     If your storage engine is DBStorage, you must use cities relationship
*      Otherwise, use the public getter method cities
*  After each request you must remove the current SQLAlchemy Session:
*      Declare a method to handle @app.teardown_appcontext
*      Call in this method storage.close()

*  Routes:
      * `/cities_by_states` : display a HTML page: (inside the tag BODY)
*          H1 tag: “States”
*          UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
*                 LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
*                     LI tag: description of one City: <city.id>: <B><city.name></B>



### 10. States and State
* Routes:
    * `/states`: display a HTML page: (inside the tag BODY)
    *    H1 tag: “States”
    *    UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) i*p
    *      LI tag: description of one State: <state.id>: <B><sta.name></B>*
    * `tates/<id>`: display a HTML page: (inside t tag BODY)*
    *  If a State object is fou with this id:*
    *      H1 tag: “State: ”*
    *      H3 tag: “Cities:”*
    *      UL tag: with the list of City objects linked to the State sorted by name (A->Z)*
    *          LI tag: description of one City: <city.id>: <B><city.name></B>
    *  Otherwise:
    *        H1 tag: “Not found!”


### 11. HBNB filters
* Routes:
    * `/hbnb_filters` : display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
*         Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
*             Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
*         State, City and Amenity objects loaded from DBStorage and sorted by name (A->Z)
* data source[10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql)



### 12. HBNB is alive!
### #advanced

    * Routes:
    *     `/hbnb`: display a HTML page like 8-index.html, done during the 0x01. AirBnB clone - Web static project
    *         Updated .popover class in 6-filters.css to enable scrolling in the popover and set max height to 300 pixels.
    * Import data from [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql)
