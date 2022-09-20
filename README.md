Real Estate(Function)
---------------------

This real estate project will consist of an interaction where:

A seller can sell a property.

A user can search for a property to buy.



I have to add a payment system for when a client want to purchase a property.[]

Applications[]
****************

Front ---> This application will consist of every thing which is related to the platform 
            such as banners , site informations etc.

Authentication ----> This application will consist of the registeration and authorization for the 
                    different type of users and their information.
                    Example: 
                        Login, Sign In and Log out 

Property ----> This application will consists of the initialization of the different properties.

User ---> This application will consist of every action which the user has to perform 
            example: 
                Agents: 
                    Add a property

                Clients: 
                    Search a property



Models[]
*********

Front[x]

Navagition bar as Anonymous: Properties , Buy , Sell , Contact Us , Sign In

Navagition bar as Client: Home , Properties , Agents , About , Contact , Account , logout , View Properties 

Navagition bar as Agents: Home , My Properties,  Request List , Add Properties , Logout
--------------------

Banner 
    property.objects.first() in order to collect the first property existing in the database
    

Newsletter_Section
    title
    description

Site_Informations
    name
    email
    address
    copyright
    logo

Recent_Property_section
    title 
    description

Featured Agents_section
    title 
    description

About_Us_section 
    Main title
    sub_title
    description

Teams_Meet_section
    title
    description

Reviews_section
    title
    description

Contact_section
    title
    description

------------------------------------------

Authentication[x]


User
    first_name
    last_name
    email
    phone_number
    image
    password
    country
    city
    description
    occupation
    address
    facebook link
    instagram link
    twitter link
    linkedin link
    user_type = Agent or client

-------------------------------------------------

Properties[]

Property
    name
    status(for Sale or Rent)
    type
    price
    bedrooms
    bathrooms
    image
    city
    Address 
    country
    description
    building_age
    rooms
    garage
    name_of_agent
    email_of _agent
    phone_number_agent
    Account(agents)






























