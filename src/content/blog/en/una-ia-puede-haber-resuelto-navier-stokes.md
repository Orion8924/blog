---
titulo: "An AI may have solved Navier–Stokes. What does it mean, and which Millennium Prize Problem could be next?"
resumen: "OpenAI has presented a proof of one of the great open problems in mathematics. What has been solved, how an AI did it, and what it tells us about which problem could fall next."
fecha: 2026-09-17
categoria: ciencia
imagen: /images/navier-stokes-portada.jpg
imagenAlt: "PENDING"
imagenCredito: "PENDING"
---

OpenAI has presented a proof of one of the great open problems in mathematics. If it survives scrutiny by the community, it would be the second of the seven Millennium Prize Problems to fall. What exactly has been solved? How could an AI do it? And does this case tell us anything about which one could be next?

On 8 September 2026, [OpenAI announced](https://openai.com/index/navier-stokes-solution/) that one of its experimental artificial intelligence systems had found a solution to the Navier–Stokes problem, one of the seven celebrated Millennium Prize Problems.

The news is extraordinary, but it still calls for caution.

The Clay Mathematics Institute, the institution that created the Millennium Prize Problems, [has said](https://www.claymath.org/news/navier-stokes-announcement/) that Navier–Stokes has "apparently been settled", not that the process is over. Its rules require publication, time for scrutiny and general acceptance of the solution within the mathematical community before a result is formally recognised.

OpenAI, for its part, has said it does not intend to claim the million dollars attached to the problem.

So the prudent formulation, for now, is this: an AI may have solved Navier–Stokes.

## What problem exactly has it solved?

The Navier–Stokes equations describe how fluids move.

And a fluid is not only water. Air is a fluid too. That is why these equations lie behind phenomena as different as water flowing through a pipe, the aerodynamics of an aircraft or certain models of the atmosphere.

The equations have been in use for a very long time. The problem was never how to write them down or apply them, but how to understand something much more basic about them.

Suppose we start from a perfectly regular fluid: its velocity is finite and changes smoothly from one point to the next.

The question was:

do the equations guarantee that this regularity will last forever, or can a singularity appear in finite time?

In the solution presented by OpenAI, the latter happens.

The motion concentrates progressively in an ever smaller region. As a certain instant approaches, the maximum velocity of the fluid grows without bound, even though the total energy remains bounded. The solution then stops being smooth: a singularity appears.

There is an important detail.

In OpenAI's construction, a smooth external force acts on the fluid.

At first sight this may look like a cheat: if we are pushing the fluid from outside, have we really solved Navier–Stokes?

Yes, if the proof is correct.

The official statement of the Millennium Prize Problem expressly contemplated this possibility as one of the valid ways of solving it. So it would not be a partial solution: it would settle the problem as Clay formulated it.

A different and even stronger question would remain open: whether such a singularity can also appear without any external force.

But that would be another problem.

## Thousands of agents researching at once

Probably the most interesting part of the story is how the proof was reached.

OpenAI did not put a single chatbot in front of the equations and wait for it to have a flash of inspiration.

The experiment looks more like having built a gigantic artificial research institute.

The company deployed groups of agents capable of consulting the literature, running code, developing arguments and exploring different strategies. Promising results could then be passed on to other groups.

The team that ended up producing the solution came to involve on the order of 10,000 concurrent agents.

And the story had a crucial intermediate step.

OpenAI had sent agents not only against Navier–Stokes but against other Millennium Prize Problems and related problems. Around a hundred agents worked for about 50 hours on the Euler equations, close relatives of Navier–Stokes, and first managed to solve a singularity-formation problem with no external force.

That advance suggested Navier–Stokes was especially promising.

OpenAI then concentrated far more resources there and handed the Euler result to the agents working on the problem.

The solution appeared some 88 hours after the experiments began. The attack on Navier–Stokes alone generated around 2.7 million messages and roughly 130 billion output tokens.

Afterwards, the proof was formalised in Lean, a system capable of mechanically checking that, once the definitions and axioms are fixed, each logical step follows correctly from the previous ones.

That provides a very strong guarantee, though it does not remove the human work: mathematicians still have to check that the formulation entered into Lean represents exactly the original problem, and study what ideas the proof actually contains.

## The AI did not start from scratch

Nor did the strategy it used arise out of nothing inside the machines.

The European Mathematical Society has pointed out that the solution is closely related to a line of research developed earlier by Diego Córdoba, Luis Martínez-Zoroa and Fan Zheng, itself resting on decades of work on singularities in fluid equations.

Two of those researchers, Córdoba and Martínez-Zoroa, are Spanish.

Over the years they had developed a strategy based on vorticity structures at progressively smaller scales. One structure amplifies a smaller one, that one does the same to the next, and the motion concentrates more and more.

That programme brought mathematicians progressively closer to the kind of singularity the Millennium Prize Problem required.

The importance of that contribution is not a patriotic claim made after the fact. Charles Fefferman, author of the official statement of the Navier–Stokes problem for the Clay Mathematics Institute, has singled out Córdoba and Martínez-Zoroa as central figures in this story.

So it would be misleading to present the result as if ten thousand agents had been handed a blank sheet and suddenly discovered a new way of thinking about fluids.

But it would be equally wrong to say they simply copied an existing proof.

The complete proof did not exist.

What existed was a promising path.

The AI had to develop it, attempt constructions, find arguments, discard dead ends and finally complete something human researchers had not yet managed to prove.

The fundamental difference seems to have been scale.

A mathematician may wonder whether to spend several weeks on strategy A or drop it to try B.

Here there could be hundreds of agents simultaneously exploring variants of A, hundreds more working on B and as many again trying C.

It is not simply "thinking ten thousand times faster".

It is doing part of mathematical research in a massively parallel way.

## A race that had already begun

Nor was OpenAI the only group using AI along this line.

The mathematicians Tristan Buckmaster, of New York University, and Levent Alpöge, of Anthropic, had been working for some time with artificial intelligence models to extend the earlier ideas, and had obtained a related result for the Euler equations with an external force.

OpenAI acknowledges their priority in that result and also admits that it launched its big push on 1 September after hearing rumours of important mathematical advances that it later connected to their work.

The coincidence gave rise to a dispute over priority, and over whether Buckmaster's private work, carried out partly with OpenAI products, might somehow have influenced the system. OpenAI denies this and says an internal investigation concluded that those prompts could not have influenced the model, even through training.

There is no need to settle that controversy here.

What matters for our story is something else: several human groups, also using artificial intelligence, were beginning to travel a line of research that had just become especially fertile.

## Can an AI produce new knowledge?

Here a question far larger than Navier–Stokes appears.

For years it has been common to picture generative models as systems locked inside a kind of circle.

They learn from texts, images, code or music previously created by humans. They can then recombine and generalise that knowledge in surprising ways.

But can they really cross the frontier of what is known?

Navier–Stokes offers a partial answer.

If the proof ends up being validated, the AI will have contributed to obtaining a mathematical result that no human being had yet managed to prove, even though the immediately preceding advances had already led specialists such as Terence Tao to consider it very likely that a construction of this kind was possible.

That would be new mathematical knowledge.

But it does not necessarily mean the AI invented a new conceptual way of thinking about the problem.

We can distinguish three levels.

The first is obtaining a previously unknown result. Navier–Stokes seems to be at that level already, subject to validation.

The second would be inventing a fundamentally new mathematical method to obtain it. Here the answer is far less clear: the main strategy had deep roots in earlier human research.

And the third would be more ambitious still: inventing a new intellectual paradigm.

We do not know whether today's AI can do that.

Moreover, a new theorem is not necessarily the same as new human understanding. A machine could produce a correct and extremely complex proof without mathematicians yet grasping which essential ideas make the argument work.

So the result is impressive without needing to be exaggerated.

If confirmed, it will show that an AI can take existing human knowledge as its starting point and carry it to a result we had not yet managed to reach.

The great unknown is whether it can also invent, on its own, the conceptual frameworks that open completely new paths.

## What are the Millennium Prize Problems?

In 2000, the Clay Mathematics Institute selected seven problems representing some of the great open frontiers of mathematics and set aside seven million dollars: one for each problem.

The institute had been founded two years earlier by the American businessman Landon T. Clay and his wife, Lavinia D. Clay, who devoted part of their fortune to advancing mathematics.

There is no time limit for solving the problems.

Until now only one had fallen: the Poincaré conjecture, proved by the Russian mathematician Grigori Perelman.

Clay awarded him the million dollars in 2010.

Perelman turned it down.

It does not seem to have been mere eccentricity. Among other things, he considered that the contribution of Richard Hamilton, the mathematician who had developed the programme on which his solution rested, had been no smaller than his own. Four years earlier he had also declined the Fields Medal.

There is a curious echo of the present case.

Hamilton opened a path that Perelman managed to complete.

Now Córdoba, Martínez-Zoroa, Zheng and other researchers have built much of the path that artificial intelligence systems may have finished travelling.

In mathematics, as in much of science, the last step rarely comes out of nowhere.

## Which problems would remain?

If Navier–Stokes is eventually accepted, five Millennium Prize Problems would remain.

The **Riemann hypothesis** seeks to prove a property of the zeta function that is closely related to the distribution of the prime numbers. The zeros of the function are not the primes, but their position holds deep information about how the primes are distributed.

**P versus NP** asks, simplifying enormously, whether every problem whose solution can be checked quickly can also be solved quickly. Its answer would have enormous consequences for computing, optimisation and cryptography.

The **Birch and Swinnerton-Dyer conjecture** connects the rational solutions of equations called elliptic curves with the behaviour of an analytic function associated with them.

The **Hodge conjecture** seeks to build a deep bridge between different ways of describing geometric objects, especially algebraic geometry and topology.

And **Yang–Mills and the mass gap** aims to give a rigorous mathematical foundation to a theory used with enormous success in particle physics.

Solving any of them need not produce a new technology the next day. Much of their importance lies in the mathematical tools and connections that would have to be discovered along the way.

But Navier–Stokes now raises an unavoidable question.

## Which one could an AI solve next?

We do not know.

And any ranked list would be little more than a bet.

But the Navier–Stokes case does let us ask what features seem to favour the capabilities artificial intelligence has just demonstrated.

There was a large body of prior knowledge, an especially promising recent human line of work, intermediate problems that could be used as stepping stones, and an enormous technical space of possibilities that could be divided among thousands of agents.

Navier–Stokes also had a particular advantage: one of the valid ways of solving it was to construct a single example that developed a singularity.

That fits especially well with a strategy capable of exploring many different constructions.

For several of the remaining conjectures, if they are true as is generally expected, the challenge would be different: one would have to prove a statement valid for infinitely many cases. Finding millions of favourable examples would never be enough.

Even so, Birch–Swinnerton-Dyer and the Riemann hypothesis are especially interesting.

Both have vast bodies of prior knowledge, partial results, intermediate problems and a significant computational dimension. They are exactly the kind of ecosystem in which thousands of agents can try different paths and share progress.

But Riemann also shows the limit of this strategy: you can check ten trillion zeros and still have proved nothing about all the rest. At some point you need an idea capable of controlling infinitely many cases at once.

P vs NP presents another obstacle. Decades of research have shown that whole families of techniques are not enough to solve it. Ten thousand agents exploring variants of a strategy known to be insufficient do not necessarily solve anything.

Hodge is harder to classify: there is a great deal of prior knowledge, but it is not clear that its main bottleneck is the kind of massively parallel exploration that has worked now.

And Yang–Mills seems even less like Navier–Stokes. Its resolution appears to require new ideas and part of the very mathematical infrastructure needed to formulate the theory rigorously.

That brings us back to the question that really matters.

## The real question after Navier–Stokes

Perhaps the most interesting thing about this story is not guessing whether the next problem will be Riemann or Birch–Swinnerton-Dyer.

It is knowing what kind of science an artificial intelligence can do.

If the proof ends up being validated, an AI will have used existing human knowledge as a starting point to reach a mathematical result we had not yet managed to prove.

It will therefore have contributed to pushing back the frontier of knowledge.

But the hardest question remains.

What will happen when there is no good human strategy to develop?

Will the AI be able to invent one?

Will it be capable not only of travelling new paths, but of imagining a completely different way of looking at the territory?

The mathematical equivalent of inventing cubism before Picasso.

Navier–Stokes does not yet let us answer.

But if one day the answer is yes, the question of which Millennium Prize Problem will be next will start to feel small.

Because then we will no longer simply be asking whether artificial intelligence can help us move faster along the frontiers of science.

We will be asking how far it can push them.
