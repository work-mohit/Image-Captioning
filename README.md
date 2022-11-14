# Image-Captioning
Image Captioning is a deep learning based project which is deployed on web.
The details of the project is mentioned below with the relevant images.

You saw an image and your brain can easily tell what the image is about, but can a 
computer tell what the image is representing?
Caption generation is a challenging artificial intelligence problem where a textual 
description must be generated for a given photograph. It requires both methods from 
computer vision to understand the content of the image and a language model from the 
field of natural language processing to turn the understanding of the image into words in 
the right order.

<!-- <img src="https://github.com/work-mohit/Image-Captioning/blob/master/Screenshots/1.PNG" width="500" height="200"> -->
![alt text](Screenshots/1.PNG?raw=true "Optional Title")
<br>
# Objective
Image caption generator is a task that involves computer vision and natural language 
processing concepts to recognize the context of an image and describe them in a natural 
language like English. Here are some objectives of this project :

● Encode images and their respective captions.<br>
● Train a model to generate captions.<br>
● Deploy the model as a web app so it can be used globally.<br>

![alt text](Screenshots/2.PNG?raw=true "Optional Title")


Many popular computer vision applications involve trying to recognize things in 
photographs; <br>for example:<br>
<b>• Object Classification:</b> What broad category of object is in this photograph?<br>
<b>• Object Identification</b>: Which type of a given object is in this photograph?<br>
<b>• Object Verification:</b> Is the object in the photograph?<br>
<b>• Object Detection:</b> Where are the objects in the photograph?<br>
<b>• Object Landmark Detection:</b> What are the key points for the object in the 
photograph?
<b>• Object Segmentation:</b> What pixels belong to the object in the image?<br>
<b>• Object Recognition:</b> What objects are in this photograph and where are they?<br>
Outside of just recognition, other methods of analysis include:<br>
<b>• Video Motion Analysis</b> uses computer vision to estimate the velocity of objects in a 
video, or the camera itself.<br>
• In <b>Image Segmentation</b>, algorithms partition images into multiple sets of views.<br>
• Scene reconstruction creates a 3D model of a scene inputted through images or 
video.<br>
• In <b>Image restoration</b>, noise such as blurring is removed from photos using 
Machine Learning based filters.
<br>
<br>
![alt text](Screenshots/comp_task.png?raw=true "Optional Title")
<br><br>

# Model Architecture

The input to cov1 layer is of fixed size 224 x 224 RGB image. The image is passed 
through a stack of convolutional (conv.) layers, where the filters were used with a very small 
receptive field: 3×3 (which is the smallest size to capture the notion of left/right, up/down, 
center). In one of the configurations, it also utilizes 1×1 convolution filters, which can be seen 
as a linear transformation of the input channels (followed by non-linearity). The convolution 
stride is fixed to 1 pixel; the spatial padding of conv. layer input is such that the spatial 
resolution is preserved after convolution, i.e. the padding is 1-pixel for 3×3 conv. layers. 
Spatial pooling is carried out by five max-pooling layers, which follow some of the conv.
layers (not all the conv. layers are followed by max-pooling). Max-pooling is performed over 
a 2×2 pixel window, with stride 2.<br>
Three Fully-Connected (FC) layers follow a stack of convolutional layers (which has a 
different depth in different architectures): the first two have 4096 channels each, the third 
performs 1000-way ILSVRC classification and thus contains 1000 channels (one for each 
class). The final layer is the soft-max layer. The configuration of the fully connected layers is 
the same in all networks.<br>
All hidden layers are equipped with the rectification (ReLU) non-linearity. It is also 
noted that none of the networks (except for one) contain Local Response Normalisation 
(LRN), such normalization does not improve the performance on the ILSVRC dataset, but 
leads to increased memory consumption and computation time.
<br><br>
## CNN Architecture 
![alt text](Screenshots/vgg_arch.png?raw=true "Optional Title")
<br><br>
## RNN Architecture
![alt text](Screenshots/lstm.png?raw=true "Optional Title")
<br><br>
## Preview Of The Combined Model
![alt text](Screenshots/3.png?raw=true "Optional Title")
<br><br>
## Results 
![alt text](Screenshots/4.png?raw=true "Optional Title")
![alt text](Screenshots/5.png?raw=true "Optional Title")
![alt text](Screenshots/6.png?raw=true "Optional Title")
![alt text](Screenshots/7.png?raw=true "Optional Title")
![alt text](Screenshots/8.png?raw=true "Optional Title")
<br><br>
# Thank you for coming this far! 
