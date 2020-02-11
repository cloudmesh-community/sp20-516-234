# Outline 

## Introduction 

- mission statement of coral is "local ecosystem for AI"

## Overview of Coral project

<!-- - Hardware components (full complete, just chips)
- Software components  (TF lite)
-  -->

## Edge TPU processor

The driving chip behind all of Google's Coral hardware offerings is the Tensor Processing Unit (TPU), a proprietary Application Specific Integrated Circuit (ASIC) built specifically for: machine learning and using TensorFlow. TPUs are used throughout Google's wide portfolio of offerings like Google Photos and Google Translate due to the chip's processing ability to accelerate neural network computations. The chip is meant to run as an alternative, and specific, resource opposed to traditional CPUs and GPUs which have a higher energy and performance demand, that translates into higher operating costs for complex nerual networks. TPU's were designed specifically to address this cost and energy demand, and per Google's benchmark testing against traditional processors (CPUs and GPUs) the TPU delivered a 15-30X performance, as well as a 30-80X performance-per-watt, boost. In order to achieve this benchmark Google thought extensively about how to optimaze memory usage while reducing potential accuracy loss, which resulted in the decision to require quantization before executing models on the TPU.

All of the Google Coral hardware offerings make use of the TPU which is only capable of working with the TensorFlow Lite API. In order to realize the performance benefits of the hardware it is required for your model to be quantized prior to execution on the Coral hardware. This process optimizes machine learning models to calculate weights and predictions using only 8-bit integers versus 16 or 32 bit floating points. This reduces the compute power requirements for executing any models and the memory usage of any local or cloud based inference servers. Google developed the TPU for usage in their data centers to power the neural networks behind some of their most powerful services, but with Google Coral the processor has been embedded directly onto their hardware offerings like the Coral Dev Board and USB Accelerator. 



<!-- - Major hardware component for all of the devices
- what is an inference?
- runs vision models
	- what are vision models?
- inference latency, wtf???
	- vs cloud AI things??

- https://cloud.google.com/blog/products/gcp/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu

https://coral.ai/technology/ -->

## dEv board

Google Coral offers a single board computer, similar to a Raspberry Pi, called the Dev Board that has an on-board TPU chip designed for prototyping local machine learning products. This is the most complete offering from the line of Coral products. The board comes fitted with a CPU, GPU, wireless connectivity, TPU, and 1 GB of RAM, plus other specs that can be found at the Coral website. The Dev Board supports only TensorFlow Lite, which is consistent through all other product offerings. Fast, small form factor inferencing is the ideal use case for integrating the Dev Board into any prototype bedded system. 

To begin set up of the Dev Board to run inferences on the device itself it is required to install the Debian derivative Mandel developed from Google. Once the micro-sd card is flashed with the Mandel OS then the board has a range of features including a shell interface, access to the Debian software archives, and a full bundle of tools to run headless machine laerning apps. Google provides a tool called the MDT which makes connecting and running commands on the board remotely possible.

<!-- TODO: maybe an example of using MDT? -->


 <!-- https://coral.ai/docs/dev-board/mdt/
- Debian Flacor Mendel 
	- optimatized for embedded systems
- headless ML applications?
	- do researhc ont eh architecture of an ML app
- parallel computing for multiple models

https://coral.ai/docs/dev-board/datasheet/ -->


## Edge TPU Accelerator overview 

Coral offers the USB Acclerator for purely prototyping on an existing system instead of using a single board computer to put together a full solution, as is possible with the Dev Board. The USB Accelerator is similar to an external hard drive, the user connects the hardware via the USB port on their existing machine and will have access to the performance and memory of the external device. This device from Google provides the Edge TPU in a parsed down device that can be used with any of the 3 major OS: Linux, MacOS, or Windows. Currently, the USB Accelerator requires Python 3.5 of higher to function with TensorFlow Lite. As with all the other Coral family of products this device can only execute TensorFlow Lite models. 

Unlike the Dev Board the USB Acclerator does not require any software to be installed on ti directly, as it is not a functioning computer, it is purely a coprocessor. However, to function appropriately, the host computer must install the Edge TPU Runtime and the TF Lite API library. Further unlike the dev board, the USB Accelerator does not have any fully functional systems that can be detached. Where the Dev Board can easily be scaled by removing the SoM and transfer easily to production the USB Accelerator is meant more specifcialyl for prototyping. 
<!-- - difference between training and inferences???
	- training involves use of a framework (tensorflow) and training datset
	- typically refers to creating an algorithm
	- inference is using a traing ML algorithm to make a prediction
	https://blogs.gartner.com/paul-debeasi/2019/02/14/training-versus-inference/
- this is an inference server
	- accepts input data directly, outputs the inferencer after running through a trained model
- on device training?
- IoT is a major player for advancement in this space -->

## Prototyping vs Production
<!-- 
- embedded systems are an optoins
- so are on prem network systems
- on device solutions often result in a reduction of pwoer for normal cloud applications of ML servers
https://simpliv.wordpress.com/2018/08/14/what-is-ai/?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com
- kety question: where shoudl I deploy my e ML infereence server in a distributed IoT system? -->

## building models
<!-- 
- converting tensorflow models to Tf lite
- wtf is the small runtime package to run the models
- wtf is quantizing a model
	-  benefits of quantizing is the reduce computation power and reduce the cost fo cloud computing, introduction of chips liek Coral make that possible 
	- specficalyl for dep learning 
	- Facebooks opens ource something
	- https://engineering.fb.com/ml-applications/fbgemm/
	- an inference server runs a model algorithm and returns the inference output
- possible for models that do image recog, bject detection, semantic seg, etc.
- training models is insanely compute instensive  -->

## Competitors 

<!-- - drawbacks to coral onyl accepts tensorflow  -->

## Next steps
<!-- 
- nexus of on device ML and cloud based ML with the added benefits of both 
- The fundamental element of heterogeneous computing is the idea that tasks can be performed on different types of hardware, and yield different performance and power efficiency.
	- opportuntiy to automate the hardware to run the inference if multiple options are available
	- why use CPU or DSP over a GPU when running models


https://developers.googleblog.com/2019/10/coral-moves-out-of-beta.html

https://qengineering.eu/google-corals-tpu-explained.html

https://www.makeuseof.com/tag/google-coral-dev-board-raspberry-pi/

https://coral.ai/docs/edgetpu/faq/#

https://coral.ai/about-coral/

https://coral.ai/technology/

https://blogs.nvidia.com/blog/2016/08/22/difference-deep-learning-training-inference-ai/ -->