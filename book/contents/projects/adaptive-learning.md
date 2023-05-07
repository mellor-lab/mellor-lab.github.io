# Cortical networks and cholinergic adaptive learning

These projects led by [Heng Wei Zhu](../our-team/members/hengweizhu) in collaboration with Rui Ponte Costa's group aim to bridge the gap between machine learning and neuroscience by exploring whether machine learning concepts can be implemented with features of biological networks.


### `Single-phase deep learning in cortico-cortical networks`

::::{grid} 1 2 2 2

:::{grid-item}

  
&nbsp;  
```{image} ../img/projects/burstccn.png 
:class: bg-transparent no-scaled-link
:align: center
```
:::

:::{grid-item}

We aim to investigate how well-established properties of cortical networks can be integrated 
into network models to enable error backpropagation-like learning in the brain. 

To do this we use PyTorch to implement novel models of how the brain can learn in a backprop-like manner 
by integrating known properties of cortical networks namely bursting activity, short-term plasticity (STP) 
and dendrite-targeting interneurons. 
This work generates circuit to systems level predictions that can be experimentally tested. [article](https://arxiv.org/pdf/2206.11769.pdf)  
:::


::::
---

### `Cholinergic-mediated adaptive learning in cortical microcircuits` 

::::{grid} 1 2 2 2

:::{grid-item}

We aim to develop a biologically plausible deep learning network with a role for cholinergic neuromodulation that is consistent with experimental findings. 
We model the cholinergic system as an adaptive learning module that modulates synaptic plasticity in a plausible backprop-like network. 

This network consists of a canonical microcircuit with pyramidal cells and SST interneurons that are modulated by acetylcholine to gate synaptic plasticity. 
Predictions made by this model are examined using ex vivo brain slice electrophysiology with a dual optogenetics approach.  

:::

:::{grid-item}


&nbsp; 
```{image} ../img/projects/dual_opto_ach.png 
:class: bg-transparent no-scaled-link
:align: center
```

:::


::::

&nbsp;


