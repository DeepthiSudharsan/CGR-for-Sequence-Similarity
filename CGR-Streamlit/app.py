import streamlit as st
import collections
from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import cm
import pylab
import math
import numpy as np
import glob
import pandas as pd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from io import StringIO  

st.title('Chaos Game Representation')
st.header(' Finding Similarity Between Sequences')

st.subheader('Select the method of input:')
option=st.radio('Radio', ["Paste the Sequences","Upload the Sequences (.FASTA format)","Select from existing files"])
st.sidebar.title("Created By:")
st.sidebar.markdown("Deepthi Sudharsan")
st.sidebar.markdown("Isha Indhu S")
st.sidebar.markdown("Lakshaya Karthikeyan")
st.sidebar.markdown("Roshan Tushar S")
st.sidebar.subheader("IBS4 - Team 15")

f_names = []
seq=[]
path = ""

def readf(filename):
    f = open(filename)
    s = f.read()
    data = "".join(s.split("\n")[1:])
    return data

def extract(s):
	data = "".join(s.split("\n")[1:])
	return data


class CGR_SeqAlignment:
    def count_kmers(self,sequence, k):
        d = collections.defaultdict(int)
        for i in range(len(sequence)-(k-1)):
            d[sequence[i:i+k]] +=1
        for key in list(d):
            if "N" in key:
                del d[key]
        return d
    
    def probabilities(self,kmer_count, k):
        probabilities = collections.defaultdict(float)
        N = len(kmer_count)
        for key, value in kmer_count.items():
            probabilities[key] = float(value) / N
        return probabilities

    def chaos_game_representation(self,probabilities, k):
        array_size = int(math.sqrt(4**k))
        chaos = []
        for i in range(array_size):
            chaos.append([0]*array_size)

        maxx = array_size
        maxy = array_size
        posx = 0
        posy = 0
        for key, value in probabilities.items():
            for char in key:
                if char == "T":
                    posx += maxx // 2
                elif char == "C":
                    posy += maxy // 2
                elif char == "G":
                    posx += maxx // 2
                    posy += maxy // 2
                maxx = maxx // 2
                maxy = maxy//2
            chaos[posy-4][posx-4] = value
            maxx = array_size
            maxy = array_size
            posx = 4
            posy = 4

        return chaos

def CGR_plot(data,k):
    cgr = CGR_SeqAlignment()
    cgr_kmers = cgr.count_kmers(data,k)
    cgr_prob = cgr.probabilities(cgr_kmers, k)
    chaos_mat = cgr.chaos_game_representation(cgr_prob, k)
    str1 = 'Chaos game representation for', k ,'-mers'
    pylab.title(str1)
    pylab.imshow(chaos_mat, interpolation='nearest',cmap=cm.PuBu)
    plt.gca().invert_yaxis()
    pylab.show()
    return chaos_mat,plt

def CGR_prob_dist(chaos1,chaos2):
    dist = np.square(np.array(chaos1) - np.array(chaos2))
    return np.sum(dist)

def FCGR(seq):
    cgr_mats=[]
    st.header("Chaos Game Representations:")
    for i in range(0,len(seq)):
    	st.subheader(f_names[i].replace('.fasta', ''))
    	cgr_mat,cgr_plt=CGR_plot(seq[i],k)
    	cgr_mats.append(cgr_mat)
    	st.pyplot(cgr_plt)

    dist_cgr = np.zeros((len(seq),len(seq)))
    for i in range(0,len(seq)):
        for j in range(0,len(seq)):
            if(i!=j):
                dist_cgr[i][j] = round(CGR_prob_dist(cgr_mats[i],cgr_mats[j]),3)

    df_dist_cgr = pd.DataFrame(dist_cgr)
    st.header("CGR Probability Distance:")
    st.dataframe(df_dist_cgr)

    pylab.title("CGR_probability_distance")
    pylab.imshow(dist_cgr, interpolation='nearest',cmap =cm.PuBu)
    plt.gca().invert_yaxis()
    plt.colorbar()
    st.pyplot(plt)
    

    hierarchy.set_link_color_palette(['m', 'g', 'r', 'k'])
    Z = hierarchy.linkage(dist_cgr)
    plt.figure()
    dn = hierarchy.dendrogram(Z , labels = f_names )
    plt.xticks(rotation=90)
    hierarchy.set_link_color_palette(None) 
    st.header("Dendrogram:")
    st.pyplot(plt)

def CCGR(seq):
    dist_cgr_coord = np.zeros((len(seq),len(seq)))
    for i in range(0,len(seq)):
        for j in range(0,len(seq)):
            if(i!=j):
                CGR_x1,CGR_y1 = CGR_coord(seq[i])
                CGR_x2,CGR_y2 = CGR_coord(seq[j])
                dist_cgr_coord[i][j] = Dist_CGR_coord(CGR_x1,CGR_x2,CGR_y1,CGR_y2)

    df_dist_cgr_coord = pd.DataFrame(dist_cgr_coord)
    st.header("CGR Coordinate Distance:")
    st.dataframe(df_dist_cgr_coord)
    plt.figure()
    pylab.title("CGR_coordinate_distance")
    pylab.imshow(dist_cgr_coord, interpolation='nearest',cmap =cm.PuBu)
    plt.gca().invert_yaxis()
    plt.colorbar()
    st.pyplot(plt)
    



x = {'A': 0,'C': 0,'G':1,'T':1}
y = { 'A': 0,'C': 1,'G':1,'T':0}

A = (0,0)
C = (0,1)
G = (1,1)
T = (1,0)

def CGR_coord(s1):
    CGR_x = [0.5]
    CGR_y = [0.5]
    for s in s1:
    	s = s.upper()
    	tempx = CGR_x[-1]
    	tempy = CGR_y[-1]
    	CGR_x.append(tempx - 0.5*(tempx - x[s]))
    	CGR_y.append(tempy - 0.5*(tempy - y[s]))
    return CGR_x,CGR_y

def CGR_coord_plot(CGR_x,CGR_y):
    n = np.arange(len(CGR_x))

    plt.figure(figsize=(20, 20))
    fig, ax = plt.subplots()
    ax.scatter(CGR_x,CGR_y,color = 'b')

    for i, txt in enumerate(n):
        ax.annotate(txt, (CGR_x[i], CGR_y[i]),fontsize= 15)
    plt.plot(CGR_x,CGR_y, 'g--')
    return plt

def Dist_CGR_coord(CGR_x1,CGR_x2,CGR_y1,CGR_y2):
    l = min(len(CGR_x1),len(CGR_x2))
    X_diff = abs(np.array(CGR_x1[0:l]) - np.array(CGR_x2[0:l]))
    Y_diff = abs(np.array(CGR_y1[0:l]) - np.array(CGR_y2[0:l]))
    return np.sum(np.square(X_diff)) + np.sum(np.square(Y_diff)) 


if option == "Paste the Sequences":
	seq.append(st.text_area('Sequence 1'))
	seq.append(st.text_area('Sequence 2'))
	f_names.append("Sequence 1")
	f_names.append("Sequence 2")

elif option == "Upload the Sequences (.FASTA format)":
	f1_in = st.file_uploader('Sequence 1')
	f2_in = st.file_uploader('Sequence 2')

	if (f1_in and f2_in) is not None:
		f1_str = StringIO(f1_in.getvalue().decode("utf-8"))
		f1 = f1_str.read()

		f2_str = StringIO(f2_in.getvalue().decode("utf-8"))
		f2 = f2_str.read()

		seq.append(extract(f1))
		seq.append(extract(f2))
		f_names.append("Sequence 1")
		f_names.append("Sequence 2")

elif option == "Select from existing files":
	opt1 = st.radio('Radio', ["Animal Genome","COVID Virus Sequences"])
	if opt1  == "Animal Genome":
		path = "C:\\Users\\deept\\Desktop\\Sem 4\\Sem4 Projects\\IBS4 Project\\ANIMAL_GENOME\\"

	elif opt1 == "COVID Virus Sequences":
		path = "C:\\Users\\deept\\Desktop\\Sem 4\\Sem4 Projects\\IBS4 Project\\DNA_SEQ\\"

		
	f = glob.glob(path+"*.fasta")
	for i in range(0,len(f)):
		ft = f[i]
		f_names.append(ft[ft.rindex("\\")+1:len(ft)])

	fileNames=st.multiselect('Multiselect', f_names)
	for i in range(0,len(fileNames)):
		seq.append(readf(path+fileNames[i]))

	f_names = fileNames
	st.text(fileNames)



st.subheader('Define KMER length:')
st.text('Default is set to 4')
k=st.number_input('',step=1,min_value=0, value = 4)

st.subheader('Select the desired method(s):')
mopt=st.selectbox('', ["Click to select", "Frequency CGR","Coordinate CGR","All of the above"])

if mopt=="Frequency CGR":
	FCGR(seq)

if mopt=="Coordinate CGR":
	CCGR(seq)

if mopt == "All of the above":
	st.header("Frequency CGR")
	FCGR(seq)
	st.header("Coordinate CGR")
	CCGR(seq)