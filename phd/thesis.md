## Where are you?

This is an experiment in creating an open kind of thesis. I would like to work together using the nonprofit <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> toolkit to annotate this living document, for which we'll track changes using [git](www.github.com/spewil/). In less than two years, this page will represent the culminated collective effort of a few people to better understand the organizing principles of human motor learning.

To start adding comments to this page, just highlight some text, click `annotate` and start typing. Note that you will have to a <a href="https://web.hypothes.is/" target="_blank">Hypothes.is</a> account, but it only takes a second.

## What am I doing?

I'm working on my PhD at the Sainsbury Wellcome Centre for Neural Circuits and Behavior in London. I'm setting up a family of experiments that I hope will test hypotheses about the organizing principles of sensorimotor control and learning. I'm setting up a task where I record from participants' muscles in their arms and hands using `electromyography`. Subjects' arms and hands are fixed in a brace, but as they send signals from their brain down to their spinal cords and ultimately to their muscles, my electrodes will sense this change in electrical potential and relay this change to the computer, which will reflect these changes through visuals shown on a screen. The object of the game is for the participant to learn which muscle activations correspond to which changes in the visual scene. You can think about this as a video game you're playing directly with your muscles.

## PhD Timeline

- Year 1 (October 2018 - October 2019)
  - coursework (October 2018 - March 2019)
  - <a href="/phd/rotations/mouse_ball.html" target="_blank">mouse wheel task in Mrsic-Flogel Lab</a> (Jan 2019 - March 2019)
  - <a href="/phd/rotations/ctrl-labs.html" target="_blank">ctrl-labs rotation in NYC</a> (April 2019 - June 2019)
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

> The processes by which biological control solutions spanning large and continuous state spaces are constructed remain relatively unexplored. Future investigations may need to embed rich dynamical interactions between object dynamics and task goals in novel and complex movements [@McNamee2019].

We know surprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on.

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions.

# Test

## Anatomy of the Hand and Forearm

the deep flexor attaches to the distal phalanx
the superficial flexor attaches to the middle phalanx

A Citation:
[@todorovCompositionalityOptimalControl2009@todorovParallelsSensoryMotor]

An inline Footnote:

First Note ^[Hi I'm a note!]

A longer note:

Long Note[^]

[^]: This is a longer note that we've indented to make sure that it is formatted properly at the end of the document.

Some more text, not in a footnote

# Background

## What are muscles?

Muscles are collections of fibers that contract when chemical gradients are produced at the neuromuscular junction by action potentials emanating from neurons in the ventral horn of the spinal cord.

## What is electromyography?

Electromyography is the detection of changes in chemical potential using electrodes. In my setup, we use a total 64 monopolar surface electrodes and monopolar needle electrodes to record chemical potentials from muscles in the forearm and hand.

## What is our current understanding of how humans control their bodies?

## Task Formalization

In this task, the subject's first goal is to interact through an unknown visuomotor mapping and internalize this model. The second problem is to use this model to solve a control problem.

1. System Identification -- learning a transition function $p(y_t|x_t, u_t)$
    - How do you learn the unknown observation model from data?

2. Policy Optimization
    - Once dynamics are learned (or at least stable?), how do we form a policy that is generalizable to new tasks under these dynamics?
    - This is the control problem.

It's safe to assume that these processes are happening in parallel. Because we have complete and arbitrary control over the observation mapping, we can ask the subject to interact through a  dynamic that is intuitive (informative prior) or unintuitive (uninformative or inhibitive prior). Each scenario, we hypothesize, will elicit different strategies for learning and control.

The unknown mapping $M$ from muscle to task space looks like the observation matrix $H$ in the LQG problem:

$$
\begin{align*}
y_t &= Hx_t + v_t\,\,\,(\mathrm{LQG}) \\
y_t &= Mx_t + v_t. \,\,\,(\mathrm{experiment})
\end{align*}
$$

The state dynamics in the task are of the form:

$$
\begin{align*}
x_{t} &= Ax_{t-1} + Bu_{t-1} + w_{t-1} \,\,\,(\mathrm{LQG}) \\
x_t &= Dx_{t-1} + Iu_{t-1} + w_{t-1} \,\,\,(\mathrm{experiment})
\end{align*}
$$

where $D$ is a diagonal decay matrix of with terms $\mathrm{e}^{-\lambda}$ and $I$ is the identity. The subject produces muscle contractions which add to the current latent (unobserved) state. In the absence of control signals, the state decays back to $0$ in line with the physics of your arm returning to a passive state in the absence of muscle contractions. The terms $w$ and $v$ are gaussian noise vectors with distributions $\mathcal{N}(0,Q)$ and $\mathcal{N}(0,R)$. If we combine the transition and observation models:

$$
\begin{align*}
y_t &= MDx_{t-1} + Mu_{t-1} + Mw_{t-1} + v_t \\
&= A^\prime x_{t-1} + B^\prime u_{t-1} + Mw_{t-1} + v_t.
\end{align*}
$$

We can think of this as the combined system identification problem where $A^\prime=MD$ and $B^\prime=M$ are unknown and must be estimated. The noise covariances of this altered system are now non-trivial, however. We could also assume that the transition dynamic $D$ is known and that the identification problem is learning the mapping $M$ only. This might not be a poor assumption since the exponential decay is meant to serve as an intuitive passive dynamic.

In each trial of the task, a subject will have some internal representation of the observation dynamic $M$ which may or may not be accurate. In order to make accurate predictions, $M$ must be estimated.

Learning linear dynamical systems from data is a hot topic of research, most of which seems to focus on learning in the context of complete state observation ($M=I$, $y=x$). Algorithms to determine parameters of $A$ and $B$ are proposed (see Dean, Recht 2018).

From LQG theory we know that the control law is a linear function of the state:

$$
\begin{align*}
u_t = -L_tx_t
\end{align*}
$$

and thus our combined system dynamic is:

$$
\begin{align*}
y_t &= M(D-L_t)x_{t-1} + Mw_{t-1} + v_t.
\end{align*}
$$

The noise covariance due to the observation Q is unchanged, but the new noise covariance for the latent process is now $MRM^T$. This may make things difficult.

#### Questions

- In a behavioral experiment, how can you disentangle system identification/estimation and control? Is suboptimality due to one or the other?
- How does the observation mapping relate to the latent state covariance? The task state covariance?
- How do we formalize this into a probabilistic graphical model? Why would we?
    - Would this make it easier to reason about what the goals are?
    - Would learning $M$ become an inference problem?
    - Would solving the control problem become an inference problem...?
- What noise assumptions can we make? Can we not make?
    - How can we incorporate signal-dependent noise?

### Model-based Reinforcement Learning

Since we only have an approximate model of the system dynamic, we could simply work towards an optimal policy directly using gradient derivative-free optimization methods in a model-free approach. Since we have good evidence that humans leverage internal models to make decisions (at least in a motor problem domain), we need to define an algorithm which uses past observations and controls to update our approximation for the system dynamic. Here is a very general algorithm:

0. Define a base policy/controller and base system model ($L_0$ and $\hat{M}_0$)
1. Collect samples (by interacting with the true environment $M_{true}$) using the current policy/controller (collect $y_t,u_t,y_{t+1}$ triples using $L_i$ for $i \in \{0\dots N\}$
2. Use sample(s) / trajectories to update current system dynamical model $\hat{M}_i$
3. Update current policy/controller $L_i$ (using the system dynamics or using a direct policy method)

If the true system dynamics were known, we could solve the Algebraic Riccati Equation with a backwards pass, and compute our controls in a forward pass. This general algorithm structure highlights how the (unknown) system identification and controller design are intertwined: identifying a system appropriately must rely on sampling and fitting regions of the state space pertinent to adequate control in terms of cost (Ross ICML 2012). Otherwise, our approximation to the true system dynamic will only produce a valid controller in regions we have previously explored. The question is how we can effectively (sample and time efficiently) utilize new state transitions we encounter either online as feedback or between trials to update our model and policy. That is, the number of trials and/or trajectories to use before updating either the system model and/or policy is an important parameter.

In the LQG setting, this might be called "adaptive LQG".

#### Questions

- how does a subject sample the state space as to efficiently learn? do they sample optimally? how does controller/policy optimization proceed based on system identification?
- how does a human subject use error information from each trial and feedback from each time step to update their model and/or policy?
    - how does a subject balance policy updates with model updates?
- On what scale (trials, timesteps) is the model altered? the policy?
    - Replanning at every timestep is a model predictive control algorithm
    - What prediction can we make for ID/learning every trial?
- how does a subject avoid "distribution mismatch" between their base policy and their optimal policy? How do they efficiently explore and use this new data to update their internal model?
    - what exploration strategy does a subject use to avoid mismatch?
    - what
- What is a subject's baseline/prior model? $y_{t} = \hat{f}_0(x_t,u_t)$ or $y_{t} \propto p_0(y_t|x_{t},u_t)$
- What is the base policy / prior policy? $u_t = \pi_0(\hat{x}_t)$
- How do we think about learning a distribution over trajectories in control law space, or perhaps equivalently, in covariance/precision space?
- We might hypothesize that a subject will act as randomly as possible while minimizing cost, a maximum entropy solution that converges to an optimal controller? $\mathcal{H}(p(u_t|x_t))$
- How does a subject penalize changes to their controllers? Do they follow a KL-divergence type of measurement when improving their policy?

## Modeling Error-based Learning with Linear Dynamical Systems

*Modeling Sensorimotor Learning with Linear Dynamical Systems* by Cheng and Sabes, 2006. The goal is to model trial-by-trial learning by fitting data to a linear dynamical system model. Here we'll call $F_t$ the **sensorimotor mapping** transforming inputs $w_t$ to $y_t$ outputs per trial:

$$
y_t = F_t(w_t, \gamma_t).
$$

This can be thought of as a mapping from inputs within a single trial to, for example, endpoint error. Noise is captured by the $\gamma_t$. The trajectory in $F$ space attempts to capture the process of learning. The learning rule $L_t$ can be written

$$F_{t+1} = L_t\left(\left\{F_\tau\right\}_{\tau=1}^{t}, u_t, \eta_t, t\right)$$

where $\left\{F_\tau\right\}_{\tau=1}^{t}$ is the history of the mapping, $u_t$ is the history of the total inputs to learning which could encompass $y$, $w$, and exogenous inputs $r$. Noise in the learning is captured by $\eta$.

We can approximate this learning problem using linear equations by assuming that $L_t=L \ \forall \ t$ is stationary, $F_t$ is parameterized by $x_t\in\mathbb{R}^y$. Thus,

$$
\begin{aligned}
y_t &= F(x_t, w_t, \gamma_t) \\
x_{t+1} &= L(x_t, u_t, \eta_t).
\end{aligned}
$$

The trial-to-trial input-output mapping $F$ is now fixed, and is transformed by trial through its parameters $x_t$ by $L$. Note that both mappings are Markovian and there are two input vectors, one for within-trial and one between-trial. These can include overlap. We can now linearize these mappings around an equilibrium point:

$$
\begin{aligned}
x_{t+1} - x_e &= A(x_t-x_e) + B(u_t-u_e) + \eta_t \\
y_t - m_e &= C(x_t-x_e) + D(w_t-w_e) + \gamma_t
\end{aligned}
$$

As shown by Cheng and Sabes, we can bundle the equilibrium terms into a bias term and drop this term if we mean-subtract our data ($x_t, y_t, u_t, w_t$) when it's time to fit. This gives us a simple linear dynamical system:

$$
\begin{aligned}
x_{t+1} &= Ax_t + Bu_t + \eta_t \\
y_t &= Cx_t + Dw_t + \gamma_t.
\end{aligned}
$$

The first equation governs the evolution of parameters of the within-trial input-output mapping, while the second equation governs the trial output given the current within-trial mapping parameters $x_t$ and learning inputs $w_t$. The parameters $x_t$ are hidden variables that are only observed through the output $y_t$. The noise terms $\eta_t$ and $\gamma_t$ are normally distributed with covariances $Q$ and $R$, respectively. $A$ governs the passive trajectory of $x_t$. If $A=\mathbb{I}$, $x_t$ does not decay passively.

There is a general form for this model which separates endogenous input $y_t$ from exogenous input $r_t$

$$
\begin{aligned}
x_{t+1} &= Ax_t + [G \ H][r_t \ y_t]^T + \eta_t \\
y_t &= Cx_t + Dw_t + \gamma_t
\end{aligned}
$$

where $H$ governs biases in directions of the outputs. A unbiased output is isotropic. To add
explicit stationary bias we write

$$
\begin{aligned}
x_{t+1} &= Ax_t + Gr_t + Hy_t - Hb_x + \eta_t.
\end{aligned}
$$

### Example Models

#### Feedback Error Learning

$$x_t+1 = Ax_t + [H\ H][-y_t^*\ y_t]^T$$

The second term is simply the difference between the output $y_t$ and the desired output $y_t^*$.

#### Prediction Error Learning

Let $u_t = y_t - \hat{y}_t$ where $\hat{y}_t$, the difference between the output and the predicted output such that

$\hat{y}_t = Cx_t + Dw_t$. Thus,$\hat{y}_t$ is a kind of forward model. Plugging in,

$$x_{t+1} = Ax_t + Bu_t + \eta_t$$

becomes

$$
\begin{aligned}
x_{t+1} &= Ax_t + B(y_t - Cx_t - Dw_t) + \eta_t \\
x_{t+1} &= (A-BC)x_t + By_t - BDw_t + \eta_t
\end{aligned}
$$

#### Target Prediction Error Learning

Now let $u_t = \hat{y}_t - y^*_t$, the difference between predicted
output and target output.

$$
\begin{aligned}
x_{t+1} &= Ax_t + B(Cx_t + Dw_t - y^*_t) + \eta_t \\
x_{t+1} &= (A+BC)x_t + BDw_t - By^*_t + \eta_t
\end{aligned}
$$

#### Steady State

If we take the output and state vectors in expectation for constant
inputs $w$ and $r$, we have

$$
\begin{aligned}
y_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Cx_\infty + Dw\right] \\
x_\infty &= \lim_{t\to\infty}\mathbb{E}\left[Ax_\infty + Bu\right] \\
&= Ax_\infty + Gr + Hy_\infty \\
&= Ax_\infty + Gr + HCx_\infty + HDw \\
-(A + HC - \mathbb{I})x_\infty &= HDw + Gr.
\end{aligned}
$$

Thus, the
eigenvalues of $A + HC$ must be less than or equal to 1 for $x_\infty$
to be stable in expectation.

### Critique

> It should be emphasized, however, that these models are not intended to provide a mechanistic explanation of adaptation—they do not explain why adaptation has the properties it does. They explain neither why compensation for a perturbation decays, nor why people learn at the rate they do. However, these models do encapsulate a set of simple assumptions about how learning might occur on a single-trial timescale, and allow us to predict behavior in response to sustained or fluctuating perturbations over many trials. (Krakauer)

> [Bayesian theories of learning] hold that adaptation is essentially a problem of estimating the properties of the imposed perturbation, given uncertainty about sensory feedback and the state of the world. Mathematically, under certain assumptions (that the noise/variability is Gaussian in both cases), this Bayesian estimation framework becomes equivalent to a Kalman filter (219)—a common algorithm for optimally tracking dynamic states under noisy observations— which is almost identical to a state-space model. (Krakauer)


## Two-rate models

$$
\begin{align*}
X_{t+1} &= X^{s}_{t} + X^f_t \\
X^s_{t+1} &= L_s \cdot e_t + R_s \cdot X^s_{t} \\
X^f_{t+1} &= L_f \cdot e_t + R_f \cdot X^f_{t} \\
\end{align*}
$$

where we fit $L_i and R_i$, the learning rate and retention parameters. (shadmehr 2006)

> Observations have revealed that there is far more to how participants compensate for an imposed perturbation than just implicit recalibration of a pre-existing motor controller. Instead, multiple, qualitatively different processes occur during adaptation tasks; for example, processes driven by explicit, cognitive strategies. When it comes to studying implicit recalibration, these other processes can be a contaminant. At the same time, however, these additional processes likely reflect the involvement of similar mechanisms to those responsible for more general motor skill learning. (Krakauer 2019 Motor Learning Review)

> it is unlikely that the underlying components that contribute to learning in adaptation paradigms only differ in terms of their learning and retention rates, as the two- state model suggests. The multiple components of learning instead correspond to entirely distinct learning processes that are simultaneously brought to bear on the same problem. (Krakauer 2019 Motor Learning Review)

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

## Bibliography
