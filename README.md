Tesfaye Samson 
1402506



Hello dear Teacher I made all the question including the deployment.
read every line there is a clear description about every document that i add to this folder 
the files
1)unitedMODEL is the code for training and creating the model .

2)united and app.py this code  is used for deploy the model on Fast API.

3)updated_survey_lung_cancer is the data set that i use for training the model and there is a full description on my ML DOC FILE  about each step.


4)lung_cancer_model.pkl is the trained model

  

To deploy you will follow the following steps

navigate to that folder first using cd path/to/folder

uvicorn app:app --host 0.0.0.0 --port 8000 --reload   on Anaconda Promp


     
  Access the API Docs by opening this URL in your browser:

    http://127.0.0.1:8000/docs
 and use  input_case2 for the input file 
    
   Find the POST /predict endpoint.
   Click Try it out and paste the JSON data use input_case2.json file 
   Click Execute and check the response.

