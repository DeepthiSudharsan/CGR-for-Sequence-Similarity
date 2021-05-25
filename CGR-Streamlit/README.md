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

![image](https://user-images.githubusercontent.com/59824729/119438838-bc515180-bd3e-11eb-8436-0f013ba17806.png)
![image](https://user-images.githubusercontent.com/59824729/119438905-de4ad400-bd3e-11eb-828f-aa8aec25e4d9.png)
![image](https://user-images.githubusercontent.com/59824729/119438928-e73ba580-bd3e-11eb-9bb2-02865461dce9.png)
![image](https://user-images.githubusercontent.com/59824729/119438952-ef93e080-bd3e-11eb-80f4-adbe87a18e2b.png)
![image](https://user-images.githubusercontent.com/59824729/119438975-fb7fa280-bd3e-11eb-912e-05f138e4791a.png)
![image](https://user-images.githubusercontent.com/59824729/119438991-05a1a100-bd3f-11eb-9936-1fc1d42deb4a.png)
![image](https://user-images.githubusercontent.com/59824729/119439011-0fc39f80-bd3f-11eb-8f3c-2427e24389f6.png)



