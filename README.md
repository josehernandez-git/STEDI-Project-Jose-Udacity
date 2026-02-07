# STEDI-Project-Jose-Udacity
Files for my submission for Udacity Project


My repo contains 4 folders which are:
- Python Scripts
- SQL Scripts
- The Data
- My Screenshots


Note: The requirements say to obtain the row counts. I could do this two different ways in SQL with:
- select * from customer_landing;
or
- select count(*) from customer_landing;

I used the "select * from customer_landing" function for all my queries becuase I want to validate that the tables are loaded correctly, any data issues, and see if there was 
anything to debug with the joins and filters. From my personal experience using Athena/Glue projects in the past I usually need to confirm that the columns exist and spelled correctly. 
I circled the Result for each one of my screenshots becuase when using Athena becuse the Results in the UI is the same as the number of rows (or its count).


My Results

Landing Zone:



<img width="1525" height="734" alt="customer_landing" src="https://github.com/user-attachments/assets/e7c118ee-4aca-45d0-b4b9-1e80b7a96dc0" />

<img width="1394" height="717" alt="customer_landing_non_null" src="https://github.com/user-attachments/assets/29fbdc1e-dc56-4613-999c-2ac0b11511c0" />

<img width="1527" height="807" alt="accelerometer_landing" src="https://github.com/user-attachments/assets/258c6256-a19c-486d-8dc1-74aaa8900ab4" />

<img width="1546" height="813" alt="step_trainer_landing" src="https://github.com/user-attachments/assets/6b194bf1-8c1c-44b8-9d64-4f19e4592942" />



Trusted Zone:


<img width="1526" height="784" alt="customer_trusted" src="https://github.com/user-attachments/assets/896c15ac-af02-4ca6-965a-59f4929692ce" />

<img width="1442" height="698" alt="customer_trusted_non_null" src="https://github.com/user-attachments/assets/068f7898-e6b4-4d82-ae27-585010e58fe1" />

<img width="1517" height="784" alt="accelerometer_trusted" src="https://github.com/user-attachments/assets/c067e666-dc4d-4a9a-8cbd-77a9b3bdc15f" />

<img width="1513" height="764" alt="step_trainer_trusted" src="https://github.com/user-attachments/assets/6474ccf9-e003-43bd-8b18-d4d204d79064" />


Curated Zone:

<img width="1521" height="770" alt="customer_curated" src="https://github.com/user-attachments/assets/2fbbb632-c7cd-4479-adb3-869c5c78f542" />

<img width="1517" height="775" alt="machine_learning_curated" src="https://github.com/user-attachments/assets/257db840-a3aa-47e7-b65a-323308f35b85" />
