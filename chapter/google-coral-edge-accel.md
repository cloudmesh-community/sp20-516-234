# Introduction To Google Coral

As machine learning and artificial intelligence expand through various
industries it is becoming more common for users to seek ways to perform
comprehensive model training and building on premise on hardware not connected
to the open internet. This use case is developing from the need to protect
sensitive data by disconnecting them from open networks and removing dependency
from computing power possible in the cloud. To accommodate this development and
to provide an offering for this type of edge computing heavy on machine learning
Google has introduced it's family of products named Google Coral. They focus
around their proprietary Tensor Processing Chip, or TPU, which was designed
specifically to improve performance of machine learning models during training
or even development[@CoralTech-sp20-516-234]. You can find the claimed stats on
the [Google Coral website](https://coral.ai/) which allows you to compare
against their handful of competitors. The family of product is separated into
two distinct verticals: Prototyping and Production. 

## Prototyping Products

The prototyping offerings are full boards reminiscent of a Raspberry Pi or
Arduino. The most comprehensive is the Dev Board. This is full computer that has
the Google TPU chip embedded on it's board[@DevBoard-sp20-516-234]. This is
meant to function as a prototype, embedded edge computer to test a full stack
solution and OS. If that is too heavy of a solution for your needs Google also
offers a tool called the Edge TPU Accelerator. This hardware is meant to
function familiarly to an external hard drive in the sense that it offers a
hardware extension to an existing system without needing to open up your machine
and machine changes[@USBAccel-sp20-516-234]. This device is essentially just a
TPU chip that runs off of your machine setup and gives the user the opportunity
to run on a powerful compute hardware when models are uploaded. The final
offering in the prototyping family is the Mini Dev Board. This offers the same
functionality of the Dev Board in a smaller package. This product in currently
in development and not widely available to general users.

## Production Aimed Products

The production offerings range from different variations of PCIe products that
have the Edge TPU chip embedded to the a singular accelerator module with the
Edge TPU chip. These products are designed to be added to the users devices to
improve the model processing power. The current slate of offerings are for the
PCIe products are: the Mini PCIe Accelerator, M.2 Accelerator A+E Key,  M.2
Accelerator B+M Key. These offer customization opportunities for the user to
upgrade the model processing power of their devices[@Products-sp20-516-234].
Next, the System-on-Module is a fully-integrated system for accelerated machine
learning that can be plugged into an existing system[@Products-sp20-516-234]. It
is runs a Linux system and can connect to the internet making brownfield devices
that do not have internet connectivity viable for that use
case[@DevBoard-sp20-516-234]. The final offering is the individual Accelerator
Module. This is the core of every device in the Coral family that drives the
improved model processing power for every device[@CoralTech-sp20-516-234], so
Google has made it available for those user who want to build a custom board but
include their TPU chip. There are further performance details and use case
examples that google outlines individually for each device. A lot of the
performance specifications overlap and are shared due to the Edge TPU, but the
specifics vary a bit from device to device. 

![Coral Products [@Products-sp20-516-234]](./coralProducts.png){#fig:Coral-Product-Line width=1in}

# Edge TPU processor

The driving chip behind all of Google's Coral hardware offerings is the Tensor
Processing Unit (TPU), "a proprietary Application Specific Integrated Circuit
(ASIC)" built specifically for: machine learning and using
TensorFlow[@FAQ-sp20-516-234]. TPUs are used throughout Google's wide portfolio
of offerings like Google Photos and Google Translate due to the chip's
processing ability to accelerate neural network computations. The chip is meant
to run as an alternative, and specific, resource opposed to traditional CPUs and
GPUs which have a higher energy and performance demand, that translates into
higher operating costs for complex neural networks. TPU's were designed
specifically to address this cost and energy demand, and per Google's benchmark
testing against traditional processors (CPUs and GPUs) the TPU delivered a
"15-30X performance, as well as a 30-80X
performance-per-watt"[@TPUInDepth-sp20-516-234], boost. In order to achieve this
benchmark Google thought extensively about how to optimize memory usage while
reducing potential accuracy loss, which resulted in the decision to require
quantization before executing models on the TPU.

All of the Google Coral hardware offerings make use of the TPU which is only
capable of working with the TensorFlow Lite API. In order to realize the
performance benefits of the hardware it is required for your model to be
quantized prior to execution on the Coral hardware[@FAQ-sp20-516-234]. This
process optimizes machine learning models to calculate weights and predictions
using only 8-bit integers versus 16 or 32 bit floating points. This reduces the
compute power requirements for executing any models and the memory usage of any
local or cloud based inference servers. Google developed the TPU for usage in
their data centers to power the neural networks behind some of their most
powerful services, but with Google Coral the processor has been embedded
directly onto their hardware offerings like the Coral Dev Board and USB
Accelerator[@TPUInDepth-sp20-516-234]. 

<!-- - Major hardware component for all of the devices
- what is an inference?
- runs vision models
    - what are vision models?
- inference latency, wtf???
    - vs cloud AI things??

- https://cloud.google.com/blog/products/gcp/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu

https://coral.ai/technology/ -->

# TensorFlow Lite

The Coral product family is dependant on all models being pre-compiled and
converted into a TensorFlow Lite file[@Products-sp20-516-234]. The Edge TPU is
designed to only run these types of files to maintain the specs Google is
advertising. TensorFlow Lite is designed specifically as a "deep learning
framework for on-device interfaces"[@TFL-sp20-516-234]. The major benefits of
TensorFlow Lite are the low latency and a small binary size to allow for on
device machine learning. The two major components of this framework are the
interpreter and the converter, both of which are needed to deploy a ML solution
built on TensorFlow Lite. 

Per Google's documentation of the TensorFlow Lite framework, the workflow for
developing and converting a TensorFlow model to one that can be embedded on a
device is as follows:

1. Pick a model

The Coral product family supports a number of pre compiled models that can be
found on their website, [here](https://coral.ai/models/), but TensorFlow Lite
and the Coral products do support custom models or third party models as long as
they are properly converted to TensorFlow
Lite[@TensorFlowLiteGuide-sp20-516-234].

2. Convert the model

For any model that is not pre-compiled to run successfully on the Coral devices
it is required to convert that model to TensorFlow Lite. The directions for that
process of using the TensorFlow Lite Convertor can be found on [Google's
website](https://www.tensorflow.org/lite/convert/index)[@TensorFlowLiteGuide-sp20-516-234].

3. Deploy to your device

Run the model on the device with the interpreter. This is where the user is able
to make use of the TensorFlow APIs to run the inferences locally on their
embedded devices[@TensorFlowLiteGuide-sp20-516-234]. 

4. Optimize your model

This is the final step laid out by Google in the workflow. This is commonly a
final step in any process once you have proven it works and is stable, the user
can then move to optimize their inferences and reduce the compute power
required. Google offers a model optimization toolkit to improve the use of
available power on the Coral devices[@TensorFlowLiteGuide-sp20-516-234].

These steps are not specific to Google Coral products, they are steps Google
shares to provide guidance for anyone building models on any edge device
product. However, these steps are required to be followed if the user is
expecting to run a model on any Coral Product as the Edge TPU requires models be
deployed in the TensorFlow Lite format to be correctly interpreted to run the
desired inferences.

For further reading on TensorFlow Lite take a deep dive into the [Google
TensorFlow Documentation](https://www.tensorflow.org/).

## Supported Models

Google Coral products support custom, pre-compiled, and third party models on
their hardware, however they must be compiled into a TensorFlow Lite format to
be properly interpreted[@CoralModels-sp20-516-234]. It is important to note that
it is not possible to train a model using TensorFlow Lite, that must be done
while the model is still a TensorFlow file, `.pb`[@TFLConverter-sp20-516-234].
Google provides a visualization of the process, including the model type at each
stage, to show how to properly deploy a model that is compatible with the Edge
TPU.

![TensorFlowLiteDeployment [@CoralModels-sp20-516-234]](./modelFlow.png){#fig:Deploy-Model-To-Coral width=1in}

<!-- https://coral.ai/docs/edgetpu/models-intro/

https://coral.ai/models/
https://cloud.google.com/vision/automl/docs/edge-quickstart -->

# Dev board

Google Coral offers a single board computer, similar to a Raspberry Pi, called
the Dev Board that has an on-board TPU chip designed for prototyping local
machine learning products. This is the most complete offering from the line of
Coral products. The board comes fitted with a CPU, GPU, wireless connectivity,
TPU, and 1 GB of RAM, plus other specs that can be found at the Coral
website[@DevBoardData-sp20-516-234]. The Dev Board supports only TensorFlow
Lite, which is consistent through all other product offerings. "Fast, small form
factor inferencing is the ideal use case for integrating the Dev Board into any
prototype bedded system"[@DevBoard-sp20-516-234]. 

To begin set up of the Dev Board to run inferences on the device itself it is
required to install the Debian derivative Mendel developed from
Google[@DevBoard-sp20-516-234]. Once the micro-sd card is flashed with the
Mendel OS then the board has a range of features including a "shell interface,
access to the Debian software archives, and a full bundle of tools to run
headless machine learning apps"[@MDT-sp20-516-234]. Google provides a tool
called the MDT which makes connecting and running commands on the board remotely
possible.

<!-- TODO: maybe an example of using MDT? -->


 <!-- https://coral.ai/docs/dev-board/mdt/
- Debian Flacor Mendel 
    - optimatized for embedded systems
- headless ML applications?
    - do researhc ont eh architecture of an ML app
- parallel computing for multiple models

https://coral.ai/docs/dev-board/datasheet/ -->


# Edge TPU Accelerator

Coral offers the USB Accelerator for purely prototyping on an existing system
instead of using a single board computer to put together a full solution, as is
possible with the Dev Board. The USB Accelerator is similar to an external hard
drive, the user connects the hardware via the USB port on their existing machine
and will have access to the performance and memory of the external device. This
device from Google provides the Edge TPU in a parsed down device that can be
used with any of the 3 major OS: Linux, MacOS, or
Windows[@AccelProductsPage-sp20-516-234]. Currently, the USB Accelerator
requires Python 3.5 of higher to function with TensorFlow
Lite[@USBData-sp20-516-234]. As with all the other Coral family of products this
device can only execute TensorFlow Lite models. 

Unlike the Dev Board the USB Accelerator does not require any software to be
installed on it directly, as it is not a functioning computer, it is purely a
coprocessor. However, to function appropriately, the host computer must install
the Edge TPU Runtime and the TF Lite API library[@MDT-sp20-516-234]. Further
unlike the dev board, the USB Accelerator does not have any fully functional
systems that can be detached. Where the Dev Board can easily be scaled by
removing the SoM and transfer easily to production the USB Accelerator is meant
more specifically for prototyping. 

<!-- - difference between training and inferences???
    - training involves use of a framework (tensorflow) and training datset
    - typically refers to creating an algorithm
    - inference is using a traing ML algorithm to make a prediction
    https://blogs.gartner.com/paul-debeasi/2019/02/14/training-versus-inference/
- this is an inference server
    - accepts input data directly, outputs the inferencer after running through a trained model
- on device training?
- IoT is a major player for advancement in this space -->

<!-- ## Prototyping vs Production -->
<!-- 
- embedded systems are an optoins
- so are on prem network systems
- on device solutions often result in a reduction of pwoer for normal cloud
  applications of ML servers
  https://simpliv.wordpress.com/2018/08/14/what-is-ai/?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com
- kety question: where shoudl I deploy my e ML infereence server in a
  distributed IoT system? -->

<!-- ## building models -->
<!-- 
- converting tensorflow models to Tf lite
- wtf is the small runtime package to run the models
- wtf is quantizing a model
    -  benefits of quantizing is the reduce computation power and reduce the
       cost fo cloud computing, introduction of chips liek Coral make that
       possible 
    - specficalyl for dep learning 
    - Facebooks opens ource something
    - https://engineering.fb.com/ml-applications/fbgemm/
    - an inference server runs a model algorithm and returns the inference
      output
- possible for models that do image recog, bject detection, semantic seg, etc.
- training models is insanely compute instensive  -->

<!-- ## Competitors  -->

<!-- - drawbacks to coral onyl accepts tensorflow  -->

<!-- ## Next steps -->
<!-- 
- nexus of on device ML and cloud based ML with the added benefits of both 
- The fundamental element of heterogeneous computing is the idea that tasks can
  be performed on different types of hardware, and yield different performance
  and power efficiency.
    - opportuntiy to automate the hardware to run the inference if multiple
      options are available
    - why use CPU or DSP over a GPU when running models


https://developers.googleblog.com/2019/10/coral-moves-out-of-beta.html

https://qengineering.eu/google-corals-tpu-explained.html

https://www.makeuseof.com/tag/google-coral-dev-board-raspberry-pi/

https://coral.ai/docs/edgetpu/faq/#

https://coral.ai/about-coral/

https://coral.ai/technology/

https://blogs.nvidia.com/blog/2016/08/22/difference-deep-learning-training-inference-ai/
-->