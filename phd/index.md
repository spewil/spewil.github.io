- [Meta](#meta)
  - [Where are you?](#where-are-you)
  - [What am I doing?](#what-am-i-doing)
  - [PhD Timeline](#phd-timeline)
- [Purpose](#purpose)
- [Background](#background)
  - [What are muscles?](#what-are-muscles)
  - [What is electromyography?](#what-is-electromyography)
  - [What is our understanding of how humans control their bodies?](#what-is-our-understanding-of-how-humans-control-their-bodies)
- [Theory](#theory)
  - [Optimal Control Theory](#optimal-control-theory)
  - [Unsupervised Feature Extraction](#unsupervised-feature-extraction)
- [Experiment](#experiment)
- [Modeling](#modeling)
  - [Bibliography](#bibliography)

# Meta

## Where are you?

This is an experiment in creating an open kind of thesis. I would like to work together using the nonprofit <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> toolkit to annotate this living document, for which we'll track changes using [git](www.github.com/spewil/). In less than two years, this page will represent the culminated collective effort of a few people to better understand the organizing principles of human motor learning.

To start adding comments to this page, just highlight some text, click `annotate` and start typing. Note that you will have to a <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> account, but it only takes a second.

## What am I doing?

I'm working on my PhD at the Sainsbury Wellcome Centre for Neural Circuits and Behavior in London. I'm setting up a family of experiments that I hope will test hypotheses about the organizing principles of sensorimotor control and learning. I'm setting up a task where I record from participants' muscles in their arms and hands using `electromyography`. Subjects' arms and hands are fixed in a brace, but as they send signals from their brain down to their spinal cords and ultimately to their muscles, my electrodes will sense this change in electrical potential and relay this change to the computer, which will reflect these changes through visuals shown on a screen. The object of the game is for the participant to learn which muscle activations correspond to which changes in the visual scene. You can think about this as a video game you're playing directly with your muscles.

## PhD Timeline

- Year 1 (October 2018 - October 2019)
  - coursework (October 2018 - March 2019)
  - <a href="mouse_ball.html" target="_blank">mouse wheel task in Mrsic-Flogel Lab</a> (Jan 2019 - March 2019)
  - <a href="ctrl-labs.html" target="_blank">ctrl-labs rotation in NYC</a> (April 2019 - June 2019)
  - <a href="https://www.sainsburywellcome.org/web/groups/murray-lab" target="_blank">MurrayLab rotation</a> (July 2019 - August 2019)
  - <a href="https://github.com/swcphd/greyboxes" target="_blank">Organize SWC PhD Bootcamp</a> (September 2019)

- Year 2 (October 2019 - October 2020)
	- list of thesis committee members
	- project proposal with literature search
	- data club presentation / 6-month review (May)
	- SfN poster introducing setup, concept
	- final draft of project proposal
	- introduction and background chapters
	- upgrade / 2nd year review (October)
	- preliminary task data
- Year 3 (October 2020 - October 2021)
	- finer-grained experiments, supporting experiments
	- theory chapter
	- modeling chapter
- Year 4 (October 2020 - October 2021)

# Purpose

We know suprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on.

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions.

# Background


## What are muscles?

Muscles are collections of fibers that contract when chemical gradients are produced at the neuromuscular junction by action potentials emanating from neurons in the ventral horn of the spinal cord.

## What is electromyography?

Electromyography is the detection of changes in chemical potential using electrodes. In my setup, we use a total 64 monopolar surface electrodes and monopolar needle electrodes to record chemical potentials from muscles in the forearm and hand.

## What is our understanding of how humans control their bodies?

# Theory

## Optimal Control Theory

A key paper is `Valero-Cuevas 2009` which recording EMG from the seven muscles driving the finger in a force-feedback task. The authors found support for the "minimum intervention principle" [@Valero-Cuevas2009].

## Unsupervised Feature Extraction

We want to determine a redundant control space from data taken during natural activity. The difficulty with this is that such a natural activity manifold may display spatial (channel-wise) correlations that are possibly physiologically separable. Thus, there are two aims   which must be addressed separately:

1. Expore subjects' ability to decorrelate descending output to the muscles which have been shown to be correlated in a natural activity dataset.
    - Such a structured exploration might provide support for the hypothesis that "synergies" are flexible correlations between muscles driven by task demands rather than (or in addition to) physiological structure. This needs to be done incredibly carefully to escape criticism of hard-wired synergy enthusiasts.
    - See *de Rugy 2012* for a critique of OFC and hard-wired synergies
2. Use common correlated outputs to develop a family of BMI-type learning tasks as a proxy for a "novel skill", then track motor planning of this new skill to compare with motor planning algorithms.
    - We might be able to get #1 for free by going after this goal if we're careful in the setup
    - This is arguably a more impactful focus as it connects low-level motor hierarchy data (EMG) to high-level planning with a normative hypothesis.

Electrode data from a single trial of a single session is held in a data matrix $X$ (n_electrodes, n_samples), and we wish to find a latent weight matrix $W$ (n_electrodes, n_components) which reconstructs $X$ by projecting latent trajectories $H$ (n_components, n_samples) into electrode space:

$$
X = W\cdot{H}
$$

$H$ is the activity of the latent processes, and $W$ is there mixing matrix. The columns of $W$ are the principal vectors spanning the latent subspace in electrode space. If we have new samples, we can project these new points onto this subspace:

$$
h_{new} = W^T\cdot{w_{new}}
$$

To justify this decomposition, we have to make some assumptions about the nature of the EMG signal, namely that the signal is linear instantaneous (each EMG sample can be instantly mapped to control space). The other assumption is that the basis $W$ should be orthonormal, that the columns of $W$ are orthogonal with unity norm. This ensures that the left inverse $W^{-1}$ is equal to the transpose $W^T$ such that:

$$
\begin{align}
X &= W\cdot{H} \\
W^{-1}\cdot{X} &= {H} \\
W^{T}\cdot{X} &= {H}
\end{align}
$$

See *Muceli 2014* for use of the Moore-Penrose pseudoinverse in place of the transpose when the columns of $W$ do not form an orthonormal basis. This would be the case for NMF. Is there a factorization that produces nonnegative, orthogonal coordinates? Or is the pseudoinverse okay? I will need to test this.

Stated in an information theoretic way, we want to minimize the reconstruction loss $\mathcal{L}$ for our derived encoder-decoder pair ($E$,$D$). We're decoding high dimensional activity into its latent dimensions, and encoding back into the high dimensional space. :

$$
\min_{E,D}{\mathcal{L}\left[X - EDX\right]}
$$

This way, forget about orthonormality and solve for an encoder and decoder directly. That is, $E\neq{D}$ is perfectly acceptable.

Each row of $D$ might be called a **spatial filter**, a linear combination of electrode activities into a surrogate, hopefully more intuitive space.

In general to find such a basis we must :

- Extract "natural activity manifold" from freeform data
- Use features of this natural subspace to derive control mapping
  - Linear iid features:
    - PCA
    - dPCA
    - NMF
    - ICA
  - Linear time-dependent features:
    - SSA
    - LDS model / PGM
  - Nonlinear
    - autoencoders
    - networks

The behaviors present in our calibration dataset are crucial, as they determine the spatial correlations used to generate the mapping. If only complex, multi-muscle movements are present in the calibration, it will be impossible to decode subtle movements involving few muscles. Additionally, because extraction is unsupervised, it will be impossible to know how to alter the control basis directions (if we wish to do so) such that they involve single muscles or the smallest sets of muscles.

Ultimately, we want to find reproducible features in our data that are due to muscle coordination alone, rather than volitional movements. We want the lowest level covariance that reflects physiology rather than a task-level behavioral description (see *Todorov, Ghahramani 2005* and *Ingram, Wolpert 2009*). The idea is that if we collect data from enough tasks, we can extract the common modes of muscle activity. This is true only if we are sampling uniformly from the space of tasks. Otherwise one task, and therefore one coordination pattern, will be overrepresented.

# Experiment

# Modeling

## Bibliography