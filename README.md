# Assignment3IoT

## Home Automation System
- Munazza Fahmeen (100701595)
- Nivetha Gnaneswaran (100695935)
- Rodaba Ebadi (100708585)

### Description of code files 
_________________________________

#### views.py
This file combines the below model.py file classes with the logic for different related views within the single class. The different classes
like ModeViewSet and StateViewSet have the needed ViewSets to work accordingly with the urls.py file. 

#### models.py
This stores the different states of the light like the on/off and auto/manual. The classes used within this are
Mode and State which map services to the models. 

#### serializers.py
This allows the model instances to be converted easily to Python datatypes which can be rendered to different content types, 
this is essentially used within the complex data to convert the data. The classes within this file work together with the Models.py
classes.

#### urls.py
This file writes the URL patterns for these services which is contected to the ViewSets instead of the views, this helps generate
the URL conf by registering the viewsets along with the router class. This determines the way the URLs for the application to be mapped
accordingly for it to handle the incoming requests. 

#### controller_service.py
This controller service is implementing the native service in Python and run on the device accordingly. 

#### django_html_frontend.py
This is the frontend of the Django application dashboard that lays out the dashboard components like the Auto and Light switches
that change depending on the status. 

#### django_views.py
This gets the POST requests and outputs and loads the current mode and current state taking into account the username and password
as well as authorizing it. 
