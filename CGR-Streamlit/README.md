## Streamlit web app implementation of the project. 

## Pre-requisites :

Make sure to install streamlit if haven't already, to install streamlit use the following command :

```
pip install streamlit
```
All the package requirements along with the versions have been mentioned in the requirements.txt file. 

## How to run?

To run the app, in the anaconda prompt, go to the location where the app.py file is using the cd command and then run the following line :

```
streamlit run app.py
```

## Excerpts from the app

After running the above command, you will get something like this in a new window of your browser. 

![image](https://user-images.githubusercontent.com/59824729/119312536-1d6e1c00-bc90-11eb-9829-25067cd8621c.png)

In the above image, you can see since option "Paste the sequences" was selected, you get two boxes to write-in your sequences. 

You can also either browse and upload two FASTA files 

![image](https://user-images.githubusercontent.com/59824729/119312869-848bd080-bc90-11eb-9068-6d68b5c5f78f.png)

or select multiple files from existing files

![image](https://user-images.githubusercontent.com/59824729/119360284-1531d300-bcc8-11eb-8928-cd8d6ae78172.png)

![image](https://user-images.githubusercontent.com/59824729/119360456-427e8100-bcc8-11eb-9417-a3736666d862.png)

If you select the option to choose multiple files from existing files, an option to choose between the ANIMAL_GENOME folder and DNA_SEQ folder comes up.

You can then give the Kmer length of your choice (default is set to K = 4) and then select the desired method(s) using the drop down.

![image](https://user-images.githubusercontent.com/59824729/119313087-c0269a80-bc90-11eb-8609-2172807b754c.png)

## Sample output

For Human, Rat and Gorilla sequences for K = 4 if we try for both methods (FCGR and CCGR) the output is : 

![image](https://user-images.githubusercontent.com/59824729/119313586-578bed80-bc91-11eb-99b4-d92b44f03548.png)
![image](https://user-images.githubusercontent.com/59824729/119313619-607cbf00-bc91-11eb-8dbf-abbbe14160b4.png)
![image](https://user-images.githubusercontent.com/59824729/119313632-68d4fa00-bc91-11eb-9e6f-2f27afa0e274.png)
![image](https://user-images.githubusercontent.com/59824729/119313656-6ffc0800-bc91-11eb-97e2-b3484a94200d.png)
![image](https://user-images.githubusercontent.com/59824729/119313677-768a7f80-bc91-11eb-9815-4f928e3a1d92.png)
![image](https://user-images.githubusercontent.com/59824729/119313749-873af580-bc91-11eb-9e09-43b1e84c79cc.png)
![image](https://user-images.githubusercontent.com/59824729/119313794-9457e480-bc91-11eb-9b38-3bd125610a8f.png)

