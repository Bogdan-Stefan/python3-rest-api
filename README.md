# python3-rest-api
Cloud Computing Assignment - Creating a simple REST API  
"Alexandru Ioan Cuza" University of Iași, Romania  
Faculty of Computer Science  

Ștefan Bogdan  
stefanbogdan.sbg@gmail.com

## Assignment Description
Create an application that provides a RESTFull API. It is mandatory to use at
least: GET, POST,PUT, DELETE. It is very important to respect all additional
requirements specified in the laboratory.  
**Important note:** You are not allowed to use any web frameworks!

## Observations
* I have made this api purely for educational purposes.  
* The api gives access to a database of cars. For the sake of simplicity, this
"database" is nothing more than a few "Car" objects stored in a python dictionary.  
* The initialisation process populates the database with the following cars:  

    | ID  | Make  | Model | Year | Price € |
    | --- | ----- | ----- | ---- | ------- |
    | 1   | Ford  | Focus | 2012 | 8000    |
    | 2   | Dacia | Logan | 2006 | 2400    |
    | 3   | BMW   | 320d  | 2010 | 10100   |

## Supported Calls
* **GET** `/cars`  
* **GET** `/car/id`  
* **POST** `/cars`  
* **PUT** `/car/id`  
* **DELETE** `/car/id`

**Note:** A JSON containing all the necessary attributes should be present in a
POST or PUT request's body.

## Useful Links
[Beginner's Guide to Creating a REST API](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)  
[HTTP Status Codes](http://www.restapitutorial.com/httpstatuscodes.html)  
[Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)  
[How to Create a REST Protocol](http://www.xml.com/pub/a/2004/12/01/restful-web.html)  
[The Difference Between POST and PUT](http://zacharyvoase.com/2009/07/03/http-post-put-diff/)  
[PUT or POST: The REST of the Story](https://jcalcote.wordpress.com/2008/10/16/put-or-post-the-rest-of-the-story/)  
[REST APIs must be hypertext-driven](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)  
