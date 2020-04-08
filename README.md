# EEGLearn

## 1 Project Introduction

I want to learn data processing skills in electroencephalogram(EEG) research. I chose the essay [Learning Representations from EEG with Deep Recurrent-Convolutional Neural Networks](https://arxiv.org/pdf/1511.06448v3.pdf). I referred to the comprehensive information and tools [paperwithcode](https://paperswithcode.com/paper/learning-representations-from-eeg-with-deep) provided.

## 2 Research Introduction

### 2.1 Paper Introduction

#### 2.1.1 Abstract

They focused on mental-load classification.

Use a deep recurrent-convolutional network.

> One of the challenges in modeling cognitive events from electroencephalogram (EEG) data is finding representations that are invariant to inter- and intra-subject differences, as well as to inherent noise associated with such data. Herein, we propose a novel approach for learning such representations from multi-channel EEG time-series, and demonstrate its advantages in the context of mental load classification task. First, we transform EEG activities into a sequence of topology-preserving multi-spectral images, as opposed to standard EEG analysis techniques that ignore such spatial information. Next, we train a deep recurrent-convolutional network inspired by state-of-the-art video classification to learn robust representations from the sequence of images. The proposed approach is designed to preserve the spatial, spectral, and temporal structure of EEG which leads to finding features that are less sensitive to variations and distortions within each dimension. Empirical evaluation on the cognitive load classification task demonstrated significant improvements in classification accuracy over current state-of-the-art approaches in this field.
>
> -------------[Pouya Bashivan](https://arxiv.org/search/cs?searchtype=author&query=Bashivan%2C+P), [Irina Rish](https://arxiv.org/search/cs?searchtype=author&query=Rish%2C+I), [Mohammed Yeasin](https://arxiv.org/search/cs?searchtype=author&query=Yeasin%2C+M), [Noel Codella](https://arxiv.org/search/cs?searchtype=author&query=Codella%2C+N)

#### 2.2.2 The Approach Outline

![EEG Learn](/Users/aronqi/Desktop/EEG Learn.png)

### 2.2 Making images from EEG time series

#### 2.2.1 Project the 3D electrodes distribution to a 2D surface

> The EEG electrodes are distributed over the scalp in a three-dimensional space. In order to trans- form the spatially distributed activity maps as 2-D images, we need to first project the location of electrodes from a 3-dimensional space onto a 2-D surface

Use polar projection (Azimuthal Equidistant Projection, AEP). This method can preserve the relative distance between neighboring electrodes.

What is Azimuthal Equidistant Projection?

Here is an example:

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Azimuthal_equidistant_projection_SW.jpg/300px-Azimuthal_equidistant_projection_SW.jpg)

Looking at this picture. We notice two things:

1. The center of the picture is the North Pole
2. If we define $s$ as the distance traveling on the ball surface, the proportion of $s$ doesn't change. For example, if the surface distance from North Pole to New York is $s_1$, the surface distance from North Pole to Beijing is $s_2$, then $k_s=s_1/s_2$ doesn't change when coverting the 3D coordinates into a 2D map.
3. Similarly, the relative latitude doesn't change.

This is its mathematical process:

![Screen Shot 2020-04-07 at 22.27.29](/Users/aronqi/Library/Application Support/typora-user-images/Screen Shot 2020-04-07 at 22.27.29.png)

1. Choose a point on the globe as "the center". I chose (0,0,0). It will project to (0,0) in a 2D map.
2. Pick a point in 3D space $(x,y,z)$. Its spherical coordinates are $r=\sqrt{x^2+y^2+z^2},\phi=arc\;cot(\frac{z}{\sqrt{x^2+y^2}}),\theta=arc\;cot(\frac{x}{y})$
3. 

## Related git works

1. [kylemath](https://github.com/kylemath)/**[DeepEEG](https://github.com/kylemath/DeepEEG)**

2. [VDelv](https://github.com/VDelv)/**[EEGLearn-Pytorch](https://github.com/VDelv/EEGLearn-Pytorch)**

3. [ViacheslavBobrov](https://github.com/ViacheslavBobrov)/**[EEG_RNN_Conv_Learning](https://github.com/ViacheslavBobrov/EEG_RNN_Conv_Learning)**

## References

1. [Learning Representations from EEG with Deep Recurrent-Convolutional Neural Networks](https://arxiv.org/abs/1511.06448)

