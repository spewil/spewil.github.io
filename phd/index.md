- [What am I looking at?](#what-am-i-looking-at)
- [What am I doing?](#what-am-i-doing)
- [What are muscles?](#what-are-muscles)
  - [What is electromyography?](#what-is-electromyography)
- [What is our understanding of how humans control their bodies?](#what-is-our-understanding-of-how-humans-control-their-bodies)
  - [Optimal control theory](#optimal-control-theory)
- [A cat](#a-cat)
- [Bibliography](#bibliography)

## What am I looking at?

This is an experiment in creating an open kind of thesis. I would like to work together using the nonprofit <a href="https://web.hypothes.is/">Hypothes.is</a> toolkit to annotate this living document, for which we'll track changes using [git](www.github.com/spewil/). In less than two years, this page will represent the culminated collective effort of a few people to better understand the organizing principles of human motor learning.

To start adding comments to this page, just highlight some text, click `annotate` and start typing. Note that you will have to a <a href="https://web.hypothes.is/">Hypothes.is</a> account, but it only takes a second.

## What am I doing?

I'm working on my PhD at the Sainsbury Wellcome Centre for Neural Circuits and Behavior in London. I'm setting up an experiment that I hope will test hypotheses about the organizing principles of sensorimotor control and learning. I'm setting up a task where I record from participants muscles in their arm using `electromyography`. Subjects' arms and hands are fixed in a brace, but as they send signals from their brain down to their spinal cords and ultimately to their muscles, my electrodes will sense this change in electrical potential and relay this change to the computer, which will update what is shown on the screen. The object of this game is for the participant to learn which muscle activations correspond to which changes in the visual scene. You can think about this as a video game you're playing directly with your muscles.

Why would I want to do this? Because we know suprisingly little about how this process unfolds in the brain. So little, in fact, that we haven't quite figured out what the brain is actually doing. We know that it is involved in these muscle contractions, but what sort of strategy do you use to explore this space of possible mappings between what you experience when you move and what you expect to see and feel as a result? This is the question I hope to make headway on. 

To do this, I'll use the literature of reinforcement learning and optimal control theory to guide my theoretical understanding of what is happening when a subject begins to experience learning in this novel situation. I will model hypotheses of this learning process and compare these models to the large amounts of data my experimental setup will produce as we track learning of subjects over many sessions. 

## What are muscles?

Muscles are collections of fibers that contract when chemical gradients are produced at the neuromuscular junction by action potentials emanating from neurons in the ventral horn of the spinal cord.

### What is electromyography?

Electromyography is the detection of changes in chemical potential using electrodes. In my setup, we use a total 64 monopolar surface electrodes and monopolar needle electrodes to record chemical potentials from muscles in the forearm and hand.

## What is our understanding of how humans control their bodies?

### Optimal control theory

A key paper is `Valero-Cuevas 2009` which recording EMG from the seven muscles driving the finger in a force-feedback task. The authors found support for the "minimum intervention principle" [@Valero-Cuevas2009].

## A cat

![this is a cat](cat.jpg)

## Bibliography