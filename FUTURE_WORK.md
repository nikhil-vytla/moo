# Future Work & Roadmap

This document outlines potential improvements and missing features for the moo interpretability library.

## Missing Attribution Methods

| Method | Priority | Effort | Description | Reference |
|--------|----------|--------|-------------|-----------|
| **Grad-CAM / Grad-CAM++** | High | Low-Medium | Class Activation Mapping for CNNs. Most requested for computer vision. Provides class-discriminative localization. | Selvaraju et al. 2017, Chattopadhyay et al. 2018 |
| **SmoothGrad** | High | Low | Noise-based gradient smoothing. Improves visual quality of saliency maps. We have GaussianDoI infrastructure that could support this. | Smilkov et al. 2017 |
| **Expected Gradients** | High | Medium | Modern improvement on Integrated Gradients. Uses distributional baselines instead of single baseline. More robust attributions. | Erion et al. 2021 |
| **Blur Integrated Gradients** | Medium | Low-Medium | Better baselines for image models. Uses blurred versions of input rather than black/uniform baseline. | Xu et al. 2020 |
| **DeepLIFT** | Medium | Medium | Compares to reference activations. Similar to Integrated Gradients but discrete. | Shrikumar et al. 2017 |
| **Layer-wise Relevance Propagation (LRP)** | Medium | High | Backpropagates relevance scores instead of gradients. Different theoretical foundation. | Bach et al. 2015 |
| **Feature Visualization** | Medium | Medium | Optimization-based. Generates inputs that maximally activate specific neurons. Complements attribution. | Olah et al. 2017 |
| **SHAP / DeepSHAP** | Low | High | Shapley Additive Explanations. Industry standard but game-theoretic (doesn't fit gradient paradigm). Many model evaluations. | Lundberg & Lee 2017 |
| **LIME** | Low | Low-Medium | Local Interpretable Model-agnostic Explanations. Perturbation-based. Better for tabular/traditional ML than deep learning. | Ribeiro et al. 2016 |
| **Occlusion Analysis** | Low | Low | Simple perturbation-based attribution. Baseline method. Useful for sanity checking. | Zeiler & Fergus 2014 |

## Transformer-Specific Features

_Note: moo currently works with transformers via gradient-based methods on embeddings, but is missing attention-specific interpretability._

| Feature | Priority | Effort | Description | Reference |
|---------|----------|--------|-------------|-----------|
| **Attention visualization** | High | Medium | Direct access to attention weights. Visualize which tokens attend to which. Per-head and per-layer analysis. | - |
| **Attention rollout** | Medium | Low-Medium | Aggregate attention across layers. Shows effective attention from inputs to outputs. | Abnar & Zuidema 2020 |
| **Attention flow** | Medium | Medium | Traces information flow through attention. More sophisticated than rollout. | Abnar & Zuidema 2020 |
| **Influence Functions for LLMs** | Medium | High | Understanding training data impact on model predictions. Increasingly important for LLMs. | Koh & Liang 2017 |
| **Token generation attribution** | Low | Medium | Explain token-by-token generation in autoregressive models. | - |

## Architecture Support

| Architecture | Priority | Effort | Description |
|--------------|----------|--------|-------------|
| **Vision Transformers (ViT)** | Medium | Medium | Attention map visualization for image patches. Class token attribution. |
| **Diffusion Models** | Low | High | Interpretability for diffusion-based generative models (increasingly relevant). |

## Performance & Scalability

| Feature | Priority | Effort | Impact | Description |
|---------|----------|--------|--------|-------------|
| **Batch processing** | High | Medium | High | Vectorized attribution computation. Currently processes samples one at a time. |
| **GPU optimizations** | Medium | Medium | High | Framework-specific GPU acceleration. Optimize memory usage for large models. |
| **Caching** | Medium | Low-Medium | Medium | Cache intermediate results. Avoid recomputing gradients for repeated queries. |
| **Sparse attributions** | Low | Medium | Medium | Efficient handling of sparse inputs. Particularly useful for NLP. |

## Usability & Documentation

| Item | Priority | Effort | Description |
|------|----------|--------|-------------|
| **Quickstart guide** | High | Low | Simple 5-minute getting started tutorial |
| **API reference docs** | High | Medium | Auto-generated from docstrings |
| **Examples directory** | High | Low-Medium | Standalone scripts: MNIST/CIFAR-10, BERT, ResNet |
| **Comparison guide** | Medium | Low-Medium | Decision tree for choosing methods. Pros/cons of each approach |
| **Tutorial notebooks** | Medium | Medium | Debugging failures, comparative explanations, custom QoI/DoI/Slices |
| **Improved docstrings** | Medium | Low | Complete parameter documentation with examples |
| **Video tutorials** | Low | Medium | Walkthrough screencasts |
| **Interactive demos** | Low | Medium-High | Gradio/Streamlit apps |

## Evaluation & Metrics

| Metric Category | Priority | Effort | Description |
|-----------------|----------|--------|-------------|
| **Sanity checks** | High | Low-Medium | Model/data randomization tests. Verify explanations change when model changes. Essential validation. | Adebayo et al. 2018 |
| **Faithfulness metrics** | High | Medium | Deletion curves, insertion curves, infidelity metrics |
| **Completeness axiom verification** | High | Low | Verify Integrated Gradients satisfies completeness. Built-in validation for attribution methods. | Sundararajan et al. 2017 |
| **ROAR/KAR benchmarks** | Medium | Medium | Standard metrics: Remove And Retrain, Keep And Retrain. Industry-standard evaluation. | Hooker et al. 2019 |
| **Robustness checks** | Medium | Medium | Explanation stability under small input perturbations. Adversarial robustness of explanations. | Ghorbani et al. 2019 |
| **Ground truth comparison** | Medium | Low-Medium | Pointing game for localization, IoU with bounding boxes (when ground truth available) |

## Global Explanations

_All current methods are local (single-sample). Missing dataset-level insights._

| Feature | Priority | Effort | Description |
|---------|----------|--------|-------------|
| **Feature importance aggregation** | High | Low-Medium | Aggregate attributions across dataset. Which features matter most overall? |
| **Influential training examples** | Medium | High | Which training examples most affected this prediction? (Influence functions) |
| **Concept-based explanations** | Low | High | Testing with Concept Activation Vectors (TCAV). High-level concepts. Requires concept datasets. | Kim et al. 2018 |

## Ecosystem Integration

| Integration | Priority | Effort | Description |
|-------------|----------|--------|-------------|
| **Captum compatibility** | High | Medium | PyTorch's official XAI library. Interop or integration layer. Critical for PyTorch ecosystem. |
| **HuggingFace integration** | High | High | Pre-built wrappers, automatic tokenizer handling, model hub compatibility |
| **Model zoo support** | Medium | Medium | Examples for timm, torchvision, TensorFlow Hub models |
| **Export formats** | Medium | Low-Medium | NumPy, HDF5, JSON for web visualization |
| **Visualization integrations** | Low | Medium | TensorBoard, Weights & Biases, Matplotlib/Seaborn utilities |

## Advanced Features

| Feature | Priority | Effort | Description |
|---------|----------|--------|-------------|
| **Counterfactual explanations** | Medium | High | Generate minimal input changes to flip predictions. Complements attribution. |
| **Ensemble attributions** | Medium | Medium | Combine multiple methods. Uncertainty quantification over explanations. |
| **Interactive exploration** | Low | High | Real-time attribution updates. Jupyter widgets for parameter tuning |
| **Multi-task attribution** | Low | Medium | Explain multiple outputs simultaneously. Shared vs. task-specific features |

## Code Quality & Maintenance

| Item | Priority | Effort | Description |
|------|----------|--------|-------------|
| **Resolve TODOs** | High | Low | 39 TODOs scattered in codebase |
| **CI/CD pipeline** | High | Medium | Automated testing and releases |
| **Code coverage** | Medium | Medium | Increase test coverage beyond core functionality |
| **Type stub files** | Low | Low-Medium | .pyi files for better IDE support |
| **Performance benchmarks** | Low | Medium | Track speed regressions |

## Breaking Changes to Consider

| Change | Impact | Effort | Description |
|--------|--------|--------|-------------|
| **Rename `tru_logger`** | Low | Low | Now that it's "moo", should be `moo_logger` |
| **Simplify type system** | Medium | High | The typing infrastructure is very complex |
| **Modern Python features** | Medium | Medium | Require Python 3.10+ for newer syntax |

## Research Opportunities

Areas where moo's unique architecture (QoI/DoI/Slices) could enable novel research:

| Opportunity | Description |
|-------------|-------------|
| **Comparative explanations at scale** | Leverage ComparativeQoI for systematic studies of class differences |
| **Distribution-aware attributions** | Explore novel DoI implementations (e.g., learned baselines, adversarial DoIs) |
| **Internal influence deep-dive** | More applications of internal neuron attribution. What do internal features represent? |
| **Cross-framework attribution comparison** | Systematic study: Do PyTorch/TF give same attributions? Framework-specific quirks? |
| **Axiomatic attribution properties** | Verify completeness, sensitivity, implementation invariance across methods |

---

## Notes on Excluded/Deprioritized Items

**Guided Backprop**: Initially included but [research shows](https://arxiv.org/abs/1810.03292) it's essentially an edge detector, not actually attributing to model decisions. If implemented, should include strong caveats.

**GNNs**: Graph neural networks removed from scope. Would require significant new infrastructure for graph operations.

**LIME**: Kept but noted as better for tabular/traditional ML. Most deep learning practitioners prefer gradient-based methods.

**SHAP/DeepSHAP**: Lower priority due to architectural mismatch (game-theoretic vs gradient-based) and computational cost.

---

## Quick Reference: Prioritization

### 🎯 Quick Wins (High Impact, Low Effort)
- **SmoothGrad** - Leverage existing GaussianDoI infrastructure
- **Quickstart guide** - Critical for adoption
- **Resolve TODOs** - Code quality
- **Sanity checks** - Essential validation
- **Feature importance aggregation** - Easy dataset-level insights

### 🚀 Strategic Investments (High Impact, Medium Effort)
- **Grad-CAM** - Most requested for computer vision
- **Attention visualization** - Critical for transformers
- **Batch processing** - Major performance win
- **Expected Gradients** - Modern, better IG
- **Captum compatibility** - PyTorch ecosystem integration
- **API reference docs** - Professional polish

### 🏗️ Long-term Goals (High Impact, High Effort)
- **HuggingFace integration** - Full ecosystem integration
- **Comprehensive evaluation metrics** - ROAR, robustness, influence functions
- **LRP implementation** - Different theoretical foundation
- **Global explanations framework** - Dataset-level insights

---

## Contributing

If you're interested in contributing any of these features:

1. **Open an issue** to discuss the approach
2. **Check existing work** - someone may already be working on it
3. **Follow code patterns** - use the QoI/DoI/Slice architecture
4. **Add tests** - all new attribution methods need tests
5. **Update documentation** - examples and docstrings
6. **Verify axioms** - if implementing attribution, verify it satisfies expected properties
