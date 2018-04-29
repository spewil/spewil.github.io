---
layout: post
title:  "social hope"
date:   2018-04-29
categories: weeklies
---

[Philosopher Richard Rorty](https://en.wikipedia.org/wiki/Richard_Rorty)

>Rorty tied this brand of philosophy to the notion of "social hope"; he believed that without the representationalist accounts, and without metaphors between the mind and the world, human society would behave more peacefully. He also emphasized the reasons why the interpretation of culture as conversation, constitutes the crucial concept of a "postphilosophical" culture determined to abandon representationalist accounts of traditional epistemology, incorporating American pragmatist naturalism that considers the natural sciences as an advance towards liberalism.

<br><br>

[why isn't everybody rich?](https://money.stackexchange.com/questions/94671/why-isnt-everybody-rich)

>- Understand that you cannot duplicate your parent's household immediately. It took them 20-30 years to get there. You are just starting out.
- Get out and stay out of consumer debt (this includes student loans and car payments)
- Then start investing some money in low-cost mutual funds.
- Save an emergency fund (3-6 months)
- Buy a modest home (15-year mortgage 10-20% down)
- With any extra income: give some, spend some, and invest a lot.

<br><br>

[nothing is cheap](https://www.nytimes.com/2018/04/21/opinion/sunday/the-real-cost-of-cheap-shirts.html)

if I want to buy something, which is often, I always put it on my list. After some time, I can decide if that thing will improve the quality of my life, and it is within my means to buy it. 'within my means' is a budgeting problem that's in a process of constant revision. the important point here is that nothing is cheap-- as with all relative transactions, what you include in your system of transaction matters. that's not to argue naively for a zero-sum economic game, but perhaps there is some ethical conservation law... 

<br><br>

i needed to extract text from a PDF file without indexed text. 

I ended up finding a local solution using `imagemagick` and `tesseract`:

```brew install tesseract, imagemagick```

things didn't work so i tried

```brew install gs```

which work. then taking the `input.pdf` file i `converted` with `imagemagick`

```$ convert -density 300 input.pdf -depth 8 -strip -background white -alpha off image_file.tiff```

where these `convert` settings took a bit of trial and error. this tiff was `470MB` for 53 pages of large text. using `tesseract`, i made `output.txt` with 

```$ tesseract -l eng image_file.tif output```

<br><br>

[some optimism about America from the Atlantic](https://www.theatlantic.com/magazine/archive/2018/05/reinventing-america/556856/?single_page=true)

>What we learned from traveling was not that the hardest American challenges of this era are illusory. They’re very real, and divisions about national politics are intense. So we made a point of never asking, early on, “How’s Obama doing?,” or later, “Do you trust Hillary?” and “What about Trump?” The answers to questions like those won’t take you beyond what you’ve already heard ad nauseam on TV.

>Instead we asked people about their own lives and their own communities.

very Freire. 

<br><br>

[cool pics from a comet](https://twitter.com/Rainmaker1973/status/988711358358261762)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">This is what a view on a comet looks like, among dust, stars and cosmic ray hits, as captured by <a href="https://twitter.com/ESA_Rosetta?ref_src=twsrc%5Etfw">@ESA_Rosetta</a> on June 1, 2016 and processed by <a href="https://twitter.com/landru79?ref_src=twsrc%5Etfw">@landru79</a> from these raw data: <a href="https://t.co/h3BV6Z2V71">https://t.co/h3BV6Z2V71</a> <a href="https://t.co/w1Yv4OwIo1">pic.twitter.com/w1Yv4OwIo1</a></p>&mdash; Massimo (@Rainmaker1973) <a href="https://twitter.com/Rainmaker1973/status/988711358358261762?ref_src=twsrc%5Etfw">April 24, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<br><br>

[life is too short for bullshit](http://www.paulgraham.com/vb.html)

>Arguments of the form "Life is too short for x" have great force. It's not just a figure of speech to say that life is too short for something. It's not just a synonym for annoying. If you find yourself thinking that life is too short for something, you should try to eliminate it if you can.

>bullshit does have a distinctive character. There's something fake about it. It's the junk food of experience.

>Cultivate a habit of impatience about the things you most want to do.

>The "flow" that imaginative people love so much has a darker cousin that prevents you from pausing to savor life amid the daily slurry of errands and alarms.

>Relentlessly prune bullshit, don't wait to do things that matter, and savor the time you have. That's what you do when life is short.

<br><br>

[when capitalism kills good things like bicycles](https://www.theguardian.com/uk-news/2017/nov/25/chinas-bike-share-graveyard-a-monument-to-industrys-arrogance)

![](https://i.guim.co.uk/img/media/c217fdc4f8ce3df1ae171ccfcda6e0e8007676dc/64_0_2666_1600/master/2666.jpg?w=860&q=20&auto=format&usm=12&fit=max&dpr=2&s=05635ef64c53e356925e8fb3b87d92c1)

<br><br>

[Buckel's self-immolation](https://www.nytimes.com/2018/04/14/nyregion/david-buckel-dead-fire.html)

>Privilege, he said, was derived from the suffering of others.

>“Many who drive their own lives to help others often realize that they do not change what causes the need for their help,” Mr. Buckel wrote, adding that donating to organizations was not enough.

>By 11 a.m., the authorities had removed Mr. Buckel’s body, leaving a blackened patch and a circular indentation around which parks officials placed two orange cones.

>The grim scene stood in stark contrast to the rest of the park, which brimmed with activity. Several youth baseball games continued nearby and participants in PurpleStride, a walk dedicated to ending pancreatic cancer, strode along the bike path with runners and joggers.

<br><br>

[Finding your baboons?](https://en.wikipedia.org/wiki/Robert_Sapolsky)

>In 1978, Sapolsky received his B.A. in biological anthropology summa cum laude from Harvard University.[8] He then went to Kenya to study the social behaviors of baboons in the wild; after which he returned to New York; studying at Rockefeller University, where he received his Ph.D. in neuroendocrinology working in the lab of endocrinologist Bruce McEwen.
>Following Sapolsky's initial year-and-a-half field study in Africa, he returned every summer for another twenty-five years to observe the same group of baboons, from the late 70s to the early 90s. He spent 8 to 10 hours a day for approximately four months each year recording the behaviors of these primates.[9]

i have this idea of _raw material_. often (continental) philosophers use literature, poetry, and film as currency in arguments. language is borrowed from art as material to build rhetoric, to color examples. in the same way, scientists have raw material, they have experiences documenting the social habits of baboons, they have data from microscopes and sensors. we all have raw material in the way of experience. choosing experiences, making choices that lead to transformations in the world lead to changes in experience. what i am working to do is reflect on these experiences, use them as _raw material_ to craft new experiences.

reflect on your baboons. 
