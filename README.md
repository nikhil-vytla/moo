# moo 🐮

**moo** is a neural network interpretability library designed to help you understand and explain deep learning model predictions through gradient-based attribution methods.

## What is moo?

Deep neural networks are often treated as black boxes, making it difficult to understand why they make particular predictions. **moo** provides tools to open up these black boxes by computing *attributions* - quantitative measures of how much each input feature or internal neuron contributed to a model's output.

The library supports multiple deep learning frameworks (PyTorch, TensorFlow, Keras) through a unified API, making it easy to apply interpretability techniques regardless of which framework you use.

## Core Concepts

**moo** is built around three key concepts that give you fine-grained control over your explanations:

- **Quantity of Interest (QoI)**: What behavior do you want to explain? This could be the model's prediction for a specific class, a comparison between two classes, or any custom function of the model's output.

- **Distribution of Interest (DoI)**: Over what set of inputs should the explanation be faithful? This could be a single point (local explanation), a linear interpolation path (as in Integrated Gradients), or a distribution around the input.

- **Slice/Cut**: At what level of abstraction do you want the explanation? You can compute attributions for input features, or for internal neurons at any layer of the network, allowing you to understand both low-level features (like edges) and high-level features (like object parts).

## Key Features

- **Multiple Attribution Methods**: Integrated Gradients, Internal Influence, gradient-based saliency maps, and more
- **Multi-Framework Support**: Works with PyTorch, TensorFlow v1/v2, and Keras models through unified model wrappers
- **Internal Attributions**: Explain not just inputs, but internal neurons and feature maps
- **Flexible API**: Simple defaults for common use cases, with full control for advanced users
- **Visualization Tools**: Built-in visualizers for creating attribution heatmaps and masks

## Use Cases

- Understand why a classifier chose a particular class
- Identify which pixels in an image were most important for a prediction
- Discover which internal feature maps drove a decision
- Compare explanations between different output classes
- Debug model behavior and identify potential biases

## Acknowledgements

**moo** is a continuation of the [**trulens-explain**](https://github.com/truera/trulens_explain) library, created by the TruEra Research team. I really enjoyed contributing to and using TruLens during my time at TruEra, and since `trulens-explain` is no longer actively maintained, I’m launching **moo** in the hopes of carrying forward and expanding on the foundational research behind the original library.

The core attribution methods implemented in this library are based on the following research:

- **Internal Influence**: Klas Leino, Shayak Sen, Anupam Datta, Matt Fredrikson, and Linyi Li. "[Influence-Directed Explanations for Deep Convolutional Networks](https://arxiv.org/abs/1802.03788)." IEEE ITC 2018.
- **Integrated Gradients**: Mukund Sundararajan, Ankur Taly, and Qiqi Yan. "[Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365)." ICML 2017.
- **Gradient-based Saliency Maps**: Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. "[Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034)." ICLR 2014.

I’m deeply grateful to the original authors and contributors of `trulens-explain`—many of whom I had the pleasure of working with—for making their work publicly available and advancing the field of neural network interpretability.

## Why moo? 🐄

It's an inside joke! 🤭
