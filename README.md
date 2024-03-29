# AKJ-APIs
Proper APIs for fetching latest kirtan from akj.org.

## Introduction
[akj.org](https://akj.org) contains more than 25,000 kirtan files. This APIs have access to all these 25,000 files as well as the new files the admin will add into akj.org.

This is great resource for one who want to create some kind of player for these kirtans. 

Kirtans are well organised with proper indexing with respect to smaagam as well as the artist or kirtaaniya.

## Apps Using These APIs

#### 1. AKJ Kirtan --> https://github.com/Hardeepsingh980/akj-kirtan

##### I would love to feature your apps here as well. Get in touch.


## Documentation

### API for all the kirtan files available

This is going to be a very heavy request because it loads more than 20,000 kirtans. So, this is not adviced to use this API in any case.

```
https://akjm.herokuapp.com/api/kirtan/
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```

### API for searching in all the database including smaagam and artist

This is going to searching in all the database including smaagam and artist. This search in the name of smaagam and name of artist for result.

```
https://akjm.herokuapp.com/api/kirtan/?search=<search_query>
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```

### Api for getting the latest 50 kirtan.

This is going to return the latest 50 kirtans from database. this can be used for displaying the most recent or latest kirtan.

```
https://akjm.herokuapp.com/kirtan/latest/
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```

### Api for searching in the smaagam name

This is going to search in the smaagam name and return the kirtans who have the searched smaagam in it.

```
https://akjm.herokuapp.com/kirtan/smaagam/?search=<search_query>
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```

### Api for searching in the artist name

This is going to search in the artist name and return the kirtans who have the searched artist in it.

```
https://akjm.herokuapp.com/kirtan/artist/?search=<search_query>
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```


### Api for getting all the smaagam
This will display all the smaagam objects in the database. It can be used to display the list of smaagam to select from.

```
https://akjm.herokuapp.com/kirtan/allsmaagam/
```
#### Response

```
List Of Smaagam Object

{
        "smaagam_id": smaagam_id(Int),
        "smaagam_name": smaagam_name(String)
},

```

### Api for searching all the smaagam objects
This will display all the smaagam objects which match the query in the database. It can be used to display the list of searched smaagam to select from.

```
https://akjm.herokuapp.com/kirtan/allsmaagam/?search=<search_query>
```
#### Response

```
List Of Smaagam Object

{
        "smaagam_id": smaagam_id(Int),
        "smaagam_name": smaagam_name(String)
},

```


### Api for getting kirtan objects with accordance to smaagam_id
This will display all the kirtan objects with the smaagam_id passed to it.

```
https://akjm.herokuapp.com/kirtan/getbysmaagam/<int: smaagam_id>
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```



### Api for getting all the artist
This will display all the artist objects in the database. It can be used to display the list of artist to select from.

```
https://akjm.herokuapp.com/kirtan/allartist/
```
#### Response

```
List Of artist Object

{
        "artist_id": artist_id(Int),
        "artist_name": artist_name(String)
},

```

### Api for searching all the artist objects
This will display all the artist objects which match the query in the database. It can be used to display the list of searched artist to select from.

```
https://akjm.herokuapp.com/kirtan/allartist/?search=<search_query>
```
#### Response

```
List Of artist Object

{
        "artist_id": artist_id(Int),
        "artist_name": artist_name(String)
},

```


### Api for getting artist objects with accordance to artist_id
This will display all the kirtan objects with the artist_id passed to it.

```
https://akjm.herokuapp.com/kirtan/getbyartist/<int: artist_id>
```
#### Response

```
List Of Kirtan Object
[{
        "kirtan_id": kirtan_id(int),
        "smaagam": {
            "smaagam_id": smaagam_id(int),
            "smaagam_name": smaagam_name(String)
        },
        "artist": {
            "artist_id": artist_id(int),
            "artist_name": artist_name(String)
        },
        "url": url_to_kirtan_file(URL),
        "duration": duration_of_kirtan(String)
},]

```
