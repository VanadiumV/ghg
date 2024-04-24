# PROBLEM STATEMENT-Medical Assistant
In recent times, the world has witnessed a concerning trend in the rise of various disease cases, posing significant challenges to healthcare systems globally. Factors such as population growth, urbanization, environmental changes, and global travel have contributed to the spread and escalation of infectious diseases, chronic conditions, and other health concerns. Amidst this backdrop, the need for accessible and reliable healthcare information and support has become more critical than ever. To address this growing demand, the development of virtual assistants tailored to healthcare needs has emerged as a promising solution. These virtual assistants leverage artificial intelligence and data-driven approaches to provide personalized recommendations, symptom analysis, and guidance, empowering individuals to make informed decisions about their health and well-being. By harnessing the power of technology, virtual assistants stand poised to assist individuals and healthcare professionals alike in navigating the complexities of today's evolving healthcare landscape, ultimately fostering better health outcomes for all.

* Create a virtual medical assistant: Develop ML algorithms and models that utilize symptoms data to predict and identify potential disease and match it with required Specialist of Disease

## Solution
Development of an ML model which takes input of symptoms from the user and compares with the feeded csv files by parsing through them and performing algorithms to increase the accuracy of model each time with new values . Used all models like Logistic Regression Accuracy : 100.000%
Decision Tree  
Random Forest 
SVM 
NaiveBayes 
K-Nearest Neighbors 
Mapped the description of Specialist for the Disease Predicted.This will help the patient to know what disease he/she facing and consult the required specialist according to emergency.


### Disease prediction AI model
The predictions provide insights into the predicted disease, the likelihood or chance of that disease based on the classification model, the recommended doctor to visit for that disease, and a description of the predicted disease.
**Predicted Disease:** *-The disease that has been predicted based on the symptoms provided.-*

**Chance of the Disease:** *-The likelihood or probability of having that disease, as determined by the classification model.-*

**Recommended Doctor:** *-The doctor or specialist recommended to visit for further evaluation or treatment of the predicted disease.-*

**Description of the Disease:** *-A brief overview or description of the predicted disease, providing additional information about its symptoms, causes, and potential treatments.-*

**This aims to provide a concise and informative overview of the predicted disease, its associated likelihood, the recommended doctor, and a brief description to aid in understanding and decision-making regarding the predicted disease.**


## Setup of local environment
1. Go to workingcode branch
2. Fork the repo
3. Run the command `git clone https://github.com/VanadiumV/ghg/tree/workingcode`
4. All the data used for training and testing the models (csv) is in the folder csv.
5. Run the jupyter notebook `disease-speciality-recommedation`
6. The model is saved in model.pkl
7. Navigate to `backend` repo.
8. Run command python Apis.py 
9. The backend will start to run on `localhost:5000/model`
10. Navigate to `frontend` repo.
11. First install all dependencies by running `npm i`.
12. Run command npm start.
13. The frontend will start to run on `localhost:3000`.
14. Check out the predictions.




