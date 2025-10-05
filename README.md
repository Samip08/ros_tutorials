few doubts with the code itself like my move_circle it finishes moving the circle but then it doesnt return control to pcp so now ive like tried to manually manage moving to 8.0 8.0 inside the service 
proportional control could be setup but we would need to subscribe to turtle1/pose unneccesarily it goes to 8.05 8.87 but we could manually trial and error it to something less error
main doubt with the move_circle is why does it not return the control to pcp you see one function is commented out that was supposed to run but its not the whole thing shuts down maybe due to return call in move_circle or the shutdown thing 

basically assignment is about moving from origin(t=0) to 5.5,8.0 and then make a circle and then to 8.0,8.0
pubsub basically keeps always publishing and subscribing but the service is cool cuz its like needs a request like a trigger of a certain datatype, trigger doesnt need an input but it does give a feedback or response all services do
if im gonna call some particular even like last years ball shoot imma check all criteria and call the service rather than having a pub sub for that cuz pub subs gona keep running aimlessly in the back rather call sevice when neededthat is if i can control it
